from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField(default=0)
    category = models.CharField(max_length=255)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.name