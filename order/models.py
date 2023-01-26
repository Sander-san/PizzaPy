from django.db import models
from django.contrib.auth.models import User
from menu.models import FoodObject


class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    food = models.ManyToManyField(FoodObject, related_name='orders', blank=True)

    def __str__(self):
        return f'{self.user} basket'


class Restaurant(models.Model):
    title = models.CharField(max_length=64, default='PizzaPy')
    address = models.CharField(max_length=256)
    working_hours = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return f'Restaurant №{self.pk} - {self.address}'


class OrderDelivery(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=128, blank=True, null=True)
    basket = models.OneToOneField(Basket, on_delete=models.PROTECT, blank=True, null=True)
    order_time = models.DateTimeField(auto_now_add=True)
    PAYMENT_CHOICE = [
        ('1', 'card'),
        ('2', 'cash')
    ]
    payment = models.CharField(max_length=5, choices=PAYMENT_CHOICE)

    # STATUS_CHOICE = [
    #     ('1', 'in process'),
    #     ('2', 'in preparation'),
    #     ('3', 'ready'),
    # ]

    def __str__(self):
        return f'{self.user} | {self.restaurant} | {self.order_time.strftime("%m/%d/%Y, %H:%M:%S")}'

    class Meta:
        verbose_name = 'Delivery'
        verbose_name_plural = 'Deliveries'


class OrderTakeAway(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    basket = models.OneToOneField(Basket, on_delete=models.PROTECT, blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank=True, null=True)
    order_time = models.DateTimeField(auto_now_add=True)
    PAYMENT_CHOICE = [
        ('1', 'card'),
        ('2', 'cash')
    ]
    payment = models.CharField(max_length=5, choices=PAYMENT_CHOICE)

    # status2 = 'in process/ in preparation/ comes to you/ at place'

    def __str__(self):
        return f'{self.user} | {self.address} | {self.order_time}'

    class Meta:
        verbose_name = 'Take away'
        verbose_name_plural = 'Take away'







