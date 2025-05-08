from rest_framework import serializers
from openpyxl import workbook

from .models import (
    Brand,
    Color,
    Gender,
    GoogleProdcutCatagory,
    ItemAvailablity,
    ItemCondition,
    ItemGroup,
    Material,
    MaxHandlingTime,
    ProductItem,
    ProductType,
    Pattern,
)
from core.utils import save_temp_file
from django.db import transaction


class UploadSerializer(serializers.Serializer):
    file = serializers.FileField(write_only=True, required=True)
    key = serializers.CharField(read_only=True)
    file_path = serializers.CharField(read_only=True)

    def validate_file(self, value):
        if not value.name.endswith(".xlsx"):
            raise serializers.ValidationError(
                "File must be an Excel file with .xlsx extension"
            )
        return value

    def create(self, validated_data):
        file = validated_data.get("file")
        key = "temp_file_path"
        file_path = save_temp_file(file)
        validated_data["file_path"] = file_path
        validated_data["key"] = key
        return validated_data 
        
class ItemGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemGroup
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = "__all__"


class GoogleProductCatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleProdcutCatagory
        fields = "__all__"


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = "__all__"


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = "__all__"


class PatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pattern
        fields = "__all__"


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"


class MaxHandelingtimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaxHandlingTime
        fields = "__all__"


class ProductItemSerializer(serializers.ModelSerializer):
    item_group_id = ItemGroupSerializer()
    brand = BrandSerializer()
    gender = GenderSerializer()
    google_product_category = GoogleProductCatagorySerializer()
    product_type = ProductTypeSerializer()
    material = MaterialSerializer()
    pattern = PatternSerializer()
    color = ColorSerializer()
    max_handling_time = serializers.CharField()
    is_bundle = serializers.CharField(default="NO")
    condition = serializers.CharField(default=ItemCondition.NEW)
    availability = serializers.CharField(default=ItemAvailablity.OUT_OF_STOCK)

    def validate_availability(self, value):
        try:
            value = value.upper()
            value = ItemAvailablity(value)
            return value
        except ValueError:
            raise serializers.ValidationError(
                f"Invalid value for availability. Must be one of:{dict(ItemAvailablity.choices).keys()}"
            )

    def validate_condition(self, value):
        try:
            value = value.upper()
            value = ItemCondition(value)
            return value
        except ValueError:
            raise serializers.ValidationError(
                f"Invalid value for condition. Must be one of:{dict(ItemCondition.choices).keys()}"
            )

    def validate_is_bundle(self, value):
        value = value.upper()
        if value not in ["YES", "NO"]:
            raise serializers.ValidationError(
                "Invalid value for is_bundle. Must be either 'YES' or 'NO'"
            )
        return value

    @transaction.atomic
    def create(self, validated_data):
        item_group_id = validated_data.pop("item_group_id")
        brand = validated_data.pop("brand")
        gender = validated_data.pop("gender")
        google_product_category = validated_data.pop("google_product_category")
        product_type = validated_data.pop("product_type")
        material = validated_data.pop("material")
        pattern = validated_data.pop("pattern")
        color = validated_data.pop("color")
        max_handling_time = validated_data.pop("max_handling_time")
        validated_data["item_group_id"], _ = ItemGroup.objects.get_or_create(
            **item_group_id
        )
        validated_data["brand"], _ = Brand.objects.get_or_create(**brand)
        validated_data["gender"], _ = Gender.objects.get_or_create(**gender)
        validated_data["google_product_category"], _ = (
            GoogleProdcutCatagory.objects.get_or_create(**google_product_category)
        )
        validated_data["product_type"], _ = ProductType.objects.get_or_create(
            **product_type
        )
        validated_data["material"], _ = Material.objects.get_or_create(**material)
        validated_data["pattern"], _ = Pattern.objects.get_or_create(**pattern)
        validated_data["color"], _ = Color.objects.get_or_create(**color)
        validated_data["max_handling_time"] = MaxHandlingTime.objects.filter(
            pk=max_handling_time
        ).first()
        return super().create(validated_data)

    class Meta:
        model = ProductItem
        fields = "__all__"
