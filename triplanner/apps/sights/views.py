from django.shortcuts import render, redirect
from .models import Sight

# Create your views here.
# create trip
def new(request):
    try:
        del request.session['sight_form']
    except:
        pass
    return render(request, 'form.html')

def create(request):
    # add create element
    new_sight = Sight.objects.create(
    name = request.POST['name'],
    day = request.POST['day'],
    order = request.POST['order'],
    duration = request.POST['duration'],
    description = request.POST['description'],
    creator = request.POST['creator'], # will need to query it
    trip = request.POST['trip'] # will need to query it
    )
    
    return redirect('/trips/__')

# update trip
def amend(request, sight_id):
    request.session['trip_form'] = 'edit'
    context = {
        'sight':Sight.objects.get(id=sight_id)
    }
    return render(request, 'form.html')

def edit(request, sight_id):
    sight_to_update = Sight.objects.get(id=sight_id)
    # add update element
    sight_to_update.sight = request.POST['sight']
    sight_to_update.day = request.POST['day']
    sight_to_update.order = request.POST['order']
    sight_to_update.duration = request.POST['duration']
    sight_to_update.description = request.POST['description']
    sight_to_update.save()
    
    return redirect('/trips/__')

def remove(request, sight_id):
    sight_to_delete = Sight.objects.get(id=sight_id)
    # delete trip
    sight_to_delete.delete()
    return redirect('/trips/___')
