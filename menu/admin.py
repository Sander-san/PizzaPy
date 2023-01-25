from django.contrib import admin
from menu.models import FoodCategory, FoodObject
from django.utils.html import mark_safe


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    fields = ['title']


@admin.register(FoodObject)
class FoodObjectAdmin(admin.ModelAdmin):
    list_display = ['get_image', 'category', 'title', 'price', 'regular_size']
    fields = ['category', ('image', 'get_image'), 'title', 'description', 'price', 'regular_size']
    list_filter = ('category', 'price', 'regular_size')
    readonly_fields = ['get_image', ]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width=26 height=26')

    get_image.short_description = 'Image'

