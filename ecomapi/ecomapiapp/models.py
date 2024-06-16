from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    originalprice = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_id = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.product.name
    
class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)
    def __str__(self):
        return self.order_id