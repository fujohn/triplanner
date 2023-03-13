from django.shortcuts import render, redirect

# Create your views here.
# amending trip
def amend(request):
    return render(request, 'form.html')

def create(request):
    # add create element
    sight = request.POST['sight']
    day = request.POST['day']
    order = request.POST['order']
    duration = request.POST['duration']
    description = request.POST['description']
    
    return redirect('/trips/__')

def edit(request):
    # add update element
    sight = request.POST['sight']
    day = request.POST['day']
    order = request.POST['order']
    duration = request.POST['duration']
    description = request.POST['description']
    
    return redirect('/trips/__')

def remove(request):
    # delete trip
    return redirect('/trips/___')
