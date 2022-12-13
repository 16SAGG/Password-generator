from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render
from .models import Password
from django.urls import reverse
import random

def home(request):
    return render(request, 'home.html')

def password(request):
    length = int(request.GET.get('length'))
    upper = request.GET.get('uppercase')
    number = request.GET.get('number')
    special = request.GET.get('special')
    base = request.GET.get('base')

    generated_password = ''

    characters = list('abcdefghijlkmnopqrstuvwxyz')

    if length > 14 or len(base) > 6:
        return render(request, '404.html')
    
    generated_password += base
    length -= len(base)

    if upper:
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    if number:
        characters.extend('1234567890')
    
    if special:
        characters.extend('$#@_¿?!¡')
    
    for x in range(length):
        generated_password += random.choice(characters)

    ctx = {
        'password': generated_password, 
    }

    return render(request, 'password.html', ctx)

def passwordRecord(request):
    passName = request.GET.get('passwordName')
    passContent = request.GET.get('password')
    if passName:
        newPass = Password(name = passName, password = passContent)
        newPass.save()
        messages.success(request, 'Your password has been saved')
    else:
        messages.error(request, "Your password don't have a name")
    return HttpResponseRedirect(reverse('home'))

def showPasswords(request):
    myPasswords = Password.objects.all()
    ctx = {
        'myPasswords': myPasswords,
    }
    return render(request, 'saves.html', ctx)

def deletePasswords(request, id):
    myPassword = Password.objects.get(id = id)
    myPassword.delete()
    return HttpResponseRedirect(reverse('saves'))

def about(request):
    return render(request, 'about.html', {})