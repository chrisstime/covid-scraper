import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
from db.db import get_db, close_db


class NswCovidScraper:
    def __init__(self):
        self.aus_gov_site = 'https://data.nsw.gov.au/data/api/3/action/datastore_search_sql?sql=SELECT'
        self.location_rid = '21304414-1ff1-4243-a5d2-f52778048b29'
        self.age_range_rid = '24b34cb5-8b01-4008-9d93-d14cf5518aec'
        self.likely_source_rid = '2f1ba0f3-8c21-4a86-acaf-444be4401a6d'
        self.cases_by_loc_table = 'cases_by_loc'
        self.cases_by_age_range_table = 'cases_by_age'
        self.cases_by_infection_source_table = 'cases_by_infection_source'

    def update_cases(self):
        location_api_query = '''{} _id as id, notification_date, postcode,
            lhd_2010_code AS local_health_district_code,
            lhd_2010_name AS local_health_district,
            lga_code19 AS local_gov_area_code,
            lga_name19 AS local_gov_area
            FROM "{}"
            WHERE _id > {}'''.format(
                self.aus_gov_site, self.location_rid,
                self.get_last_case_id(self.cases_by_loc_table)
                )
        response = requests.get(location_api_query)
        json_response = response.json()
        self._insert_records_to_db(json_response['result']['records'])

        return json_response['success']

    def _insert_records_to_db(self, records):
        conn = get_db()
        df = DataFrame(records)
        df.to_sql('cases_by_loc', conn, if_exists='append', index=False)
        close_db()

    def get_available_councils(self):
        c = get_db().cursor()
        c.execute('''SELECT DISTINCT local_gov_area FROM cases_by_loc''')
        councils = [str(results[0]) for results in c.fetchall()]
        c.close()
        close_db()
        councils.sort()
        
        return councils

    def get_cases_by_council(self, council):
        c = get_db().cursor()
        c.execute('''SELECT * FROM cases_by_loc 
            WHERE local_gov_area like {}'''.format(council))
        cases = [[item for item in results] for results in c.fetchall()]
        c.close()
        close_db()

        return cases

    def get_cases_by_postcode(self, postcode):
        c = get_db().cursor()
        c.execute('''SELECT * FROM cases_by_loc
            WHERE postcode LIKE "{}"'''.format(postcode))
        cases = [[item for item in results] for results in c.fetchall()]
        c.close()
        close_db()

        return cases

    def get_last_case_id(self, table_name):
        c = get_db().cursor()
        c.execute('''SELECT id FROM "{table}" 
            WHERE id=(SELECT max(id) FROM {table})'''.format(table = table_name))
        last_case_update = c.fetchone()
        c.close()
        close_db()

        return last_case_update[0]
    
    def load_all_cases(self):
        c = get_db().cursor()
        c.execute('''SELECT * FROM cases_by_loc''')
        cases = [[item for item in results] for results in c.fetchall()]
        c.close()
        close_db()

        return cases
