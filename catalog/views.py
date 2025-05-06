from django.shortcuts import render, redirect


def home(request):
    """Контроллер для главной страницы"""
    return render(request, template_name="catalog/home.html")


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
