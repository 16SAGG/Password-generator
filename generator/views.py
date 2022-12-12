from django.shortcuts import render
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