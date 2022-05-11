import requests


headers = {}
endpoint = 'http://localhost:8000/api/offers/'
get_response = requests.get(endpoint, headers=headers)

print(get_response.json())