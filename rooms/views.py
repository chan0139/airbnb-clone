from django.shortcuts import render
from django.http import HttpResponse
from . import models

def all_rooms(request):
    rooms = models.Room.objects.all()
    return render(request, "rooms/home.html", context={"potato": all_rooms})
