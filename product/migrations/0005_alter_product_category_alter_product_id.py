# Generated by Django 4.2.7 on 2023-12-17 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_product_id_product_id_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('MTW', "MEN'S Topwear"), ('MBW', "MEN'S Bottomwear"), ('MFW', "MEN'S Footwear"), ('MA', 'MEN Accessories'), ('WTW', "WOMEN'S Topwear"), ('WBW', "WOMEN'S Bottomwear"), ('MFW', "WOMEN'S Footwear"), ('SA', 'Saree'), ('WMA', 'WOMEN Accessories'), ('ST', 'Stickers'), ('CL', 'Clocks'), ('SP', 'Showpiece'), ('KS', 'Kitchen storage'), ('CB', 'Cookware & Bakeware'), ('MAKE', 'Makeup'), ('SC', 'Skin Care & Bath'), ('HA', 'Haircare'), ('FR', 'Fragrance'), ('MOB', 'Mobile'), ('SW', 'Smart watch')], max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
