from django.shortcuts import render
from menu.models import FoodObject
from order.models import Restaurant


def index(request):
    pizza = FoodObject.objects.filter(category__title='pizza').order_by('price')
    cake = FoodObject.objects.filter(category__title='cake').order_by('-price')
    drink = FoodObject.objects.filter(category__title='drink')
    context = {
        'pizza': pizza,
        'cake': cake,
        'drink': drink,
    }
    return render(request, 'menu.html', context)


def delivery_info(request):
    restaurant = Restaurant.objects.all()
    context = {
        'restaurant': restaurant,
    }
    return render(request, 'delivery_info.html', context)


def sorry(request):
    return render(request, 'sorry.html')
