# Generated by Django 4.1.5 on 2023-01-27 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conditiont_swap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cond', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.TextField(max_length=700)),
                ('deliv', models.TextField(max_length=700)),
                ('pay', models.TextField(max_length=700)),
                ('data', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Swap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField(max_length=300)),
                ('cond_swap_goods', models.TextField(max_length=700)),
                ('cond_swap_money', models.TextField(max_length=700)),
            ],
        ),
    ]