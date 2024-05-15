from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from django_countries.fields import CountryField
import datetime
from django.db.models.signals import post_save
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    slug = models.SlugField(blank=True,null=True)
    country =CountryField()
    img = models.ImageField(upload_to="profile_imgs",blank=True,null=True)
    address = models.CharField(blank=True, max_length=100)
    joindate = models.DateTimeField(blank=True, default=datetime.datetime.now)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.user.username)
        super(Profile,self).save(*args,**kwargs)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('accounts:profile_detail',kwargs={'slug':self.slug})

def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile=Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)
