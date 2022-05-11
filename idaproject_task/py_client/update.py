import requests

endpoint = 'http://localhost:8000/api/offers/2/'
data = {
    'pk': 2,
    "bank_name": "bank_2_updated",
    "term_min": 20,
    "term_max": 40,
    "rate_min": 5.6,
    "rate_max": 12.1,
    "payment_min": 10000,
    "payment_max": 9999999
}
get_response = requests.put(endpoint, json=data)


print(get_response.json())