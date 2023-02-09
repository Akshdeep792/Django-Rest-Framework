from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer
# Create your views here.

class ProductListCreateAPIVoew(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        
        if content is None:
            content = title
        serializer.save(content=content)

product_list_create_view = ProductListCreateAPIVoew.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup field = 'pk

product_detail_view = ProductDetailAPIView.as_view()


# class ProductListAPIView(generics.ListAPIView):

#     '''
#     not gonna use this method
#     '''
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # lookup field = 'pk

# product_list_view = ProductListAPIView.as_view()



# function based views

@api_view(["GET", "POST"])
def product_alt_view(request, pk = None,*args, **kwargs):
    method = request.method # PUT -> update , DESTROY -> delete

    if method == "GET":
        if pk is not None:
            # detail view
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
       
        qs = Product.objects.all()
        data = ProductSerializer(qs, many=True).data
        return Response(data)    

        
    
    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
        
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid" : "Not a valid data"})