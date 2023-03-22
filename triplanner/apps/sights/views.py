from django.shortcuts import render, redirect
from .models import Sight
from django.contrib import messages
from ..users.models import User
from ..trips.models import Trip
from django.http import HttpResponse

# Create your views here.
# create trip
def new(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request, 'sight_form.html')

def create(request):
    errors = Sight.objects.sight_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/sights/new')
    else:
    # add create element
        creator = User.objects.get(id=int(request.session['user_id']))
        trip = Trip.objects.get(id=int(request.session['trip_id']))
        new_sight = Sight.objects.create(
        name = request.POST['name'],
        day = int(request.POST['day']),
        order = int(request.POST['order']),
        duration = int(request.POST['duration']),
        description = request.POST['description'],
        creator = creator,
        trip = trip
        )
        
        return redirect(f'/trips/{trip.id}')

# update trip
def amend(request, sight_id):
    if 'user_id' not in request.session:
        return redirect('/')
    sight = Sight.objects.get(id=sight_id)
    if request.session['user_id'] != sight.creator.id:
        return redirect(f'/trips/{sight.trip.id}')
    request.session['edit_sight'] = str(sight_id)
    context = {
        'sight':sight
    }
    return render(request, 'sight_form.html', context)

def edit(request, sight_id):
    errors = Sight.objects.sight_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/sights/{sight_id}/edit')
    else:
        sight_to_update = Sight.objects.get(id=sight_id)
        # add update element
        sight_to_update.name = request.POST['name']
        sight_to_update.day = request.POST['day']
        sight_to_update.order = request.POST['order']
        sight_to_update.duration = request.POST['duration']
        sight_to_update.description = request.POST['description']
        sight_to_update.save()
    
    return redirect(f'/trips/{sight_to_update.trip.id}')

def remove(request, sight_id):
    sight_to_delete = Sight.objects.get(id=sight_id)
    return_id = sight_to_delete.trip.id
    # delete trip
    sight_to_delete.delete()
    return redirect(f'/trips/{return_id}')
