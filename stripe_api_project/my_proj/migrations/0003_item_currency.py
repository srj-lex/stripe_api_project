# Generated by Django 3.2.16 on 2023-12-21 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_proj', '0002_alter_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='currency',
            field=models.CharField(default='usd', max_length=100, verbose_name='Валюта'),
        ),
    ]
