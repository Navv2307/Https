from django.shortcuts import render

# Create your views here.
import base64
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth import authenticate, login
# from rest_framework.authtoken.models import Token
# from .serializers import LoginSerializer

# class LoginView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             username = serializer.validated_data['username']
#             password = serializer.validated_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 token, created = Token.objects.get_or_create(user=user)
#                 #btoa = lambda x:base64.b64decode(x)
#                 #geoserver_token = base64.b64encode('{}:{}'.format(username, password).encode('utf-8')).decode('ascii')
#                 #geoserver_token =base64.b64decode('{0}:{1}'.format(username, password))
#                 #return Response({'token': token.key, 'geoserver_token': geoserver_token, 'detail': 'User Login successful.'})
#                 return Response({'token': token.key, 'detail': 'User Login successful.'})
#                 # token, created = Token.objects.get_or_create(user=user)
                
#                 # return Response({'token': token.key,'detail': 'User Login successful.'})
#             else:
#                 return Response({'detail': 'Invalid username or password.'}, status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from .serializers import LoginSerializer

class LoginView(APIView):
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                refresh = RefreshToken.for_user(user)
                return Response({'detail': 'Login Successful','refresh': str(refresh), 'access': str(refresh.access_token)})
            else:
                return Response({'detail': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

