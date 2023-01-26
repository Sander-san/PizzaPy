from django.urls import path
from menu.views import index, sorry, delivery_info


urlpatterns = [
    path('', index, name='index'),
    path('delivery_info/', delivery_info, name='delivery_info'),
    path('sorry/', sorry, name='sorry'),
]
