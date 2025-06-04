from django.views import View
from django.shortcuts import render
from catalog.services.product_service import get_products_by_category
from django.views.generic import ListView
from catalog.models import Category


class ProductsByCategoryView(View):
    template_name = "catalog/category_products.html"

    def get(self, request, slug):
        category, products = get_products_by_category(slug)
        context = {
            "category": category,
            "products": products,
        }
        return render(request, self.template_name, context)




class CategoryListView(ListView):
    model = Category
    template_name = "catalog/category_list.html"
    context_object_name = "categories"


