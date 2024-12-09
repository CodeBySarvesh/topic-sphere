from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


rooms=[
    {'id': 1, 'name': 'C'},
    {'id': 2, 'name': 'Java'},
    {'id': 3, 'name': 'Python'}
]


def home(request):
    context = {'rooms':rooms}
    return render(request, 'base/home.html',context)

def room(request,pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room':room}
    return render(request, 'base/room.html',context)