from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginAPI),
    path('register/', views.userRegister, name='register'),
    path('logout/', views.userLogout, name='logout'),
    path('chest/<int:chestID>/', views.chestAPI)
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)