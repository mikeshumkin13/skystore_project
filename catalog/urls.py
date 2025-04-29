from django.urls import path
from catalog import views  # Импортируем файл с контроллерами (views)

urlpatterns = [
    path('', views.home, name='home'),            # Главная страница
    path('contacts/', views.contacts, name='contacts'), # Страница контактов
    path('thank-you/', views.thank_you),
]
