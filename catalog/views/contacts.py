from django.shortcuts import render, redirect


def contacts(request):
    """Контроллер для страницы контактов"""
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        print(f"Новое сообщение:\nИмя: {name}\nТелефон: {phone}\nСообщение: {message}")
        return redirect("catalog:thank_you")

    return render(request, "catalog/contacts.html")


def thank_you(request):
    """Страница благодарности"""
    return render(request, "catalog/thank_you.html")

