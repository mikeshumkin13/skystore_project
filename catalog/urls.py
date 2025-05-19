from django.urls import path
from .views import HomePageView, ProductDetailView, AddProductView, ContactsView, ThankYouView

app_name = "catalog"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("add-product/", AddProductView.as_view(), name="add_product"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("thank-you/", ThankYouView.as_view(), name="thank_you"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
]

