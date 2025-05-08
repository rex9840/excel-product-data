from import_export import resources
from import_export.fields import Field
from import_export.formats.base_formats import XLSX
from .models import ProductItem


class ProductItemsResoures(resources.ModelResource):
    id = Field(column_name="id", attribute="id")
    title = Field(column_name="title", attribute="title")
    image_link = Field(column_name="image_link", attribute="image_link") 
    additional_image_links = Field(column_name="additional_image_links", attribute="additional_image_links")
    lifestyle_image = Field(column_name="lifestyle_image_link", attribute="lifestyle_image_link")
    description = Field(column_name="description", attribute="description")
    link = Field(column_name="link", attribute="link")
    price = Field(column_name="price", attribute="price")
    sale_price = Field(column_name="sale_price", attribute="sale_price")
    shipping_cost = Field(column_name="shipping_cost", attribute="shipping_cost")
    item_group_id = Field(column_name="item_group_id", attribute="item_group_id")
    availability = Field(column_name="availability", attribute="availability")
    brand = Field(column_name="brand", attribute="brand")
    gtin = Field(column_name="gtin", attribute="gtin")
    gender = Field(column_name="gender", attribute="gender")
    google_product_category = Field(
        column_name="google_product_category", attribute="google_product_category"
    )
    product_type = Field(column_name="product_type", attribute="product_type")
    material = Field(column_name="material", attribute="material")
    pattern = Field(column_name="pattern", attribute="pattern")
    color = Field(column_name="color", attribute="color")
    prodcuct_length = Field(column_name="product_length", attribute="product_length")
    product_width = Field(column_name="product_width", attribute="product_width")
    product_height = Field(column_name="product_height", attribute="product_height")
    prodcut_weight = Field(column_name="product_weight", attribute="product_weight")
    size = Field(column_name="size", attribute="size")
    max_handling_time = Field(
        column_name="max_handling_time", attribute="max_handling_time"
    )
    is_bundle = Field(column_name="is_bundle", attribute="is_bundle")
    model = Field(column_name="model", attribute="model")
    condition = Field(column_name="condition", attribute="condition")
    created_at = Field(column_name="created_at", attribute="created_at")
    updated_at = Field(column_name="updated_at", attribute="updated_at")

    class Meta:
        models = ProductItem
