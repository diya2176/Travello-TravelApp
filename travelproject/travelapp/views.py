# from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Team


# Create your views here.
def demo(request):
    places = Place.objects.all()
    team = Team.objects.all()
    context = {
        'result': places,
        'res': team,
    }
    return render(request, "index.html", context)


