from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   
   path('', views.homepage, name="homepage"),
   path('signup/', views.signup, name="signup"),
   path('signin/', views.signin, name="signin"),
   path('signout/', views.signout, name="signout"),
   path('checkout/', views.checkout, name='checkout'),
   path('dashboard/', views.dashboard, name='dashboard')
    
  ]