from django.shortcuts import render
from menu.models import FoodCategory, FoodObject


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

