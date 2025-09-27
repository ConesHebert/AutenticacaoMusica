from django.contrib.messages import constants
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages, auth
import musicas

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('/musicas/list_musicas')
    status = request.GET.get('status')
    return render(request, 'register.html', {'status': status})

def login(request):
    if request.user.is_authenticated:
        return redirect('/musicas/list_musicas')
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def validate_register(request):
   name = request.POST.get('name')
   email = request.POST.get('email')
   password = request.POST.get('password')
   
   if len(name.strip()) == 0 or len(email.strip()) == 0 or len(password) == 0 :
    messages.add_message(request, constants.ERROR, "Name, e-mail or password can't be empty!")
    return redirect('/auth/register')

   if len(password) < 8 :
     messages.add_message(request, constants.ERROR, 'The password need to have at least 8 characters.')
     return redirect('/auth/register')

   if User.objects.filter(email=email).exists():
    messages.add_message(request, constants.ERROR, 'This e-mail is already registered')
    return redirect('/auth/register')

    try:
      usuario = User.objects.create_user(username=name,email=email,password=password)
      usuario.save()
      messages.add_message(request, constants.SUCCESS, 'Your account was created!')
      return redirect('/auth/register')  
    except:
        messages.add_message(request, constants.ERROR, 'System error')
        return redirect('/auth/register') 

def validate_login(request):
  email = request.POST.get('email')
  password = request.POST.get('password')
  username = User.objects.get(email=email).username
  user = auth.authenticate(username=username, password=password)


  if not user:
     messages.add_message(request, constants.WARNING, 'E-mail or password is incorrect')
     return redirect ('/auth/login/')
  else:
     auth.login(request,user)
     return redirect('/musicas/list_musicas')
  
def exit(request):
   auth.logout(request)
   messages.add_message(request, constants.WARNING, 'login before entering!')
   return redirect('/auth/login/')

