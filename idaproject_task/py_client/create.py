import requests


headers = {}
data = {
    'bank_name': 'bank_py_client',
    'term_min': 10,
    'term_max': 30,
    'rate_min': 1.8,
    'rate_max': 9.8,
    'payment_min': 1000000,
    'payment_max': 10000000,
}

endpoint = 'http://localhost:8000/api/offers/'

get_response = requests.post(endpoint, json=data, headers=headers)


print(get_response.json())