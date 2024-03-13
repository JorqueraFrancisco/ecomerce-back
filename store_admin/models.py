from django.db import models
from authentication.models import User
from django.contrib.auth.models import AbstractBaseUser


class Customer(AbstractBaseUser):
    customer_id = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=12)
    email = models.EmailField(max_length=255, blank=False, unique=True)
    password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)

    class Meta:
        db_table = 'Customer'


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.BooleanField(default=True)
    price = models.IntegerField()
    available_quantity = models.IntegerField()

    class Meta:
        db_table = 'Product'


class File(models.Model):
    file_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='files'
    )
    image = models.ImageField(upload_to='images/',)
    file = models.FileField(upload_to='files/',)

    class Meta:
        db_table = 'File'

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'Cart'


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateField()
    total_amount = models.IntegerField()
    status = models.CharField(max_length=50)

    class Meta:
        db_table = 'Order'
