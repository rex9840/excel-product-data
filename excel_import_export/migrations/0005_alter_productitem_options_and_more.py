# Generated by Django 5.2 on 2025-05-08 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excel_import_export', '0004_rename_lifestype_image_link_productitem_lifestyle_image_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productitem',
            options={'ordering': ['-product_id']},
        ),
        migrations.AlterField(
            model_name='productitem',
            name='availability',
            field=models.CharField(choices=[('IN_STOCK', 'in_stock'), ('OUT_OF_STOCK', 'out_of_stock')], default='OUT_OF_STOCK'),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='gtin',
            field=models.CharField(unique=True),
        ),
    ]
