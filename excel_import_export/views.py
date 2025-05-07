from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.views import status

from . import resources
from . import models


@swagger_auto_schema(
    method="get",
    description="export the product item data into excel",
    response=status.HTTP_200_OK,
    permission_classes=[permissions.AllowAny],
)
@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def export_excel(request):
    queryset = models.ProductItem.objects.all()
    get_resources = resources.ProductItemsResoures()
    data = resources.XLSX()
    response = HttpResponse(
        data.export_data(get_resources.export(queryset=queryset)),
        content_type=data.get_content_type(),
    )
    
    response["Content-Disposition"] = (
        f'attachment; filename="products.xlsx"'
    )
    return response
