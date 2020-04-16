from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
from .nsw_covid_scraper import NswCovidScraper

AUSTRALIA_BLUEPRINT = Blueprint('australia', __name__,
                        template_folder='templates')

@AUSTRALIA_BLUEPRINT.route('/cases_in_australia', methods=['GET'])
def australia():
    try:
        acs = NswCovidScraper()
        results = acs.get_cases_by_postcode('2121')

        return render_template(
            'australia.html', title='COVID-19 Cases in Australia',
            location='in Australia',
            councils=acs.get_available_councils(),
            results=results
            )
    except TemplateNotFound:
        abort(404)