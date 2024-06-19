from django_filters import rest_framework as filters, BaseInFilter, CharFilter
from .models import Product


class ListFilter(BaseInFilter, CharFilter):
    pass


class ProductFilter(filters.FilterSet):
    category = ListFilter(field_name="category", lookup_expr='in')

    class Meta:
        model = Product
        fields = ['category']