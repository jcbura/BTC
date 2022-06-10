from requests import Request, Session
from datetime import datetime
now = datetime.now()
import json
import sys

url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'

parameters = {
    'slug' : 'bitcoin',
    'convert' : 'USD'
}

headers = {
    'Accepts' : 'application/json',
    'X-CMC_PRO_API_KEY' : '816fabc0-cb01-4b0f-86cd-9b6ddff6b050'
}

session = Session()
session.headers.update(headers)

response = session.get(url, params=parameters)

original_stdout = sys.stdout

with open('/Users/jason/BTC_PRICE_CHECKER/btc_price.txt', 'a') as f:
    sys.stdout = f
    print('Price of bitcoin @ {}'.format(now), 'is:')
    print(json.loads(response.text)['data']['1']['quote']['USD']['price'])
    sys.stdout = original_stdout

