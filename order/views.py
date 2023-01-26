from django.shortcuts import render, redirect
from menu.models import FoodObject
from order.models import Basket


def add_to_basket(request, element_pk):
    element = FoodObject.objects.filter(id=element_pk)
    if request.method == 'GET':
        user_basket = Basket.objects.filter(user=request.user).first()
        if user_basket:
            pass
        context = {
            'element': element,
        }
        return render(request, 'basket.html', context)
    else:
        return redirect('index')


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


def remove_from_basket(request):
    return redirect('basket')
