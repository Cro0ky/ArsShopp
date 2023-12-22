from django.db import models

# Create your models here.


class Products(models.Model):
    title = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
