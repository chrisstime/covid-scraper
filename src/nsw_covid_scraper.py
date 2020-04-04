import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class NswCovidScraper:
    def __init__(self):
        self.aus_gov_site = 'https://data.nsw.gov.au/data/api/3/action/datastore_search_sql?sql=SELECT'
        self.district_resource_id = '21304414-1ff1-4243-a5d2-f52778048b29'
        self.age_range_resource_id = '24b34cb5-8b01-4008-9d93-d14cf5518aec'

    def get_cases_by_postcode(self, postcode):
        sql_api_query = '''{} notification_date AS case_report_date,
            lhd_2010_name AS region, 
            lga_name19 AS council FROM "{}" WHERE postcode={}'''.format(
            self.aus_gov_site, self.district_resource_id, int(postcode)
            )
        results = requests.get(sql_api_query)
        
        return results.json()['result']['records']
    
    def get_available_councils(self):
        sql_api_query = '''{} DISTINCT 
        lga_name19 AS council FROM "{}"'''.format(
            self.aus_gov_site, self.district_resource_id
            )
        results = requests.get(sql_api_query)
        
        return results.json()['result']['records']

    def get_cases_by_council(self, council):
        sql_api_query = '''{} notification_date AS case_report_date,
            lhd_2010_name AS region, 
            postcode FROM "{}" WHERE council LIKE "{}"'''.format(
            self.aus_gov_site, self.district_resource_id, council
            )
        results = requests.get(sql_api_query)
        
        return results.json()['result']['records']

cs = NswCovidScraper()
# print('Type in a postcode:')
# postcode = input()
# print(cs.get_cases_by_postcode(postcode))
councils = cs.get_available_councils()
my_df = pd.DataFrame.from_dict(councils)
print(my_df)