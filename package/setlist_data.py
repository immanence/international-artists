import requests
import json
from package.config import *

headers = {'Accept': 'application/json', 'x-api-key': token}

def get_data(number_of_pages, year):
    data_with_dups = []
    data = []
    for i in range(1,number_of_pages+1):
        url = 'https://api.setlist.fm/rest/1.0/search/setlists?p=' + str(i) + '&year=' +str(year)
        response = requests.get(url, headers=headers)
        raw_data = json.loads(response.content)
        narrowed_raw_data = raw_data['setlist']
        empty_sets_removed = [item for item in narrowed_raw_data if item['sets']['set'] != []]
#        cleaned_page = [item for item in empty_sets_removed if isinstance(item['sets']['set'][0]['song'][0],dict)]
        data_with_dups = data_with_dups + empty_sets_removed
    for item in data_with_dups:
        if item['id'] not in set([datum['id'] for datum in data]):
            data.append(item)
    return data

data = get_data(51, 2017)
print('done getting data')
