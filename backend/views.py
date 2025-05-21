from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_protect
from django.db import transaction

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Chest, Skin, UserInventory
from .serializers import *

import random


#returns chests in json
@api_view(['GET'])
def getChests(request):
    chests = Chest.objects.all()
    serializer = ChestSerializer(chests, many = True, context = {'request': request})
    return Response(serializer.data)


#returns skins in json
@api_view(['GET'])
def getSkins(request, chest_ID):
    skins = Skin.objects.filter(chestID = chest_ID)
    serializer = SkinSerializer(skins, many = True, context = {'request': request})
    return Response(serializer.data)


#needed to forms validation
@api_view(['GET'])
def getCSRFToken(request):
    return Response({'CSRFToken': get_token(request)})


@csrf_protect
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
        #creates new user
        user = User.objects.create_user(username = username, email = email, password = password)
        UserInventory.objects.create(userID = user)
        logout(request)
        login(request, user)
        return Response()


@csrf_protect
@api_view(['POST'])
def loginAPI(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username = username, password = password)

    #logs in if found user
    if user is not None:
        logout(request)
        login(request, user)
        return Response()
    else:
        return Response({'message': 'Invalid login or password'}, status = 400)


@csrf_protect
@api_view(['POST'])
def logoutAPI(request):
    logout(request)
    return Response()


#returns user name, balance and items in inventorys
@api_view(['GET'])
def userInfo(request):
    if request.user.is_authenticated:
        inventory = UserInventory.objects.get(userID = request.user.id)
        serializer = InventorySerializer(inventory, context = {'request': request})
        
        return Response({
            'username': request.user.username,
            'balance': serializer.data.get('balance'),
            'items': serializer.data.get('items')
        })
    else:
        return Response(status = 401)
    

@csrf_protect
@api_view(['POST'])
def buyChest(request):
    chestID = request.data.get('chestID');
    try:
        chest = Chest.objects.get(id = chestID)
    except Chest.DoesNotExist:
        return Response({'message': 'Chest does not exists!'})  

    #select for update locks inventory during transaction
    inventory = UserInventory.objects.select_for_update().get(userID = request.user.id)

    if inventory.balance < chest.price:
        return Response({'message': "You don't have enough money to buy that chest!"})
    
    skins = Skin.objects.filter(chestID = chestID)
    wonSkin = random.choice(list(skins))

    #using sql transaction to ensure payment will be made
    with transaction.atomic():
        inventory.balance -= chest.price

        haveItem = False
        for item in inventory.items:
            if wonSkin.id == item['skinID']:
                item['count'] += 1
                haveItem = True
                break
        
        if not haveItem:
            inventory.items.append({'skinID': wonSkin.id, 'count': 1})
        
        inventory.save()
    
    return Response({
        'wonSkin': SkinSerializer(wonSkin, context = {'request': request}).data
    })