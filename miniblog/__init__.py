from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from miniblog.models import DBSession, Base


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('add_entry', '/add')
    config.add_route('view_entry', '/entry/{id_}')
    config.add_route('about', '/about')
    config.add_route('search', '/search')
    config.scan()
    return config.make_wsgi_app()