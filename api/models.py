from django.contrib.auth.models import AbstractUser
from django.db import models


class ApiUser(AbstractUser):
    user_type_choices = (
                        (1, 'Поставщик'),
                        (2, 'Потребитель'),
    )
    user_type = models.IntegerField()

    def __str__(self):
        try:
            user_type_display = dict(self.user_type_choices).get(self.user_type, "Неизвестный тип пользователя")
            return f"ID: {self.id}, " \
                   f"Имя пользователя: {self.username}, " \
                   f"Тип пользователя: {user_type_display}, " \
                   f"email: {self.email} "
        except IndexError:
            return f"ID: {self.id}, " \
                   f"Имя пользователя: {self.username}, " \
                   f"Тип пользователя: Ошибка в типе пользователя (user_type={self.user_type}), " \
                   f"email: {self.email} "


class Stock(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"ID склада: {self.id}. " \
            f"Название склада: {self.name} "


class Product(models.Model):
    name = models.CharField(max_length=256)
    quantity = models.IntegerField()
    owner = models.ForeignKey(ApiUser,
                              related_name='products',
                              on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock,
                              related_name='products',
                              on_delete=models.CASCADE)

    def __str__(self):
        return f"ID товара - {self.id}. " \
            f"Наименование: {self.name}. " \
            f"Количество: {self.quantity}. " \
            f"Владелец: {self.owner.id}. " \
            f"Склад: {self.stock}"


class Business(models.Model):
    user = models.ForeignKey(ApiUser,
                             related_name="business_actions",
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name="business_actions",
                                on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def __str__(self):
        return f"Пользователь: {self.user.username}, " \
               f"Товар: {self.product.name}, " \
               f"Количество: {self.quantity}"
