from flask import Blueprint, render_template, abort, request, jsonify
from jinja2 import TemplateNotFound
from .scrapers.nsw_covid_scraper import NswCovidScraper

AUSTRALIA_BLUEPRINT = Blueprint('australia', __name__,
                        template_folder='templates')
NCS = NswCovidScraper()

@AUSTRALIA_BLUEPRINT.route('/cases_in_australia', methods=['GET'])
def australia():
    try:
        return render_template(
            'australia.html', title='COVID-19 Cases in Australia',
            location='in Australia',
            councils=NCS.get_available_councils(),
            total_cases_nsw=NCS.get_total_cases(),
            results = NCS.load_all_cases(),
            update_cases= NCS.update_cases()
            )
    except TemplateNotFound:
        abort(404)
