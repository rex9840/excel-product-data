from django.urls import path, include
from . import views


urlpatterns = [
    path("prodcut/export", views.export_excel, name="export-product-excel"),
]
