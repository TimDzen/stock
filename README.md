# Тестовый проект для создания складов, размещения продуктов на складе поставщиками, выгрузка продуктов со склада потребителями.

Описание:
Проект на Django REST Framework.
Возможности, прописанные в коде:
- Создание пользователя (поля: Username, email, password, Тип пользователя (поставщик/потребитель))
- Создание склада (поля: название)
- Создание продукта поставщиками (поля: название, количество, склад)
- Выбор и отгрузка продуктов со склада потребителями (поля: продукт, количество)

Ограничения:
-  Потребитель не может поставлять товар
- Поставщик не может получать товар
- Потребитель не может получить товара больше, чем имеется на складе
# Сайт проекта на pythonanywhere:

```
DzenTim.pythonanywhere.com
```
## Установка

1. Клонировать репозиторий:
 ```
  git clone https://github.com/stock.git
```
3. Установить зависимости:
```
   pip install -r requirements.txt
```
4. Применить миграции:
```
   python manage.py migrate
```
5. Запустить сервер:
```
   python manage.py runserver
```
6. Открыть браузер и перейти по адресу http://127.0.0.1:8000/

7. ### Как зарегистрировать пользователя
Пройдите по ссылке и введите необходимые данные

```
http://localhost:8000/users/
```
Либо отправить POST запрос с данными
```
{
    "username": "test",
    "email": "test@test.ru ",
    "password": "1234",
    "user_type": 1 or 2 #  на выбор поставщик или потребитель
}
```
8. Создать склад:
```
http://127.0.0.1:8000/stocks/
```
Либо отправить POST запрос с данными
```
{
    "name": "test"  # название склада
 }
```
Так вы получите доступ к функционалу поставщика: 
```
http://localhost:8000/products/

```
Либо отправить POST запрос с данными
```
{
    "name": "test", # название продукта
    "quantity": null, # количество 
    "stock": null # склад
}
```
или потребителя:
```
http://localhost:8000/business/
```
Либо отправить POST запрос с данными
```
{
    "quantity": null, # количество товара
    "product": null # наименование
}
```

