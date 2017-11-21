from django.db import models


class Manufacturer(models.Model):
    code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.URLField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, related_name='products')

    def __str__(self):
        return self.name
