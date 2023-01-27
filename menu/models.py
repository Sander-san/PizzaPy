from django.db import models


class FoodCategory(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Food category'
        verbose_name_plural = 'Food categories'


class FoodObject(models.Model):
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/food_img/')
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    regular_size = models.FloatField('Size')
    quantity = models.IntegerField(blank=True, null=True, default='1')

    def __str__(self):
        return f"{self.category} {self.title} - {self.price}"

    class Meta:
        verbose_name = 'Food'
        verbose_name_plural = 'Food'
