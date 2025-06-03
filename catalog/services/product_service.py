from catalog.models import Product, Category
from django.shortcuts import get_object_or_404

def get_products_by_category(slug: str):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, is_active=True)
    return category, products


