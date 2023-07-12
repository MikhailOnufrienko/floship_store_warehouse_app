from django.db import models


class Order(models.Model):
    class Statuses(models.TextChoices):
        CREATED = 'Создан', 'Создан'
        READY_FOR_SHIPMENT = 'Готов к отгрузке', 'Готов к отгрузке'

    class Warehouses(models.TextChoices):
        WAREHOUSE_1 = 'Склад_1', "Склад_1"
        WAREHOUSE_2 = 'Склад_2', 'Склад_2'

    id = models.IntegerField(primary_key=True)    
    status = models.TextField(
        verbose_name='Статус', choices=Statuses.choices
    )
    warehouse = models.TextField(
        verbose_name='Склад', choices=Warehouses.choices
    )
    creation_dt = models.DateTimeField(
        verbose_name='Дата и время создания'
    )

    class Meta:
        db_table = "warehouse\".\"order"
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
    
    def __str__(self):
        return self.id
