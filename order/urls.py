from django.urls import path
from order.views import basket, add_to_basket, remove_from_basket, delivery, take_away, order_status, \
    change_order_status, admin_orders_panel, received_order, expand_quantity, reduce_quantity, \
    admin_order_detail


urlpatterns = [
    path('basket/', basket, name='basket'),
    path('add_to_basket/<int:element_pk>', add_to_basket, name='add_to_basket'),
    path('remove_from_basket/', remove_from_basket, name='remove_from_basket'),
    path('delivery/', delivery, name='delivery'),
    path('take_away/', take_away, name='take_away'),
    path('order_status/', order_status, name='order_status'),
    path('change_order_status/<int:order_pk>', change_order_status, name='change_order_status'),
    path('admin_orders_panel/', admin_orders_panel, name='admin_orders_panel'),
    path('received_order/', received_order, name='received_order'),
    path('expand_quantity/<int:element_pk>', expand_quantity, name='expand_quantity'),
    path('reduce_quantity/<int:element_pk>', reduce_quantity, name='reduce_quantity'),
    path('admin_order_detail/<int:user_pk>', admin_order_detail, name='admin_order_detail'),
]
