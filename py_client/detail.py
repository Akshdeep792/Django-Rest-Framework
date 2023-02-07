import requests


# HTTP request -> HTML
# REST API HTTP request --> JSON
endpoint = "http://localhost:8000/api/products/1/"


# get_request = requests.get(endpoint,params={"abc": 123}, json={"query": "Hello World"}) # api --> method
get_response = requests.get(endpoint) # api --> method

# print(get_response.text)
print(get_response.json())
