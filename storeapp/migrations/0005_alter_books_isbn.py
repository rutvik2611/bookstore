# Generated by Django 3.2.2 on 2021-09-17 19:52

from django.db import migrations, models
import storeapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0004_library'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='isbn',
            field=models.CharField(help_text='Enter 13 digit ISBN Number', max_length=13, unique=True, validators=[storeapp.models.nameFiledValidator], verbose_name='ISBN'),
        ),
    ]
