from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound 

index = Blueprint('index', __name__,
                        template_folder='templates')

@index.route('/', defaults={'page': 'index'})
@index.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)
