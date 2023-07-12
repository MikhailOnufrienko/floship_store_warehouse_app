from django.db import models


class Order(models.Model):
    class Statuses(models.TextChoices):
        CREATED = 'Создан', 'Создан'
        READY_FOR_SHIPMENT = 'Готов к отгрузке', 'Готов к отгрузке'

    class Warehouses(models.TextChoices):
        WAREHOUSE_1 = 'Склад_1', "Склад_1"
        WAREHOUSE_2 = 'Склад_2', 'Склад_2'

    status = models.TextField(
        verbose_name='Статус', choices=Statuses.choices, default=Statuses.CREATED
    )
    warehouse = models.TextField(
        verbose_name='Склад', choices=Warehouses.choices, default=Warehouses.WAREHOUSE_1
    )
    creation_dt = models.DateTimeField(
        verbose_name='Дата и время создания', auto_now_add=True
    )
    payed = models.BooleanField(
        verbose_name='Оплачен', default=False
    )
    
    class Meta:
        db_table = "store\".\"order"
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
    
    def __str__(self):
        return self.id
