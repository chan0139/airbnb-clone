#from math import ceil
#from django.shortcuts import redirect, render
#from django.http import HttpResponse
#from django.core.paginator import EmptyPage, Paginator
from django.utils import timezone
from django.views.generic import ListView
from . import models

class HomeView(ListView):
    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context
"""
def all_rooms(request):
    page = request.GET.get("page", 1)
    page = int(page or 1)
    page_size = 10
    limit = page_size*page
    offset = limit-page_size
    rooms = models.Room.objects.all()[offset:limit]
    page_count = ceil(models.Room.objects.count() / page_size)
    return render(request, "rooms/home.html", context={
                                                "potato": rooms,
                                                 "page": page,
                                                 "page_count": page_count,
                                                 "page_range": range(1, page_count+1),
                                                 })
""" # paginator 수동 방법

"""
def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", {"page":rooms})
    except EmptyPage:
        return redirect("/")
    #print(dir(rooms)) paginator func 확인 
""" # paginator 자동 방법


