# Generated by Django 4.2 on 2023-04-24 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Имя')),
                ('gender', models.CharField(max_length=7, verbose_name='Пол')),
                ('date', models.DateTimeField(max_length=10, verbose_name='Дата и время входа')),
                ('online', models.BooleanField(max_length=5, verbose_name='Онлайн')),
            ],
            options={
                'verbose_name': 'Посетитель',
                'verbose_name_plural': 'Посетители',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Название товара')),
                ('price', models.IntegerField(verbose_name='Цена товара')),
                ('date', models.DateTimeField(max_length=19, verbose_name='Дата и время заказа')),
                ('visitorNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.visitors')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
