from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login1,name='login1'),
    path('loginuser',views.loginuser,name='loginuser'),
    path('logout',views.logoutuser,name='logout'),

]