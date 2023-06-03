import requests

print('Задача 1')
# Задача 1
response = requests.get('https://swapi.dev/api/people')
print(response)
json = response.json()
list_of_persons = json['results']
for i in range(len(list_of_persons)):
    print(f'{i + 1}: {list_of_persons[i]["name"]}')

print()

print('Задача 2')
# Задача 2
# Можно также решить с параметрами
# param = {'search': 'Millennium Falcon'}
response = requests.get('https://swapi.dev/api/starships')
print(response)
json = response.json()
list_of_starships = json['results']
for i in range(len(list_of_starships)):
    if list_of_starships[i]['name'] == 'Millennium Falcon':
        print(f"Стоимость {list_of_starships[i]['name']}: {list_of_starships[i]['cost_in_credits']} кредитов")
    else:
        continue
