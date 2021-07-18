import requests
from datetime import datetime

USERNAME = 'rafguzdev'
TOKEN = 'aasfdewfwedwefff'

pixela = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
# responce = requests.post(url=pixela, json=user_params)
# print(responce.text)

graph = f'{pixela}/{USERNAME}/graphs'
graph_config = {
    'id': 'graph1',
    'name': 'Code Graph',
    'unit': 'commit',
    'type': 'int',
    'color': 'sora'
}
headers = {
    'X-USER-TOKEN': TOKEN
}
# responce = requests.post(url=graph, json=graph_config, headers=headers)
# print(responce.text)

post_url = f'{pixela}/{USERNAME}/graphs/graph1'
json = {
    'date': datetime.now().strftime("%Y%m%d"),
    'quantity': input('How many commits: ')
}
responce = requests.post(url=post_url, json=json, headers=headers)
print(responce.text)

# del_url = f'{pixela}/{USERNAME}/graphs/graph1/{datetime.now().strftime("%Y%m%d")}'
# responce = requests.delete(url=del_url, headers=headers)
# print(responce.text)
