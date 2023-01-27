from django.shortcuts import render, redirect
from menu.models import FoodObject
from order.models import Basket, OrderDelivery, OrderTakeAway, Restaurant
from django.contrib.auth.decorators import login_required
from order.forms import OrderDeliveryForm, OrderTakeAwayForm


@login_required(login_url='/signup/')
def add_to_basket(request, element_pk):
    delivery = OrderDelivery.objects.filter(user=request.user).filter(expired=False)
    take_away = OrderTakeAway.objects.filter(user=request.user).filter(expired=False)
    if delivery or take_away:
        return redirect('basket')
    element = FoodObject.objects.filter(id=element_pk)
    user_basket = Basket.objects.filter(user=request.user).first()
    if user_basket:
        user_basket.food.add(element.first())
    else:
        new_basket = Basket(user=request.user)
        new_basket.save()
        new_basket.food.add(element.first())
    return redirect('basket')


@login_required(login_url='/signup/')
def basket(request):
    delivery = OrderDelivery.objects.filter(user=request.user).filter(expired=False)
    take_away = OrderTakeAway.objects.filter(user=request.user).filter(expired=False)
    if delivery or take_away:
        return redirect('order_status')
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
    if user_basket:
        items = Basket.objects.get(user=request.user).food.all()
        prices = Basket.objects.get(user=request.user).food.all()
        total_price = 0
        for i in prices:
            total_price += i.price

        form = OrderTakeAwayForm()
        if request.method == 'POST':
            form = OrderTakeAwayForm(request.POST)
            if form.is_valid():
                restaurant = Restaurant.objects.filter(pk=form.data['restaurant'])
                user_order = OrderTakeAway.objects.create(
                    user=request.user,
                    restaurant=restaurant.first(),
                    basket=user_basket,
                    payment=form.data['payment'],
                )
                user_order.save()
                return order_status(request)
        context = {
            'user_basket': user_basket,
            'form': form,
            'items': items,
            'total_price': total_price,
        }
        return render(request, 'take_away.html', context)
    else:
        return render(request, 'sorry.html')


@login_required(login_url='/signup/')
def delivery(request):
    user_basket = Basket.objects.filter(user=request.user).first()
    if user_basket:
        items = Basket.objects.get(user=request.user).food.all()
        prices = Basket.objects.get(user=request.user).food.all()
        total_price = 0
        delivery_price = 4
        for i in prices:
            total_price += i.price
        if total_price < 20:
            total_price += delivery_price

        form = OrderDeliveryForm()
        if request.method == 'POST':
            form = OrderDeliveryForm(request.POST)
            if form.is_valid():
                user_order = OrderDelivery.objects.create(
                    user=request.user,
                    address=form.data['address'],
                    basket=user_basket,
                    payment=form.data['payment'],
                )
                user_order.save()
                return order_status(request)
        context = {
            'user_basket': user_basket,
            'form': form,
            'items': items,
            'delivery_price': delivery_price,
            'total_price': total_price,
        }
        return render(request, 'delivery.html', context)
    else:
        return render(request, 'sorry.html')


@login_required(login_url='/signup/')
def order_status(request):
    delivery = OrderDelivery.objects.filter(user=request.user).filter(expired=False).first()
    take_away = OrderTakeAway.objects.filter(user=request.user).filter(expired=False).first()
    if delivery or take_away:
        ready_take_away = OrderTakeAway.objects.filter(user=request.user).filter(expired=False).filter(
            status='Order complete').first()
        ready_delivery = OrderDelivery.objects.filter(user=request.user).filter(expired=False).filter(
            status='Courier delivered the order').first()
        context = {
            'delivery': delivery,
            'take_away': take_away,
            'ready_take_away': ready_take_away,
            'ready_delivery': ready_delivery,
        }
        return render(request, 'user_order_status.html', context)
    else:
        return redirect('basket')


@login_required(login_url='/signup/')
def admin_orders_panel(request):
    orders_delivery = OrderDelivery.objects.filter(expired=False)
    orders_take_way = OrderTakeAway.objects.filter(expired=False)
    context = {
        'orders_delivery': orders_delivery,
        'orders_take_way': orders_take_way,
    }
    return render(request, 'admin_order_panel.html', context)


@login_required(login_url='/signup/')
def change_order_status(request, order_pk):
    orders_delivery = OrderDelivery.objects.filter(pk=order_pk).first()
    orders_take_way = OrderTakeAway.objects.filter(pk=order_pk).first()
    if orders_delivery:
        orders_delivery.update_status()
    else:
        orders_take_way.update_status()
    return redirect('admin_orders_panel')


@login_required(login_url='/signup/')
def received_order(request):
    user_basket = Basket.objects.filter(user=request.user).first()
    if user_basket:
        user_order1 = OrderTakeAway.objects.filter(user=request.user).first()
        user_order2 = OrderDelivery.objects.filter(user=request.user).first()
        if user_order1:
            user_order1.delete()
            user_basket.delete()
        elif user_order2:
            user_order2.delete()
            user_basket.delete()
        return render(request, 'thanks.html')
    else:
        return render(request, 'sorry.html')

