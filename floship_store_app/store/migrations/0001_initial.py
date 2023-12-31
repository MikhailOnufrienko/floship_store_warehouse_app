# Generated by Django 4.2.3 on 2023-07-12 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunSQL('CREATE SCHEMA IF NOT EXISTS store;'),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField(choices=[('Создан', 'Создан'), ('Готов к отгрузке', 'Готов к отгрузке')], default='Создан', verbose_name='Статус')),
                ('warehouse', models.TextField(choices=[('Склад_1', 'Склад_1'), ('Склад_2', 'Склад_2')], default='Склад_1', verbose_name='Склад')),
                ('creation_dt', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('payed', models.BooleanField(default=False, verbose_name='Оплачен')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'db_table': 'store"."order',
            },
        ),
    ]
