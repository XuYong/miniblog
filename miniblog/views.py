from functools import partial
from miniblog.forms import EntryForm, CategoryForm
from miniblog.models import DBSession, Entry, Category, get_recent_posts, \
    get_categories
from pyramid.decorator import reify
from pyramid.httpexceptions import HTTPFound, HTTPBadRequest, \
    HTTPInternalServerError, HTTPNotFound
from pyramid.response import Response
from pyramid.security import remember, forget, authenticated_userid
from pyramid.view import view_config, notfound_view_config
from sqlalchemy import func
from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm import subqueryload
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql import exists
from sqlalchemy.sql.expression import desc
from webhelpers.paginate import Page, PageURL_WebOb
from webob.multidict import MultiDict
import json
import logging
import requests
import transaction


log = logging.getLogger(__name__)

class BaseView(object):
    """View for all user related stuff."""

    def __init__(self, request):
        self.request = request

    @reify
    def categories(self):
        """A list of :class:`miniblog.models.Category` that have entries
        attached."""
        categories = DBSession.query(Category)\
            .filter(exists().where(Category.name == Entry.category_name))\
            .all()
        return categories

    @reify
    def recent(self):
        """A list of recent posts as returned by
        :func:`miniblog.models.get_recent_posts`."""
        recent_entries = get_recent_posts()
        return recent_entries

    @view_config(route_name='home', renderer='entries.mako')
    @view_config(route_name='home_paged', renderer='entries.mako')
    def home(self):
        current_page = int(self.request.matchdict.get('page', 1))
        all_entries = DBSession.query(Entry)\
            .order_by(desc(Entry.entry_time))
        page_url = partial(self.request.route_url, 'home_paged')
        page = Page(all_entries, page=current_page, items_per_page=5,
             item_count=all_entries.count(),
             url=page_url)
        return {'entries': page}

    @view_config(route_name='view_entry', renderer='entry.mako')
    def view_entry(self):
        id_ = self.request.matchdict['id_']
        try:
            entry = DBSession.query(Entry).filter(Entry.id == id_).one()
        except NoResultFound:
            raise HTTPNotFound("Blog post not found. This blogpost was "
                               "possibly deleted.")
        return {'entry': entry}

    @view_config(route_name='view_category', renderer='entries.mako')
    def view_category(self):
        current_page = int(self.request.matchdict.get('page', 1))
        id_ = self.request.matchdict['id_']
        page_url = partial(self.request.route_url, 'view_category')
        entries = DBSession.query(Entry).\
            filter(Entry.category_name == id_).\
            order_by(desc(Entry.entry_time))
        page = Page(entries, page=current_page, items_per_page=5,
             item_count=entries.count(),
             url=page_url)
        return {'entries': page}

    @view_config(route_name='about', renderer='about.mako')
    def about(self):
        return {}

    @view_config(route_name='view_categories', renderer='categories.mako')
    def view_categories(self):
        current_page = int(self.request.GET.get('page', 1))
        last_entry = DBSession.query(Entry.entry_time).\
                    filter(Entry.category_name == Category.name).\
                    order_by(desc(Entry.entry_time)).\
                    limit(1).\
                    as_scalar()
        categories = DBSession.query(Category, last_entry)

        page_url = partial(self.request.route_url, 'view_categories')
        page = Page(categories, page=current_page, items_per_page=20,
                    item_count=categories.count(),
                    url=page_url)
        return {'categories': page}


    @view_config(route_name='search', renderer='search.mako')
    def search(self):
        results = DBSession.query(Entry)\
            .filter(Entry.title.like('%%%s%%' % (self.request.GET['search'])))\
            .all()
        return {'results': results}

    @view_config(route_name='login')
    def login(self):
        verify_url = self.request.registry.settings['persona_verifier_url']
        try:
            assertion = self.request.POST['assertion']
        except KeyError:
            raise HTTPBadRequest("No assertion provided, could not log in!")
        data = {'assertion': assertion, 'audience': self.request.host_url}
        resp = requests.post(verify_url, data=data, verify=True)

        if resp.ok:
            verification_data = json.loads(resp.content)

            if verification_data['email'] != self.request.registry.settings['admin_email']:
                raise HTTPBadRequest("Only the defined administrator is allowed to log in!")

            if verification_data['status'] == 'okay':
                # Log the user in
                log.info("User %s logged in as Blog admin" % verification_data['email'])
                headers = remember(self.request, verification_data['email'])
                return Response(json.dumps(verification_data), headers=headers)

        raise HTTPInternalServerError("Something went wrong with the assertion!")

    @view_config(route_name='logout')
    def logout(self):
        user_mail = authenticated_userid(self.request)
        log.info("User %s logged out" % user_mail)
        headers = forget(self.request)
        return Response(headers=headers)

    @notfound_view_config(renderer='404.mako')
    def view_404(self):
        return {'msg': self.request.exception.message}


class AdminView(BaseView):
    """View for all administration stuff.

    Everything with a view config needs to have the permission ``edit``
    or it might expose administrative functions to the end user:

    .. code-block:: python

        @view_config(route_name='...', permission='edit')
        def do_admin_stuff(self):
            ...
    """

    @view_config(route_name='delete_entry', permission='edit')
    def delete_entry(self):
        entry_id = self.request.matchdict["id_"]
        entry = DBSession.query(Entry).filter(Entry.id == entry_id).one()
        DBSession.delete(entry)
        get_categories.invalidate()
        get_recent_posts.invalidate()
        return HTTPFound(location=self.request.route_url('home'))

    @view_config(route_name='manage_categories',
                 renderer='edit_categories.mako',
                 permission='edit')
    def manage_categories(self):
        form = CategoryForm(self.request.POST)
        if self.request.method == 'POST':
            category = Category(form.data['name'])
            DBSession.add(category)
            get_categories.invalidate()
            return HTTPFound(location=self.request.route_url('manage_categories'))
        categories = DBSession.query(Category).all()
        return {'form': form, 'categories': categories}

    @view_config(route_name='edit_entry', renderer='add.mako',
                 permission='edit')
    @view_config(route_name='add_entry', renderer='add.mako',
                 permission='edit')
    def add_entry(self):
        entry_id = self.request.matchdict.get("id_", 0)
        if entry_id:
            entry = DBSession.query(Entry).filter(Entry.id == entry_id).one()
            form_data = MultiDict({'title': entry.title, 'text': entry._text,
                                   'category': entry.category_name})
            form_data.update(self.request.session.get("edit_entry_%i_form" % entry.id, {}))
        else:
            entry = None
            form_data = MultiDict(self.request.session.get("add_entry_form", {}))
        form_data.update(self.request.POST)
        form = EntryForm(form_data)
        form.category.choices = [('', ' - None - ')] + [(name[0], name[0]) for name in get_categories()]
        preview = None
        if self.request.method == 'POST':
            if not form.validate():
                for field, errors in form.errors.items():
                    for error in errors:
                        self.request.session.flash('Field "%s" has the following error: "%s"' % (field, error))
                if entry:
                    self.request.session["edit_entry_%i_form" % entry.id] = form.data
                else:
                    self.request.session["add_entry_form"] = form.data
                return HTTPFound(location=self.request.route_url('add_entry'))

            if form.submit.data:
                if "category" in form.data and form.data["category"]:
                    category = DBSession.query(Category)\
                        .filter(Category.name == form.data["category"]).one()
                else:
                    category = None
                if not entry:
                    entry = Entry(form.data["title"], form.data["text"])
                    entry.category = category
                    if "add_entry_form" in self.request.session:
                        del self.request.session["add_entry_form"]
                    DBSession.add(entry)
                else:
                    if "edit_entry_%i_form" \
                            % entry.id in self.request.session:
                        del self.request.session["edit_entry_%i_form"
                                                 % entry.id]
                    entry._text = form.data["text"]
                    entry.title = form.data["title"]
                    entry.category = category
                DBSession.flush()
                get_categories.invalidate()
                get_recent_posts.invalidate()
                return HTTPFound(location=self.request.route_url('view_entry', id_=entry.id))
            if form.preview.data:
                preview = entry
        return {'form': form, 'preview': preview}

    @view_config(route_name='delete_category', permission='edit')
    def delete_category(self):
        category = DBSession.query(Category)\
            .options(subqueryload(Category.entries))\
            .filter(Category.name == self.request.matchdict["name_"])\
            .one()
        if category.entries:
            self.request.session.flash(
                'There are still entries in category %s, cannot delete!'
                % category.name)
        else:
            DBSession.delete(category)
        return HTTPFound(location=self.request.route_url('manage_categories'))
