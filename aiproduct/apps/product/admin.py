from django.contrib import admin
from .models import Product, ProductClick, UserUtmParameter, Category


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', 'category', 'url', 'image_url']
    list_filter = ['category', 'created_at', 'updated_at']


class ProductClickAdmin(admin.ModelAdmin):
    search_fields = ['click_source', 'product']
    list_filter = ['created_at', 'updated_at']


class UserUtmParameterAdmin(admin.ModelAdmin):
    search_fields = ['utm_campaign', 'utm_content', 'utm_medium', 'utm_source']


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductClick, ProductClickAdmin)
admin.site.register(UserUtmParameter, UserUtmParameterAdmin)
admin.site.register(Category, CategoryAdmin)
