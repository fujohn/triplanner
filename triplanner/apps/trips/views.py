from django.shortcuts import render, redirect

# Create your views here.
# dashboard
def index(request):
    return render(request, 'list.html')

# amending trip
def amend(request):
    return render(request, 'form.html')

def create(request):
    # add create element
    destination = request.POST['destination']
    transportation = request.POST['transportation']
    description = request.POST['description']
    organizer = request.POST['organizer']
    
    return redirect('/trips')

def edit(request):
    # add update element
    destination = request.POST['destination']
    transportation = request.POST['transportation']
    description = request.POST['description']
    organizer = request.POST['organizer']
    
    return redirect('/trips')

def remove(request):
    # delete trip
    return redirect('/trips')

# view trip
def access(request):
    # view trip
    return render(request, 'details.html')