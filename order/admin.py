from django.contrib import admin
from order.models import Basket, Restaurant, OrderDelivery, OrderTakeAway, BasketItem


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'address']
    list_filter = ('title', )


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'created_date']
    list_filter = ('user', )


@admin.register(OrderDelivery)
class OrderDeliveryAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'order_time', 'expired', 'status']
    list_filter = ('user', 'payment', 'expired', 'status')

    def customer(self, obj):
        return self.list_display[0]

    customer.short_description = 'Customer'


@admin.register(OrderTakeAway)
class OrderTakeAwayAdmin(admin.ModelAdmin):
    list_display = ['user', 'restaurant', 'order_time', 'expired', 'status']
    list_filter = ('user', 'payment', 'expired', 'status')


@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    list_display = ['basket', 'product', 'quantity']
    list_filter = ('basket',)
