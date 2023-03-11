from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='login'),
    path('user/create', views.create), # POST
    path('user/registered', views.register, name='registered'),
    path('user/login', views.login) # POST

]
