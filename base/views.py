from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        form = RoomFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'base/room_form.html', context)