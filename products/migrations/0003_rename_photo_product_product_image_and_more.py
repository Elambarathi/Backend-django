# Generated by Django 4.2.16 on 2024-09-09 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_name_alter_seller_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='photo',
            new_name='product_image',
        ),
        migrations.AddField(
            model_name='product',
            name='warranty_period',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='seller',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='seller',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='sellers/'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
    ]
