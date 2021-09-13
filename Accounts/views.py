from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
from Treasures.models import Treasure
import bcrypt

def landing_page(request):
    return render(request, 'landing_page.html')

def login(request):
    if request.method != "POST":
        return redirect('/')
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect('/dashboard')
    messages.error(request, "Please enter a valid email and password")
    return redirect("/")

def registration(request):
    return render(request, 'registration.html')

def register(request):
    if request.method != "POST":
        return redirect('/')
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/registration')
    hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt(14)).decode()

    new_user = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = hashed_pw
    )

    request.session['user_id'] = new_user.id

    return redirect('/dashboard')

def logout(request):
    request.session.flush()
    return redirect('/')

# Might need to be in the treasure app
def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {
        'this_user': User.objects.get(id = request.session['user_id']),
        'treasure_list': Treasure.objects.all()
    }
    return render(request, 'dashboard.html', context)

def my_account(request):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {
        'this_user': User.objects.get(id = request.session['user_id']),
        'treasure_list': Treasure.objects.all()
    }
    return render(request, 'my_account.html', context)