# Generated by Django 3.2 on 2021-10-14 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordinates', '0003_auto_20211010_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinates',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='создано'),
        ),
    ]
