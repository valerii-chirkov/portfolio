import requests

endpoint = """
    http://localhost:8000/api/offers/?
    rate_min=&
    rate_max=&
    payment_min=10000&
    payment_max=9999999
"""

get_response = requests.get(endpoint)


print(get_response.json())