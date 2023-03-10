from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'login.html')

# Registering
def create(request):
    # add create element
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    confirm_pw = request.POST['confirm_pw']

    return redirect('/user/registered')

def register(request):
    return render(request, 'registered.html')

# Logging in
def login(request):
    # read login and validate with existing data
    email = request.POST['email']
    password = request.POST['password']
    return redirect('/trips')
# testing
# testing comment