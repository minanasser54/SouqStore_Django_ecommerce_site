# Generated by Django 3.0.6 on 2020-05-29 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20200529_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(default='product_img/default.png', upload_to='product_img'),
        ),
    ]
