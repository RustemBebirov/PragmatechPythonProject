from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.

class User(AbstractUser):

    email = models.EmailField('Email',unique=True)
    image = models.ImageField("Image 40x40 ",upload_to='profile_images',null=True, default='profile.jpg')
    fullname = models.CharField('FullName', max_length=127)
    


    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.email

    def get_absolute_url(self):
        return reverse('teachers:teachers-single',args=([self.id]))


