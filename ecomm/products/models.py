from django.db import models
from base.models import BaseModel
from django.utils.text import slugify


class Catagory(BaseModel):
    catagory_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    catagory_image = models.ImageField(upload_to='catagories')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.catagory_name)
        super(Catagory, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.catagory_name


class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, related_name='products')
    price = models.IntegerField()
    product_desciption = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.product_name

class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product')