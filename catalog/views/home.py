from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from ..models import Product
from ..forms import ProductForm


# def home(request):
#     """Контроллер для главной страницы"""
#     latest_products = Product.objects.order_by('-created_at')[:5]  # последние 5 продуктов
#     return render(request, 'catalog/home.html', {'latest_products': latest_products})


class AddProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/add_product.html"
    success_url = reverse_lazy("catalog:home")
