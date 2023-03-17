from django.shortcuts import render, redirect
from django.db.models import Max
from django.contrib import messages
from .models import Trip
from ..users.models import User

# Create your views here.
# dashboard
def index(request):
    try:
        del request.session['edit_trip']
    except:
        pass
    try:
        del request.session['trip_id']
    except:
        pass
    context = {
        'all_trips': Trip.objects.all()
    }
    return render(request, 'list.html', context)

# adding trip
def new(request):
    return render(request, 'form.html')

def create(request):
    errors = Trip.objects.trip_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/trips/new')
    else:
        # add create element
        organizer = User.objects.get(id=int(request.session['user_id']))
        new_trip = Trip.objects.create(
        destination = request.POST['destination'],
        transportation = request.POST['transportation'],
        description = request.POST['description'],
        organizer = organizer
        )
        
        return redirect('/trips')

# amending trip
def amend(request, trip_id):
    request.session['edit_trip'] = str(trip_id)
    context = {
        'trip': Trip.objects.get(id=trip_id),
        'choices': {'car': 'Car',
                    'public': 'Public Transportation',
                    'walk': 'Walking'}
        }
    return render(request, 'form.html', context)

def edit(request, trip_id):
    trip_to_update = Trip.objects.get(id=trip_id)
    
    errors = Trip.objects.trip_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/trips/{trip_id}/edit')
    else:
    # add update element
        trip_to_update.destination = request.POST['destination']
        trip_to_update.transportation = request.POST['transportation']
        trip_to_update.description = request.POST['description']
        trip_to_update.save()
    
        return redirect('/trips')

def remove(request, trip_id):
    # delete trip
    trip_to_delete = Trip.objects.get(id=trip_id)
    trip_to_delete.delete()
    return redirect('/trips')

# view trip
def access(request, trip_id):
    try:
        del request.session['edit_sight']
    except:
        pass
    trip = Trip.objects.get(id=trip_id)
    # needed format for a for loop [[day,[events]],...]
    ordered_sights = []

    for day in range(1,(trip.sights.aggregate(Max('day')))['day__max'] + 1):
        sights_for_day = trip.sights.filter(day=day).order_by('order')
        ordered_sights.append([day, sights_for_day])

    # view trip
    context = {
        'trip': trip,
        'ordered_sights':ordered_sights
    }
    request.session['trip_id'] = trip_id
    return render(request, 'details.html', context)