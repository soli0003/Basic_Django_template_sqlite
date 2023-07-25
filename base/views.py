from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import ProductSerializer,CategorySerializer, MyTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView



# ---------------------------------------------------------------------------- login and register  -----------------------------------------------------------------------------------------#

# register
@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')

    # Check if the username already exists
    if User.objects.filter(username=username).exists():
        return Response({"message": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

    # Create a new user
    user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
    return Response("new user born")





 
 #login
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# ---------------------------------------------------------------------------- method to check IsAuthenticated works correct -----------------------------------------------------------------------------------------#
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(req):
    return Response("hello")


class products_view(APIView):
    # permission_classes = [IsAuthenticated]
    
    def get(self, request, category=None):  # Add 'category' parameter with a default value of None to recieve spesific category 
        if category:
            return self.get_products_by_category(request, category)
        else:
            my_model = Product.objects.all()
            serializer = ProductSerializer(my_model, many=True)
            return Response(serializer.data)

    def post(self, request, category=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(category=category)  # Set the category field
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk):
        my_model = Product.objects.get(pk=pk)
        serializer = ProductSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        my_model = Product.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_products_by_category(self, request, category):
        my_model = Product.objects.filter(category=category)
        serializer = ProductSerializer(my_model, many=True)
        return Response(serializer.data)
