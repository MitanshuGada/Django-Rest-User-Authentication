from . import models
from usersApp.serializers import UserSerializer, userLoginSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

# Create your views here.
@api_view(['POST', ])
def register(request):
    if request.method=='POST':
        serializer_class =  UserSerializer(data=request.data)
        data = {}
        
        if serializer_class.is_valid():
            user = serializer_class.save()
            data['response'] = 'Successfully registered a new user'
            data['email'] = user.email
            data['username'] = user.username
            token = Token.objects.get(user=user).key
            data['token'] = token

        else:
            data = serializer_class.errors
        return Response(data)



@api_view(['POST', ])
def login(request):
    if request.method=='POST':
        serializer_class = userLoginSerializer(data=request.data)

        data = {}
        # print(serializer_class)
        # print()
        
        if serializer_class.is_valid():
            new_data = serializer_class.data
            data['response'] = f'Login Successful'
            data['token'] = new_data['token']
            #token = Token.objects.get(user=serializer_class.get_user(request.data)).key
            #data['token'] = token
        else:
            data['error'] = 'Invalid Credentials'
        return Response(data)

