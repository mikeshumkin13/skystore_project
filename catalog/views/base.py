from django.views.generic import ListView, DetailView
from ..models import Product


class HomePageView(ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "latest_products"

    def get_queryset(self):
        return Product.objects.order_by('-created_at')[:5]


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"

