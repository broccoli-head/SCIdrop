from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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


def registerAPI(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }

    return render(request, 'app/register.html', context)


@api_view(['POST'])
def loginAPI(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username = username, password = password)

    if user is not None:
        login(request, user)
        return Response({'message': 'Logged in successfully', 'username': user.username})
    else:
        return Response({'error': 'Invalid credentials'}, status=400)

    # if request.method == 'POST':
    #     form = AuthenticationForm(data = request.POST)
    #     if form.is_valid():
    #         user = form.get_user()
    #         login(request, user)
            
    #         if not request.POST.get('rememberMe'):
    #             request.session.set_expiry(0)
    #         else:
    #             request.session.set_expiry(999999999)
    #         return redirect('/')
    # else:
    #     form = AuthenticationForm()
    
    # context = {
    #     'form': form
    # }

    # return render(request, 'app/login.html', context)


def logoutAPI(request):
    logout(request)
    return redirect('/')