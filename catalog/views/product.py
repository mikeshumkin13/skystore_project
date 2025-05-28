from django.shortcuts import render, get_object_or_404
from ..models import Product


# def product_detail(request, pk):
#     """Контроллер для страницы одного товара"""
#     product = get_object_or_404(Product, pk=pk)
#
#     context = {
#         'product': product
#     }
#     return render(request, 'catalog/product_detail.html', context)
