from django import forms
from order.models import OrderDelivery, OrderTakeAway, Restaurant


class OrderDeliveryForm(forms.Form):
    address = forms.CharField()
    payment = forms.ChoiceField(choices=OrderDelivery.PAYMENT_CHOICE)

    class Meta:
        model = OrderDelivery
        fields = ('address', 'payment',)


class OrderTakeAwayForm(forms.Form):
    restaurants = Restaurant.objects.all()
    RESTAURANT_CHOICE = []
    for i in restaurants:
        RESTAURANT_CHOICE += (i.pk, i.address),
    print(RESTAURANT_CHOICE)
    restaurant = forms.ChoiceField(choices=RESTAURANT_CHOICE)
    payment = forms.ChoiceField(choices=OrderTakeAway.PAYMENT_CHOICE)

    class Meta:
        model = OrderTakeAway
        fields = ('restaurant', 'payment',)
