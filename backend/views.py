from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Chest, Skin
from .serializers import ChestSerializer


@api_view(['GET'])
def getChests(request):
    chests = Chest.objects.all()
    serializer = ChestSerializer(chests, many = True, context = {'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def getSkins(request, chest_ID):
    skins = Skin.objects.filter(chestID = chest_ID)
    serializer = ChestSerializer(skins, many = True, context = {'request': request})
    return Response(serializer.data)


@api_view(['POST'])
def registerAPI(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if not username:
        return Response({'message': 'Username field is required!'}, status = 400)
    elif not email:
        return Response({'message': 'E-mail field is required!'}, status = 400)
    elif not password:
        return Response({'message': 'Password field is required!'}, status = 400)
    
    elif User.objects.filter(username = username).exists():
        return Response({'message': 'User with that name already exists!'}, status = 400)
    elif User.objects.filter(email = email).exists():
        return Response({'message': 'User with that e-mail already exists!'}, status = 400)
    
    else:
        user = User.objects.create_user(username = username, email = email, password = password)
        login(request, user)
        return Response()


@api_view(['POST'])
def loginAPI(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username = username, password = password)

    if user is not None:
        login(request, user)
        return Response()
    else:
        return Response({'message': 'Invalid login or password'}, status = 400)


@api_view(['POST'])
def logoutAPI(request):
    logout(request)
    return Response()


@api_view(['GET'])
def userInfo(request):
    if request.user.is_authenticated:
        return Response({'username': request.user.username})
    else:
        return Response({'message': 'Not logged'}, status = 401)