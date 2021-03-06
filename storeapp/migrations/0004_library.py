# Generated by Django 3.2.2 on 2021-09-17 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0003_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('books', models.ManyToManyField(to='storeapp.Books')),
            ],
            options={
                'ordering': ['created_at'],
                'abstract': False,
            },
        ),
    ]
