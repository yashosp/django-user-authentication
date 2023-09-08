# from django.shortcuts import render
# from rest_framework.decorators import api_view, permission_classes
# from .serializers import CustomUserSerializer
# from django.contrib.auth import authenticate, login, logout
# from rest_framework.response import Response
# from rest_framework import status, permissions

# # Create your views here.

# @api_view(['POST'])
# @permission_classes([permissions.AllowAny])
# def register_user(request):
#     serializer = CustomUserSerializer(data=request.data)
#     if serializer.is_valid():
#         user = serializer.save()
#         user.set_password(request.data['password'])
#         user.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# @permission_classes([permissions.AllowAny])
# def login_user(request):
#     username = request.data.get('username')
#     password = request.data.get('password')

#     user = authenticate(request, username=user, password=password)

#     if user is not None:
#         login(request, user)
#         return Response({"message":"Login Successful"}, status=status.HTTP_200_OK)
#     else:
#         return Response({"message":"Login Failed"}, status=status.HTTP_401_UNAUTHORIZED)

# @api_view(['POST'])
# def logout_user(request):
#     logout(request)
#     return Response({"message":"Logout Successful"}, status=status.HTTP_200_OK)

from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import CustomUser
from .serializers import CustomUserSerializer

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register_user(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data['password'])
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return Response({"message": "Login Successful"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return Response({"message": "Logout Successful"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Not logged in"}, status=status.HTTP_400_BAD_REQUEST)
