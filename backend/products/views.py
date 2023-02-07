from django.shortcuts import render
from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer
# Create your views here.

class ProductCreateAPIVoew(generics.CreateAPIView):
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

product_create_view = ProductCreateAPIVoew.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup field = 'pk

product_detail_view = ProductDetailAPIView.as_view()