from django.views.generic import TemplateView, View
from django.shortcuts import redirect
from django.http import HttpRequest


class ContactsView(View):
    template_name = "catalog/contacts.html"

    def get(self, request: HttpRequest):
        return self.render()

    def post(self, request: HttpRequest):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"Новое сообщение:\nИмя: {name}\nТелефон: {phone}\nСообщение: {message}")
        return redirect("catalog:thank_you")

    def render(self):
        from django.shortcuts import render
        return render(self.request, self.template_name)


class ThankYouView(TemplateView):
    template_name = "catalog/thank_you.html"

