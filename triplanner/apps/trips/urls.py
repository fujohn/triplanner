from django.urls import path
from . import views

app_name = 'trips'

urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.amend, name='new'),
    path('create', views.create), # POST
    path('<int:trip_id>/edit', views.amend, name='edit'),
    path('<int:trip_id>/update', views.edit), # PUT
    path('<int:trip_id>/delete', views.remove), # DELETE
    path('<int:trip_id>', views.access)

]
