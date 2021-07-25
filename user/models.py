from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    CATEGORY_CHOICES = {
        (True,'Student'),
        (False,'Teacher')
    }

    email = models.EmailField('Email',unique=True)
    image = models.ImageField("Image",upload_to='profile_images',null=True, default='profile.jpg')
    phone = models.CharField('Phone',unique=True, max_length=127)
    fullname = models.CharField('FullName',null=True, max_length=127)
    category = models.BooleanField('Category',choices=CATEGORY_CHOICES,default=True)

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = ['']