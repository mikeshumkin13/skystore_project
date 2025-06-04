from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product
from .forms import ProductForm
from django.core.exceptions import PermissionDenied

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from django.views import View
from django.shortcuts import render
from catalog.services.product_service import get_products_by_category



class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "products"

@method_decorator(cache_page(60 * 5), name="dispatch")
class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"



class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != request.user:
            raise PermissionDenied("Вы не являетесь владельцем этого продукта.")
        return super().dispatch(request, *args, **kwargs)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        # Владелец или пользователь с правом can_unpublish_product
        if obj.owner != request.user and not request.user.has_perm("catalog.can_unpublish_product"):
            raise PermissionDenied("Удалять может только владелец или модератор.")
        return super().dispatch(request, *args, **kwargs)





