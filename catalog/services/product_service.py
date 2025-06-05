from catalog.models import Product, Category
from django.shortcuts import get_object_or_404
from django.core.cache import cache


def get_products_by_category(slug: str):
    cache_key = f"category_products_{slug}"
    cached_data = cache.get(cache_key)

    if cached_data:
        return cached_data

    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, is_published=True)

    cache.set(cache_key, (category, products), 300) #5 мин
    return category, products

