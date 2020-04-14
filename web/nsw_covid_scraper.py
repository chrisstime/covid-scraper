import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class NswCovidScraper:
    def __init__(self, conn):
        self.aus_gov_site = 'https://data.nsw.gov.au/data/api/3/action/datastore_search_sql?sql=SELECT'
        self.location_rid = '21304414-1ff1-4243-a5d2-f52778048b29'
        self.age_range_rid = '24b34cb5-8b01-4008-9d93-d14cf5518aec'
        self.likely_source_rid = '2f1ba0f3-8c21-4a86-acaf-444be4401a6d'

        self.c = conn.cursor()

    def update_cases(self):
        location_api_query = '''{} notification_date, postcode,
            lhd_2010_code AS local_health_district_code,
            lhd_2010_name AS local_health_district,
            lga_code19 AS local_gov_area_code,
            lga_name19 AS local_gov_area
            FROM "{}"
            WHERE notification_date > '''.format(self.aus_gov_site, self.location_rid)
        results = requests.get(location_api_query)

        return results.json()['result']['records']

    def get_available_councils(self):
        self.c.execute('''SELECT DISTINCT local_gov_area FROM cases_by_loc''')
        councils = [str(results[0]) for results in self.c.fetchall()]
        councils.sort()
        
        return councils

    def get_cases_by_council(self, council):
        self.c.execute('''SELECT * FROM cases_by_loc 
            WHERE local_gov_area like {}'''.format(council))

        return self.c.fetchall()

    def get_cases_by_postcode(self, postcode):
        self.c.execute('''SELECT * FROM cases_by_loc
            WHERE postcode = "{}"'''.format(postcode))

        return self.c.fetchall()

    def get_last_case(self, table_name):
        self.c.execute('''SELECT * FROM "{table}" 
            WHERE id=(SELECT max(id) FROM {table})'''.format(table = table_name))
        
        return self.c.fetchall()
