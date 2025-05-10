from django.shortcuts import render, redirect
from .models import Product


def home(request):
    """Контроллер для главной страницы"""
    latest_products = Product.objects.order_by('-created_at')[:5]  # последние 5 продуктов
    return render(request, 'catalog/home.html', {'latest_products': latest_products})




def contacts(request):
    """Контроллер для страницы контактов"""
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        print(f"Новое сообщение:")
        print(f"Имя: {name}")
        print(f"Телефон: {phone}")
        print(f"Сообщение: {message}")

        return redirect("/thank-you/")

    return render(request, template_name="catalog/contacts.html")


def thank_you(request):
    """Страница благодарности"""
    return render(request, template_name="catalog/thank_you.html")
