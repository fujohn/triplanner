from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user/create', views.create), # POST
    path('user/registered', views.register),
    path('user/login', views.login) # POST

]
