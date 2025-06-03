from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .models import User
from .forms import UserRegisterForm


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        response = super().form_valid(form)
        user_email = form.cleaned_data.get("email")

        # Отправка приветственного письма
        send_mail(
            subject="Добро пожаловать в Skystore!",
            message="Спасибо за регистрацию!",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user_email],
            fail_silently=True,
        )
        return response


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "users/profile.html"
