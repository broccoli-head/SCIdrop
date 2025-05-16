from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Chest
from .serializers import ChestSerializer


def home(request):
    chests = Chest.objects.order_by('-id')[:10]
    context = {
        'chests': chests
    }
    return render(request, 'app/home.html', context)


def userRegister(request):

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


def userLogout(request):
    logout(request)
    return redirect('/')


@api_view(['GET'])
def chestAPI(request, chestID):
    try:
        chest = Chest.objects.get(id = chestID)
    except Chest.DoesNotExist:
        return Response({'error': 'Chest not found'}, status = 404)

    serializer = ChestSerializer(chest, context =  {'request': request})
    return Response(serializer.data)