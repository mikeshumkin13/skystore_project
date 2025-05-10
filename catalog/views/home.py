from django.shortcuts import render, redirect
from ..models import Product
from ..forms import ProductForm


def home(request):
    """Контроллер для главной страницы"""
    latest_products = Product.objects.order_by('-created_at')[:5]  # последние 5 продуктов
    return render(request, 'catalog/home.html', {'latest_products': latest_products})


def add_product(request):
    """Контроллер для добавления продукта"""
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("catalog:home")
    else:
        form = ProductForm()

    return render(request, "catalog/add_product.html", {"form": form})

