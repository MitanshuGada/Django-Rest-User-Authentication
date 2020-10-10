from . import views
from django.urls import path, include

app_name='usersApp'

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login')
]