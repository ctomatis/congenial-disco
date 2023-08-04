from jinja2 import Template


def render_body(tmpl, **kwargs):
    with open(tmpl) as fp:
        template = Template(fp.read())
    return template.render(kwargs)
