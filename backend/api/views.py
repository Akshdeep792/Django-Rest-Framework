from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.

# echo get data
def api_home(request, *args, **kwargs ):
    body = request.body #byte string of JSON data
    print(body)
    data = {}
    try:
        data = json.loads(body) # string of json data  --> python dictionary
    except:
        pass
    # print(data)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)
