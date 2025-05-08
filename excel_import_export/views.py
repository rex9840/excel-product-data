from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes,parser_classes
from rest_framework.generics import ListCreateAPIView
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.views import Response, status
from rest_framework.parsers import MultiPartParser, FormParser 

from excel_import_export.serializers import ProductItemSerializer, UploadSerializer

from . import resources
from . import models
from . import utils


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


@swagger_auto_schema(
    method="post",
    description="import excel",
    response=status.HTTP_200_OK,
    request_body=UploadSerializer,
    permission_classes=[permissions.AllowAny],
) 
@api_view(["POST"]) 
@permission_classes([permissions.AllowAny]) 
@parser_classes([MultiPartParser, FormParser]) 
def import_excel(request): 
    serializer = UploadSerializer(data=request.data) 
    serializer.is_valid(raise_exception=True) 
    serializer.save()
    file_path = serializer.data["file_path"]
    utils.serialize_and_save_json(file_path)  
    return Response(
         status =status.HTTP_201_CREATED,
    )


class ProductItemView(ListCreateAPIView): 
    serializer_class = ProductItemSerializer
    queryset = models.ProductItem.objects.all()
    
    
