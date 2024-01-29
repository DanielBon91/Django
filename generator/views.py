from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def author(request):
    return render(request, 'generator/author.html')

def password(request):
    characters = list("abcdefghijklmnopqrstuvwxyz")

    if request.GET.get('uppercase'):
        characters.extend(list(map(str.upper, characters)))
    if request.GET.get('special'):
        characters.extend(list('!@#$^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list(map(str, range(11))))

    length = int(request.GET.get('length', 14))
    thepassword = ''

    for _ in range(length):
        thepassword +=random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})
