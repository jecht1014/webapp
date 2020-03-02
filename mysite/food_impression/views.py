from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import FoodFormAdd

def index(request):
    latest_food_list = Food.objects.order_by('-pub_date')[:5]
    context = {'latest_food_list': latest_food_list}
    return render(request, 'food_impression/index.html', context)

def detail(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    return render(request, 'food_impression/detail.html', {'food': food})

def add(request):
    if (request.method == 'POST'):
        obj = Food()
        info = FoodFormAdd(request.POST, instance = obj)
        info.save()
        return redirect(to='/food_impression')
    
    return render(request, 'food_impression/add.html', {'form':FoodFormAdd()})
