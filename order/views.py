from django.shortcuts import render, redirect
from menu.models import FoodObject
from order.models import Basket
from django.contrib.auth.decorators import login_required


@login_required(login_url='/signup/')
def add_to_basket(request, element_pk):
    element = FoodObject.objects.filter(id=element_pk)
    user_basket = Basket.objects.filter(user=request.user).first()
    print(element.first())
    if user_basket:
        user_basket.food.add(element.first())
    else:
        new_basket = Basket(user=request.user)
        new_basket.save()
        new_basket.food.add(element.first())
    return redirect('index')


@login_required(login_url='/signup/')
def basket(request):
    user_basket = Basket.objects.filter(user=request.user).first()
    if user_basket:
        items = Basket.objects.get(user=request.user).food.all()
        pos_count = Basket.objects.get(user=request.user).food.all().count()
        prices = Basket.objects.get(user=request.user).food.all()
        total_price = 0
        for i in prices:
            total_price += i.price
        context = {
            'user_basket': user_basket,
            'items': items,
            'pos_count': pos_count,
            'total_price': total_price,
        }
        return render(request, 'basket.html', context)
    context = {
        'user_basket': user_basket,
    }
    return render(request, 'basket.html', context)


@login_required(login_url='/signup/')
def remove_from_basket(request):
    order = Basket.objects.filter(user=request.user).first()
    order.delete()
    return redirect('basket')


@login_required(login_url='/signup/')
def take_away(request):
    user_basket = Basket.objects.filter(user=request.user).first()
    context = {
        'user_basket': user_basket
    }
    return render(request, 'take_away.html', context)


@login_required(login_url='/signup/')
def delivery(request):
    user_basket = Basket.objects.filter(user=request.user).first()
    if user_basket:
        items = Basket.objects.get(user=request.user).food.all()
        context = {
            'user_basket': user_basket,
            'items': items,
        }
        return render(request, 'delivery.html', context)
    context = {
        'user_basket': user_basket
    }
    return render(request, 'delivery.html', context)


