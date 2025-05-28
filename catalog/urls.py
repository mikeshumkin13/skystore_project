from django.urls import path
from catalog.views.base import HomePageView
from catalog.views.contacts import ContactsView, ThankYouView
from catalog.product_views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)


app_name = "catalog"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("thank-you/", ThankYouView.as_view(), name="thank_you"),
    # Новый CRUD
    path("products/", ProductListView.as_view(), name="product_list"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path(
        "products/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
]
