from flask import Blueprint, render_template, abort, url_for
from jinja2 import TemplateNotFound

ABOUT_BLUEPRINT = Blueprint('about', __name__,
                        template_folder='templates')

@ABOUT_BLUEPRINT.route('/about')
def about():
    try:
        return render_template('about.html', title='What is COVID-19?')
    except TemplateNotFound:
        abort(404)