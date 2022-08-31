from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login1,name='login1'),
    path('loginuser',views.loginuser,name='loginuser'),
    path('logout',views.logoutuser,name='logout'),
    path('register',views.register,name='register'),
    path('registeruser',views.registeruser,name='registeruser'),
    path('book_slots',views.bookslots,name='book slots'),
    path('book_slots/<slug:sport_id>',views.courts,name='courts'),
    path('slots/<slug:court_id>',views.slotbook,name='slotbook'),
    path('book_slot/<slug:slot_id>',views.bookslot,name='book slot'),
    path('confirm/<slug:slot_id>',views.confirm,name='confirm'),
    path('view_slots',views.bookedslots,name='my slots'),
    path('profile',views.profile,name='profile')

]