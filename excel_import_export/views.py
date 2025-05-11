from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.serializers import ListSerializer
from rest_framework.views import Response, status
from rest_framework.parsers import MultiPartParser, FormParser

from excel_import_export.serializers import (
    LogSerializer,
    ProductItemSerializer,
    UploadSerializer,
)

from . import resources
from . import models
from . import tasks


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

    response["Content-Disposition"] = f'attachment; filename="products.xlsx"'
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
    tasks.serialize_and_save_json.delay(file_path)
    return Response(
        status=status.HTTP_201_CREATED,
    )


@swagger_auto_schema(
    method="get",
    description="latest-import-stats",
    response=status.HTTP_200_OK,
    permission_classes=[permissions.AllowAny],
)
@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def import_stats(request):
    start_time = models.Log.objects.filter(
            remarks="START_TIME" 
    )
    if not start_time.exists(): 
        return Response(
            {"message": "No import process found."},
            status=status.HTTP_404_NOT_FOUND,
    ) 
    start_time = start_time.first().message 
    process_records = models.Log.objects.filter(
        status=models.LogStatus.INFO, remarks=f"ITEMS_{start_time}"
    ).count() 
    sucess_save = models.Log.objects.filter(
        status=models.LogStatus.SUCCESS,
        remarks=f"ITEMS_{start_time}", 
    ).count()
    waring_records = models.Log.objects.filter(
        status=models.LogStatus.WARNING, remarks=f"WARNING_{start_time}"
    ).count()
    error_records = models.Log.objects.filter(
        status=models.LogStatus.ERROR, remarks=f"ERROR_{start_time}"
    ).count()
    time_taken = (
        models.Log.objects.filter(
            status=models.LogStatus.INFO, remarks=f"TIME_TAKEN_{start_time}"
        )
        .first()
        .message 
    ) 
    end_time = (
        models.Log.objects.filter(
            status=models.LogStatus.INFO, remarks=f"END_TIME_{start_time}"
        )
        .first()
        .message
    )

    data = {
        "start_time": start_time,
        "process_records": process_records,
        "sucess_save": sucess_save,
        "waring_records": waring_records,
        "error_records": error_records,
        "time_taken": time_taken,
        "end_time": end_time,
    }

    return Response(data, status=status.HTTP_200_OK)


class ProductItemView(ListCreateAPIView):
    serializer_class = ProductItemSerializer
    queryset = models.ProductItem.objects.all()


class LogView(ListAPIView):
    serializer_class = LogSerializer
    queryset = models.Log.objects.all()
