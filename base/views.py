from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
from .forms import RoomFrom
# Create your views here.


# rooms=[
#     {'id': 1, 'name': 'C'},
#     {'id': 2, 'name': 'Java'},
#     {'id': 3, 'name': 'Python'}
# ]


def home(request):
    rooms = Room.objects.all()
    print(rooms)
    context = {'rooms':rooms}
    return render(request, 'base/home.html',context)

def room(request,pk):
    room = Room.objects.get(pk=pk)
    context = {'room':room}
    return render(request, 'base/room.html',context)


def createRoom(request):
    form = RoomFrom()
    context = {'form':form}
    return render(request, 'base/room_form.html', context)