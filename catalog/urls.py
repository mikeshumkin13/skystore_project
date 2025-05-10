from django.urls import path
from .views.home import home, add_product
from .views.product import product_detail
from .views.contacts import contacts, thank_you

app_name = "catalog"

urlpatterns = [
    path("", home, name="home"),
    path("add-product/", add_product, name="add_product"),
    path("contacts/", contacts, name="contacts"),
    path("thank-you/", thank_you, name="thank_you"),
    path("product/<int:pk>/", product_detail, name="product_detail"),

