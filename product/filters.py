import django_filters
from . models import Product, Category


class ProductFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Product
        fields = ['ProCtegory', 'ProBrand', 'ProPrice', 'ProDiscountPrice']


# class CategoryFilter(django_filters.FilterSet):
#     # name = django_filters.CharFilter(lookup_expr='iexact')

#     class Meta:
#         model = Category
#         fields = ['price', 'release_date']