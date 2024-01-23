from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from populars.models import Food
from populars.models import Local

# Create your views here.
def index(request) :
    context = dict()
    today = datetime.today().date()
    food = Food.objects.all()
    local = Local.objects.all()
    context["date"] = today
    context["menus"] = food
    context["locals"] = local
    return render(request, 'populars/home_index.html', context)

def food(request, pk) :
    context = dict()
    food1 = Food.objects.all().get(id = pk)
    context["menu"] = food1
    return render(request, 'populars/food_detail.html', context)

