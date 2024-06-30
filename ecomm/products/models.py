from django.db import models
from base.models import BaseModel


class Catagory(BaseModel):
    catagory_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    catagory_image = models.ImageField(upload_to='catagories')


class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, related_name='products')
    price = models.IntegerField()
    product_desciption = models.TextField()


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product')