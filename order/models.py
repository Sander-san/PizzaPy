from django.db import models
from django.contrib.auth.models import User
from menu.models import FoodObject


class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    food = models.ManyToManyField(FoodObject, related_name='orders', blank=True)

    def __str__(self):
        return f'{self.user} basket'



