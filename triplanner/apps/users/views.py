from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User

# Create your views here.
def index(request):
    try:
        del request.session['name']
        del request.session['user_id']
    except:
        pass
    return render(request, 'login.html')

# Registering
def create(request):
    # add create element
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='registration')
        return redirect('/')
    else:
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
        name = request.POST['name'],
        email = request.POST['email'],
        password_hash = pw_hash
        )
        request.session['name'] = new_user.name
        request.session['user_id'] = new_user.id

        return redirect('/user/registered')


def register(request):
    print(request.session['name'])
    print(request.session['user_id'])
    return render(request, 'registered.html')

# Logging in
def login(request):
    # read login and validate with existing data
    user = User.objects.filter(email=request.POST['email'])
    print(user)
    if user:
        print('User found')
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password_hash.encode()):
            print('PW matched')
            request.session['user_id'] = logged_user.id
            request.session['name'] = logged_user.name
            return redirect('/trips')
        else:
            print('PW not match')
            messages.error(request, 'Invalid password for account', extra_tags='login')
            return redirect('/')
    else:
        print('No User found')
        messages.error(request, 'There is no account to this email', extra_tags='login')
        return redirect('/')