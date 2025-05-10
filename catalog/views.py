from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category



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


def product_detail(request, pk):
    """Контроллер для страницы одного товара"""
    # Получаем товар по его первичному ключу (pk)
    product = get_object_or_404(Product, pk=pk)

    # Передаём товар в контекст
    context = {
        'product': product
    }

    # Рендерим шаблон product_detail.html с контекстом
    return render(request, 'catalog/product_detail.html', context)

def thank_you(request):
    """Страница благодарности"""
    return render(request, template_name="catalog/thank_you.html")


def add_product(request):
    """Контроллер для добавления нового товара"""
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        category_id = request.POST.get("category")
        image = request.FILES.get("image")

        # Проверим, существует ли категория
        category = get_object_or_404(Category, pk=category_id)

        # Создаём новый товар
        product = Product.objects.create(
            name=name,
            description=description,
            price=price,
            category=category,
            image=image
        )

        # Перенаправляем на страницу товара
        return redirect('catalog:product_detail', pk=product.pk)

    # Передаём категории в контекст для выбора в форме
    categories = Category.objects.all()
    return render(request, 'catalog/add_product.html', {'categories': categories})

