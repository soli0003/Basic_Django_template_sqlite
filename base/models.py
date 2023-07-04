from django.db import models


class Category(models.Model):
    description = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.description


class Product(models.Model):
    desc = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    createdTime = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images', null=True, blank=True)

    def __str__(self):
        return self.desc


