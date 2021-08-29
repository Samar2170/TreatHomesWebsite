from django.db import models
from django.contrib.auth.models import User 



# Create your models here.
class Customer(models.Model):
    cust_id=models.PositiveIntegerField()
    customer=models.OneToOneField(User, on_delete=models.PROTECT)
    address=models.CharField(max_length=500)
    contact=models.CharField(max_length=13)

    def __str__(self):
        return self.customer.username

class Product(models.Model):
    sku=models.CharField(max_length=20)
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='media/product',null=True, blank=True)

    def __str__(self):
        return self.name


class Wishlist(models.Model):
    customer=models.OneToOneField(Customer, on_delete=models.CASCADE)
    products=models.ManyToManyField(Product)

    def __str__(self):
        return self.customer.customer.username