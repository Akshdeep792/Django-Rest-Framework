from django.shortcuts import render
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer
# Create your views here.

# echo get data
# def api_home(request, *args, **kwargs ):
#     body = request.body #byte string of JSON data
#     print(body)
#     data = {}
#     try:
#         data = json.loads(body) # string of json data  --> python dictionary
#     except:
#         pass
#     # print(data)
#     data['params'] = dict(request.GET)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     return JsonResponse(data)

# @api_view(["GET"])
# def api_home(request, *args, **kwargs):

#     '''
#         drf api view
#     '''
#     instance = Product.objects.all().order_by("?").first()
#     # print(instance)
#     data = {}
#     if instance:
#         # data['id'] = model_data.id
#         # data['title'] = model_data.title
#         # data['content']=  model_data.content
#         # data['price'] = model_data.price

#         # data = model_to_dict(model_data , fields = ['id', 'title', 'sale_price', 'price'])
#         data = ProductSerializer(instance).data
#         # model instance (model_data)
#         # turn a Python dict
#         # return JSON to my_client
#     return Response(data)


@api_view(["POST"])
def api_home(request, *args, **kwargs):

    data = request.data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # verify the requirements

        # instance = serializer.save()
        # print(data)
        data = serializer.data
        return Response(data)
    return Response({"invalid" : "Not a valid data"})