# Generated by Django 4.1.2 on 2023-02-04 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_page_image_alter_page_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes'),
        ),
    ]