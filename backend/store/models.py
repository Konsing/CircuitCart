from django.db import models

# store/models.py
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_featured = models.BooleanField(default=False)
    is_combo = models.BooleanField(default=False)

    def __str__(self):
        return self.title
