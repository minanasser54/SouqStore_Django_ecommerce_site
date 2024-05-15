from django.db import models

# Create your models here.
class Brand(models.Model):
    brand_name=models.CharField(blank=True, max_length=100)
    brand_desc=models.TextField(blank=True)
    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return str(self.brand_name)

class Variant(models.Model):
    var_name=models.CharField(blank=True, max_length=100)
    var_desc=models.TextField(blank=True)
    class Meta:
        verbose_name = 'Variant'
        verbose_name_plural = 'Variants'

    def __str__(self):
        return str(self.var_name)
