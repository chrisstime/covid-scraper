from flask import Blueprint, render_template, abort, request, jsonify
from jinja2 import TemplateNotFound
from flask_paginate import Pagination, get_page_parameter
from .scrapers.nsw_covid_scraper import NswCovidScraper

AUSTRALIA_BLUEPRINT = Blueprint('australia', __name__,
                        template_folder='templates')
NCS = NswCovidScraper()

@AUSTRALIA_BLUEPRINT.route('/cases_in_australia', methods=['GET'])
def australia():
    try:
        search = False
        q = request.args.get('q')
        if q:
            search = True

        page = request.args.get(get_page_parameter(), type=int, default=1)
        total_per_page = 20
        all_cases = NCS.load_all_cases()
        all_cases_len = len(all_cases)
        page_set = total_per_page * page
        results = all_cases[page_set-total_per_page:page_set]
        pagination = Pagination(
            page=page, per_page=total_per_page, 
            total=all_cases_len, search=search, 
            record_name='results'
            )
        
        return render_template(
            'australia.html', title='COVID-19 Cases in Australia',
            location='in Australia',
            councils=NCS.get_available_councils(),
            total_cases_nsw=all_cases_len,
            results = results,
            update_cases= NCS.update_cases(),
            pagination = pagination
            )
    except TemplateNotFound:
        abort(404)

@AUSTRALIA_BLUEPRINT.route('/_search_by_postcode')
def search_by_postcode():
    postcode = request.args.get('postcode', 0, type=int)
    results = NCS.get_cases_by_postcode(postcode)
    
    return jsonify(results)

@AUSTRALIA_BLUEPRINT.route('/_update_cases')
def update_cases():
    NCS.update_cases()

@AUSTRALIA_BLUEPRINT.route('/_load_all_cases')
def load_cases():
    return NCS.load_all_cases()