from django.contrib.messages import constants
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth

# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        favGenre = request.POST.get('favGenre')
        Genre = request.POST.get('genre')
        
        if User.objects.filter(email=email).exists():
            return HttpResponse('This e-mail is already registered on the platform')
    
        if User.objects.filter(username=username).exists():
            return HttpResponse('This username is already taken')
        
        try:
         user = User.objects.create_user(username=username, email=email, password=password)
         user.save()
         messages.add_message(request, constants.SUCCESS, 'Your account is created!')
         return redirect('/auth/register')  

        except:
            messages.add_message(request, constants.WARNING, 'System error!')
            return redirect('/auth/register')







def login(request):
    return render(request, 'login.html')