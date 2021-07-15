import requests

params = {
    'amount': 10,
    'type': 'boolean',
}

data = requests.get(url='https://opentdb.com/api.php', params=params)
data.raise_for_status()
question_data = data.json()['results']