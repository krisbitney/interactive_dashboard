import requests
from collections import defaultdict

def request_wb_data(indicator):
    # gdp -> NY.GDP.MKTP.CD
    url_base = 'http://api.worldbank.org/v2/countries/cn;us/indicators/' + indicator
    params = {'format': 'json', 'per_page': '500', 'date': '2000:2017'}
    try:
        data = requests.get(url_base, params=params)
    except:
        data = None
    return data

def clean_json_data(request):
    data = defaultdict(list)
    for entry in request.json()[1]:
        # check if country is already in dictionary. If so, append the new x and y values to the lists
        # if country not in dictionary, then initialize the lists that will hold the x and y values
        if not data[entry['country']['value']]:
            data[entry['country']['value']] = [[], []]
        data[entry['country']['value']][0].append(int(entry['date']))
        data[entry['country']['value']][1].append(float(entry['value']))
    return data
