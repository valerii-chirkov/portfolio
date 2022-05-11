import requests


offer_id = input('What is the offer id you want to delete?\n')

try:
    offer_id = int(offer_id)
except:
    offer_id = None
    print(f'{offer_id} is not allowed')

if offer_id:
    endpoint = f'http://localhost:8000/api/offers/{offer_id}/'
    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code==204)