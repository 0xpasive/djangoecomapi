# Generated by Django 5.0.6 on 2024-06-16 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapiapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]