# Generated by Django 2.2.7 on 2019-12-18 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_id',
            field=models.IntegerField(default=1),
        ),
    ]