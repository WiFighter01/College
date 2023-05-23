import requests

# API
# HTTP or HTTPS
# XML
# JSON
# REST
# REST full API
# https://seapi.dev/api/people/1/


# response = requests.get('https://pruffme.com/')
# response.encoding = 'utf-8'
# print(type(response), response)
# print(response.text)

# http://site.com?first=1&second=name

# response = requests.get('https://swapi.dev/api/planets/10/')
# print(response)
# text = response.text
# print(type(text), text)
# json = response.json()
# print(type(json), json)
# for key in json:
#     print(f'{key}: {json[key]}')


param = {
    'lang': 'ru',
    'format': 'j1'
}

# https://wttr.in/Moscow?lang=ru&format=j1
response = requests.get('https://wttr.in/Moscow', params=param)
response.encoding = 'utf-8'
print(response)
print(response.text)
