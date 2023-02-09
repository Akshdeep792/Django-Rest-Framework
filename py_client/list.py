import requests


# HTTP request -> HTML
# REST API HTTP request --> JSON
endpoint = "http://localhost:8000/api/products/"


get_response = requests.get(endpoint)


print(get_response.json())