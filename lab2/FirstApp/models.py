from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(default=0)  # Nowe pole
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
