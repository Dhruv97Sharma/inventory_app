from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.TextField()

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    number_in_stock = models.IntegerField(default=0)
    description = models.TextField()
    url = models.TextField()
    category = models.ManyToManyField(Category)
    extra_fields = models.JSONField(default=dict)

    def __str__(self):
        return self.name

