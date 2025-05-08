from django.db import models


class LogStatus(models.TextChoices):
    ERROR = ("ERROR", "ERROR")
    WARNING = ("WARNING", "WARNING")
    INFO = ("INFO", "INFO")


class ItemAvailablity(models.TextChoices):
    IN_STOCK = ("IN_STOCK", "in_stock")
    OUT_OF_STOCK = ("OUT_OF_STOCK", "out_of_stock")


class ItemCondition(models.TextChoices):
    NEW = ("NEW", "new")
    USED = ("USED", "used")
    REFURBISHED = ("REFURBISHED", "refurbished")


class ItemGroup(models.Model):
    name = models.CharField(null=False, blank=False)
    remarks = models.CharField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


class Brand(models.Model):
    name = models.CharField(null=False, blank=False)
    remarks = models.CharField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


class Gender(models.Model):
    name = models.CharField(null=False, blank=False)
    remarks = models.CharField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Color(models.Model):
    name = models.CharField(null=False, blank=False)
    remarks = models.CharField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Pattern(models.Model):
    name = models.CharField(null=False, blank=False)
    remarks = models.CharField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class GoogleProdcutCatagory(models.Model):
    name = models.CharField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    remarks = models.CharField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


class Material(models.Model):
    name = models.CharField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    remarks = models.CharField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class ProductType(models.Model):
    name = models.CharField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    remarks = models.CharField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class MaxHandlingTime(models.Model):
    start_time = models.CharField(null=False, blank=False)
    end_time = models.CharField(null=False, blank=False)
    remarks = models.CharField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)


class ProductItem(models.Model):
    id = models.CharField(null=False, blank=False,primary_key=True)
    title = models.CharField(max_length=250, null=False, blank=False)
    image_link = models.CharField(max_length=300, null=False, blank=False)
    additional_image_links = models.CharField(max_length=300, null=False, blank=False)
    lifestyle_image_link = models.CharField(max_length=300, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=250, null=False, blank=False)
    price = models.CharField(null=False, blank=False)
    sale_price = models.CharField(null=False, blank=False)
    shipping_cost = models.CharField(null=False, blank=False)
    item_group_id = models.ForeignKey(
        "ItemGroup", related_name="item", on_delete=models.DO_NOTHING
    )
    availability = models.CharField(
        choices=ItemAvailablity.choices, default=ItemAvailablity.OUT_OF_STOCK
    )
    brand = models.ForeignKey("Brand", related_name="item", on_delete=models.CASCADE)
    gtin = models.CharField(max_length=250)
    gender = models.ForeignKey(
        "Gender", related_name="item", on_delete=models.DO_NOTHING
    )
    google_product_category = models.ForeignKey(
        "GoogleProdcutCatagory", related_name="item", on_delete=models.DO_NOTHING
    )
    product_type = models.ForeignKey(
        "ProductType", related_name="item", on_delete=models.DO_NOTHING
    )

    material = models.ForeignKey(
        "Material", related_name="item", on_delete=models.DO_NOTHING
    )

    pattern = models.ForeignKey(
        "Pattern", related_name="item", on_delete=models.DO_NOTHING
    )
    color = models.ForeignKey(
        "Color",
        related_name="item",
        on_delete=models.DO_NOTHING,
    )
    product_length = models.CharField(null=True, blank=True)
    product_width = models.CharField(null=True, blank=True)
    product_height = models.CharField(null=True, blank=True)
    product_weight = models.CharField(null=True, blank=True)
    size = models.CharField(null=True, blank=True)
    max_handling_time = models.ForeignKey(
        "MaxHandlingTime", related_name="item", on_delete=models.DO_NOTHING
    )
    is_bundle = models.CharField(
        choices=[
            ("yes", "yes"),
            ("no", "no"),
        ],
        default="no",
    )
    model = models.CharField(max_length=250)
    condition = models.CharField(
        choices=ItemCondition.choices, default=ItemCondition.NEW
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        ordering = ["-pk"]


class Log(models.Model):
    status = models.CharField(choices=LogStatus.choices, default=LogStatus.INFO)
    message = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.status} {self.created_at} : {self.message}"
