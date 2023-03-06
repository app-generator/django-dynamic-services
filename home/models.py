from django.db import models

# Create your models here.

class Product(models.Model):
    id   = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100) 
    info = models.CharField(max_length = 100, default = '')

    def __str__(self):
        return self.name

class Sales(models.Model):
    id      = models.AutoField(primary_key=True)
    product = models.OneToOneField(Product, on_delete=models.DO_NOTHING)
    note    = models.CharField(max_length = 100)

    def __str__(self):
        return str(self.id) + self.product.name
