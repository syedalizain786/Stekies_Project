from venv import logger
from django.core.exceptions import ValidationError
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User
from user.serializers import UserSerializer
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from user.user_update_serializer import UserUpdateSerializer


@permission_classes([IsAuthenticated])
class User_View(APIView):
    def get(self,request,id=None):
        print(f"Received GET request with id={id}")
        try:
            if id:
                user = User.objects.get(id=id)
                serializer = UserSerializer(user)
                data = serializer.data
                data.pop('password', None)
                return Response(data, status=status.HTTP_200_OK)
            else:
                users = User.objects.all()
                paginator = PageNumberPagination()
                paginator.page_size = 20
                paginated_queryset = paginator.paginate_queryset(users, request)
                serializer = UserSerializer(paginated_queryset, many=True)
                return paginator.get_paginated_response(serializer.data)
        except User.DoesNotExist:
            print("Hellloo")
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Server Error: {str(e)}")
            return Response({'error': 'Server error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class User_Create_View(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if User.objects.filter(email=request.data.get('email')).exists():
            return Response({'error': 'User with this email already registered'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            try:
                serializer.save()
                return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return Response({'error': e.message_dict}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class User_Updation_View(APIView):
    permission_classes = [AllowAny]
    def patch(self,request,id):
        try:
            user = User.objects.get(pk=id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    

        serializer = UserUpdateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            except ValidationError as e:
                return Response({'error': e.message_dict}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = User.objects.get(email=email)
            print(user)
            if check_password(password, user.password):
                print("Password Checked")
                refresh = RefreshToken.for_user(user)
                return Response({
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
            
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(f"Exception: {str(e)}")
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
   
    

