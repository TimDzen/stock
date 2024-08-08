Тестовый проект для создания складов, размещения продуктов на складе поставщиками, выгрузка продуктов со склада потребителями.
Проект на Django REST Framework. Возможности, прописанные в коде:

 •Создание пользователя (поля: Username, email, password, Тип пользователя (поставщик/потребитель))
 •Создание склада (поля: название)
 •Создание продукта поставщиками (поля: название, количество, склад)
 •Выбор и отгрузка продуктов со склада потребителями (поля: продукт, количество)
Ограничения:
 • Потребитель не может поставлять товар
 • Поставщик не может получать товар
 • Потребитель не может получить товара больше, чем имеется на складе
