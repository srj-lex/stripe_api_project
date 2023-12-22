from django.db import models


class Item(models.Model):
    name = models.CharField("Название", max_length=200)
    description = models.TextField("Описание", max_length=500)
    price = models.IntegerField("Цена", )
    currency = models.CharField("Валюта", max_length=100, default="usd")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ("name", )

    def __str__(self) -> str:
        return self.name
