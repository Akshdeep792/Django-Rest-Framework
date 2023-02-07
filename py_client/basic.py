import requests


# HTTP request -> HTML
# REST API HTTP request --> JSON
endpoint = "http://localhost:8000/api/"


# get_request = requests.get(endpoint,params={"abc": 123}, json={"query": "Hello World"}) # api --> method
get_request = requests.post(endpoint, json={"title": "Hello World"}) # api --> method

# print(get_request.text)
print(get_request.json())
