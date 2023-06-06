import requests

TOKEN = 'TOKEN'
url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
params = {'chat_id': '___',
          'text': 'Hello'}
response = requests.get(url, params)
print(response.json())