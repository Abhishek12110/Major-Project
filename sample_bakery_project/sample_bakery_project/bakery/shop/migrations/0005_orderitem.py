# Generated by Django 4.0.1 on 2022-04-17 11:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=50)),
                ('product', models.CharField(max_length=2000)),
                ('price', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('date', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]
