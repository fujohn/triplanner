from django.shortcuts import render, redirect
from .models import Trip

# Create your views here.
# dashboard
def index(request):
    try:
        del request.session['trip_form']
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
    # add create element
    new_trip = Trip.objects.create(
    destination = request.POST['destination'],
    transportation = request.POST['transportation'],
    description = request.POST['description'],
    organizer = request.POST['organizer']
    )
    
    return redirect('/trips')

# amending trip
def amend(request, trip_id):
    request.session['trip_form'] = 'edit'
    context = {
        'trip': Trip.objects.get(id=trip_id)
        }
    return render(request, 'form.html', context)

def edit(request, trip_id):
    trip_to_update = Trip.objects.get(id=trip_id)
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
    # view trip
    context = {
        'trip': Trip.objects.get(id=trip_id)
    }
    request.session['trip_id'] = trip_id
    return render(request, 'details.html')