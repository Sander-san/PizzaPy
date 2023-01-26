from django.contrib import admin
from order.models import Basket, Restaurant, OrderDelivery, OrderTakeAway


admin.site.register(Basket)
admin.site.register(Restaurant)
admin.site.register(OrderDelivery)
admin.site.register(OrderTakeAway)
