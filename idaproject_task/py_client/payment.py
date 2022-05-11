import requests


headers = {}
endpoint = 'http://localhost:8000/api/offers/?price=10000&deposit=100&term=10'
get_response = requests.get(endpoint, headers=headers)

print(get_response.json())