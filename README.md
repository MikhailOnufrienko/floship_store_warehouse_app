# Floship Store Warehouse
## Изолированные приложения store и warehouse, общающиеся по API
### Тестовое задание на позицию python developer

1. Клонируйте репозиторий.
2. Создайте виртуальное окружение и установите зависимости из файла requirements.txt.
3. Запустите два docker-контейнера с БД PostgreSQL следующими командами:

```
   docker run --name store_pg -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=pgpass -e POSTGRES_DB=store_db -p 5432:5432 -d postgres:15
```

```
   docker run --name warehouse_pg -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=pgpass -e POSTGRES_DB=warehouse_db -p 5433:5432 -d postgres:15
```

4. Создайте .env-файл из примера .env.example.
5. Примените миграции приложений: из каталога floship_store_app выполните команду

     ```
     python manage.py migrate
     ```
    Ту же команду выполните из каталога floship_warehouse_app.
6. Создайте администраторов для обоих приложений.
   Для этого из каталогов floship_store_app и floship_warehouse_app выполните команду

   ```
     python manage.py createsuperuser
   ```
7. Имена суперпользователей впишите в файл .env.
8. Запустите отладочные сервера приложений.
   Для этого из каталога floship_store_app выполните команду
   
   ```
     python manage.py runserver 127.0.0.1:8001
   ```
   а из каталога floship_warehouse_app команду

   ```
     python manage.py runserver 127.0.0.1:8002
   ```
10. Зайдите на сайт администратора приложения store по адресу:

   ```
   http://127.0.0.1:8001/admin
   ```
11. Зайдите на сайт администратора приложения warehouse по адресу:
    
   ```
   http://127.0.0.1:8002/admin
   ```
11. Создайте в приложении store заказ. Запись с таким же заказом должна появиться в приложении warehouse.
12. Измените автоматически созданный в приложении warehouse заказ (поменяйте значение "Склад" и/или "Статус"). Запись с тем же заказом в приложении store изменится соответствующим образом.
