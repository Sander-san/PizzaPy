from django.urls import path
from order.views import basket, add_to_basket, remove_from_basket


urlpatterns = [
    path('basket/', basket, name='basket'),
    path('add_to_basket/<int:element_pk>', add_to_basket, name='add_to_basket'),
    path('remove_from_basket/', remove_from_basket, name='remove_from_basket'),
]
