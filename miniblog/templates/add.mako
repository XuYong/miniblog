<%inherit file="layout.mako" />
<form method="POST">
	${form.title.label} ${form.title()} <br/>
	${form.text.label} ${form.text()} <br/>
	${form.submit()} <br/>
</form>