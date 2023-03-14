from django.urls import path
from . import views

app_name = 'sights'

urlpatterns = [
    path('new', views.new, name='new'),
    path('create', views.create), # POST
    path('<int:sight_id>/edit', views.amend, name='edit'),
    path('<int:sight_id>/update', views.edit), # PUT
    path('<int:sight_id>/delete', views.remove), # DELETE

]
