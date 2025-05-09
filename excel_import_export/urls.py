from django.urls import path, include
from . import views


urlpatterns = [
    path(
        "product/",
        include(
            [
                path("export", views.export_excel, name="export-product-excel"),
                path("import", views.import_excel, name="import-product-excel"),
                path("", views.ProductItemView.as_view(), name="list-create-product"),
            ],
        ),
        name="product",
    ),
    path(
        "logs/",
        include(
            [
                path("", views.LogView.as_view(), name="log-list"),
                path("latest/stats", views.import_stats, name="log-import-stats"),
            ],
        ),
        name="log",
    ),
]
