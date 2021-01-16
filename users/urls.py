from django.urls import path
from django.shortcuts import redirect
from .views import CreateUser, ListUsers, UserLogout

app_name = 'users'

urlpatterns = [
    path('create/', CreateUser.as_view(), name='create'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('list/', ListUsers.as_view(), name='list'),
]

