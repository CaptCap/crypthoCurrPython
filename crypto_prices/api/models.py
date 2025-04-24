from django.db import models

# Create your models here.
class Cryptocurrency(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=10)
    def __str__(self):
        return self.name
