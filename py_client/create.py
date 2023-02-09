import requests


# HTTP request -> HTML
# REST API HTTP request --> JSON
headers = {'Authorization': 'Bearer 9cd034e3d90a7937b0680b445fcb9c1fa38fcd7c'}

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "this field is done"
}
get_response = requests.post(endpoint, json=data, headers=headers)


print(get_response.json())
