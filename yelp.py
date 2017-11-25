import requests
from urlparse import urljoin
import random
import os
from flask import render_template
from flask_ask import statement



# https://www.yelp.com/developers/v3/manage_app

CLIENT_ID = os.environ.get("YELP_CLIENT_ID")
CLIENT_SECRET = os.environ.get("YELP_CLIENT_SECRET")


API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
TOKEN_PATH = '/oauth2/token'
GRANT_TYPE = 'client_credentials'


SEARCH_LIMIT = 10


def obtain_bearer_token(host, path):
    url = urljoin(host,path)

    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': GRANT_TYPE,
    }

    headers = {
        'content-type': 'application/x-www-form-urlencoded',
    }

    response = requests.request('POST', url, data=data, headers=headers)
    bearer_token = response.json()['access_token']
    return bearer_token

def search(location):
    bearer_token=obtain_bearer_token(API_HOST,TOKEN_PATH)
    url_params = {
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT,
        'term': "restaurants",
        'open_now': True
    }
    return request(API_HOST, SEARCH_PATH, bearer_token, url_params=url_params)


def request(host, path, bearer_token, url_params=None):
    url_params = url_params or {}
    url = urljoin(host, path)
    headers = {
        'Authorization': 'Bearer %s' % bearer_token,
    }

    response = requests.request('GET', url, headers=headers, params=url_params)

    rjson = response.json()
    business_list = rjson['businesses']
    random_business = (random.choice(business_list))
    random_business_name=random_business['name']
    random_business_rating=random_business['rating']
    random_business_address=' '.join(random_business['location']['display_address'])
    print random_business_address

    response = render_template ('random_restaurant', random_business_name=random_business_name, random_business_rating=random_business_rating, random_business_address=random_business_address)
    return statement(response)



