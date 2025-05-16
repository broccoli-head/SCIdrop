from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import chestOpening

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.userLogin, name='login'),
    path('register/', views.userRegister, name='register'),
    path('logout/', views.userLogout, name='logout'),
    path('chest/<int:chestID>', chestOpening)
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)