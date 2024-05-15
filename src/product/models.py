from django.db import models
from django.utils.text import slugify
from django.urls import reverse
import datetime
# Create your models here.
class Product(models.Model):
    name = models.CharField(blank=True, max_length=100)
    category=models.ForeignKey('Category',on_delete=models.CASCADE,blank=True,null=True)
    slug = models.SlugField(blank=True,null=True)
    brand=models.ForeignKey('settings.Brand',on_delete=models.CASCADE,blank=True,null=True)
    description = models.TextField(blank=True)
    img= models.ImageField(upload_to="product_img",blank=True,null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount= models.DecimalField(max_digits=6, decimal_places=2)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(blank=True, default=datetime.datetime.now)
    new = models.BooleanField(default=True)
    bestseller = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('main:product_detail',kwargs={'slug':self.slug})
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'



    def save(self,*args,**kwargs):
        if not self.slug :
            self.slug=slugify(self.name)
        super(Product,self).save(*args,**kwargs)
    def __str__(self):
        return str(self.name)



class ProductImage(models.Model):
    image_product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_img= models.ImageField(upload_to="product_img")
    class Meta:
        verbose_name = 'ProductImage'
        verbose_name_plural = 'ProductImages'

    def __str__(self):
        return str(self.image_product)

class Category(models.Model):
    cat_name= models.CharField(blank=True, max_length=100)
    cat_parent=models.ForeignKey('self',blank=True,null=True,limit_choices_to={'cat_parent__isnull':True},on_delete=models.CASCADE)
    cat_description = models.TextField(blank=True)
    cat_img = models.ImageField(upload_to="category_img")
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return str(self.cat_name)

class Alternative(models.Model):
    alt_product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="main_product")
    alts= models.ManyToManyField(Product,related_name="alternative_products")

    class Meta:
        verbose_name = 'Alternative'
        verbose_name_plural = 'Alternatives'

    def __str__(self):
        return str(self.alt_product)

class Accessories(models.Model):
    acc_product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="master_product")
    accessories=models.ManyToManyField(Product,related_name="accessories_products")
    class Meta:
        verbose_name = 'Accessories'
        verbose_name_plural = 'Accessoriess'

    def __str__(self):
        return str(self.acc_product)
