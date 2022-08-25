from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product

User = get_user_model()

class Cart(models.Model):
    user = models.ForeignKey(User, related_name='cart', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return f'{self.user}\'s Cart'

    class Meta:
        verbose_name_plural = 'Cart'