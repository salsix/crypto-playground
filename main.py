from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
    'slug':'bitcoin',
    'convert':'EUR'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'a6952186-cdb5-4263-9d7c-250c9f62ad6a',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data['data']['1']['quote']['EUR']['price'])
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

def test():
    print('Hi,')


if __name__ == '__main__':
    test()
