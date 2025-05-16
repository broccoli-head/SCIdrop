from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginAPI),
    path('register/', views.registerAPI),
    path('logout/', views.logoutAPI),
    path('chests/', views.getChests),
    path('skins/<int:chest_ID>/', views.getSkins),
]