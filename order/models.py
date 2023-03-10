from django.db import models
from django.contrib.auth.models import User
from menu.models import FoodObject


class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.user} basket'


class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(FoodObject, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        res = 0
        for i in self:
            res += i.product.price * i.quantity
        return round(res, 2)

    def __str__(self):
        return f'{self.basket} {self.product} {self.quantity}'


class Restaurant(models.Model):
    title = models.CharField(max_length=64, default='PizzaPy')
    address = models.CharField(max_length=256)
    working_hours = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return f'Restaurant №{self.pk} - {self.address}'


class OrderDelivery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=128, blank=True, null=True)
    basket = models.OneToOneField(Basket, on_delete=models.SET_NULL, blank=True, null=True)
    order_time = models.DateTimeField(auto_now_add=True)
    PAYMENT_CHOICE = [
        ('card', 'card'),
        ('cash', 'cash')
    ]
    payment = models.CharField(max_length=5, choices=PAYMENT_CHOICE)
    expired = models.BooleanField(default=False)
    STATUS_CHOICE = [
        ('Pending', 'Pending'),
        ('In process', 'In process'),
        ('Order complete, waiting for courier', 'Order complete, waiting for courier'),
        ('Courier picked up the order', 'Courier picked up the order'),
        ('Courier delivered the order', 'Courier delivered the order'),
    ]
    status = models.CharField(max_length=64, choices=STATUS_CHOICE, default='Pending', auto_created=True)

    def update_status(self):
        if self.status == self.STATUS_CHOICE[0][1]:
            self.status = self.STATUS_CHOICE[1][1]
            self.save()
        elif self.status == self.STATUS_CHOICE[1][1]:
            self.status = self.STATUS_CHOICE[2][1]
            self.save()
        elif self.status == self.STATUS_CHOICE[2][1]:
            self.status = self.STATUS_CHOICE[3][1]
            self.save()
        elif self.status == self.STATUS_CHOICE[3][1]:
            self.status = self.STATUS_CHOICE[4][1]
            self.save()

    def __str__(self):
        return f'{self.user} | {self.address} | {self.order_time.strftime("%m/%d/%Y %H:%M")}'

    class Meta:
        verbose_name = 'Delivery'
        verbose_name_plural = 'Deliveries'


class OrderTakeAway(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    basket = models.OneToOneField(Basket, on_delete=models.SET_NULL, blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank=True, null=True)
    order_time = models.DateTimeField(auto_now_add=True)
    PAYMENT_CHOICE = [
        ('card', 'card'),
        ('cash', 'cash')
    ]
    payment = models.CharField(max_length=5, choices=PAYMENT_CHOICE)
    expired = models.BooleanField(default=False)
    STATUS_CHOICE = [
        ('Pending', 'Pending'),
        ('In process', 'In process'),
        ('Order complete', 'Order complete'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='Pending', auto_created=True)

    def update_status(self):
        if self.status == self.STATUS_CHOICE[0][1]:
            self.status = self.STATUS_CHOICE[1][1]
            self.save()
        elif self.status == self.STATUS_CHOICE[1][1]:
            self.status = self.STATUS_CHOICE[2][1]
            self.save()

    def __str__(self):
        return f'{self.user} | {self.restaurant} | {self.order_time.strftime("%m/%d/%Y %H:%M")}'

    class Meta:
        verbose_name = 'Take away'
        verbose_name_plural = 'Take away'

