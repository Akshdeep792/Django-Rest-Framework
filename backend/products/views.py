from django.shortcuts import render
from rest_framework import authentication ,generics, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from api.authentication import TokenAuthentication
from .models import Product
from api.permissions import IsStaffEditorPermission
from .serializers import ProductSerializer
from api.mixins import StaffEditorPermissionMixix
# Create your views here.

class ProductListCreateAPIView(
    StaffEditorPermissionMixix,
    generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [
    #     authentication.SessionAuthentication,
    #     TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes = [permissions.DjangoModelPermissions]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]




    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(serializer.validated_data)
        email = serializer.validated_data.pop('email')
        # print(email)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        
        if content is None:
            content = title
        serializer.save(content=content)

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(
    StaffEditorPermissionMixix,
    generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    # lookup field = 'pk

product_detail_view = ProductDetailAPIView.as_view()

class ProductUpdateAPIView(
    StaffEditorPermissionMixix,
    generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]


    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


product_update_view = ProductUpdateAPIView.as_view()

class ProductDestroyAPIView(
    StaffEditorPermissionMixix,
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_destroy(self, serializer):
        super().perform_destroy(instance)

product_destroy_view = ProductDestroyAPIView.as_view()


# class ProductListAPIView(generics.ListAPIView):

#     '''
#     not gonna use this method
#     '''
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # lookup field = 'pk

# product_list_view = ProductListAPIView.as_view()

class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin, # take care of lookup field
    generics.GenericAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def get(self,request, *args, **kwargs):
        # print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self,request, *args, **kwargs):
        # print(args, kwargs)
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        
        if content is None:
            content = "This is a single view doing cool stuff"
        serializer.save(content=content)
    # same can be done for post method
product_mixin_view = ProductMixinView.as_view()
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