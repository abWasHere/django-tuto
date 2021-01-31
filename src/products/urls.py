from django.urls import path
from products.views import (
    product_create_view,
    product_delete_view,
    product_list_view,
    dynamic_lookup_view,
)

urlpatterns = [
    path("", product_list_view, name="product-list"),
    path("create/", product_create_view, name="product-create"),
    path("<int:id>/", dynamic_lookup_view, name="product-detail"),
    path("<int:id>/delete/", product_delete_view, name="product-delete"),
]
