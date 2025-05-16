from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Chest, Skin

from rest_framework.response import Response
from rest_framework.decorators import api_view


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



def userLogin(request):

    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            if not request.POST.get('rememberMe'):
                request.session.set_expiry(0)
            else:
                request.session.set_expiry(999999999)
            return redirect('/')
    else:
        form = AuthenticationForm()
    
    context = {
        'form': form
    }

    return render(request, 'app/login.html', context)


def userLogout(request):
    logout(request)
    return redirect('/')


@api_view(['GET'])
def chestOpening(request, chestID):
    chest = Chest.objects.get(id = chestID)
    skins = Skin.objects.filter(chestID = chestID)

    context = {
        'chest': chest,
        'skins': skins
    }
    return Response(context)