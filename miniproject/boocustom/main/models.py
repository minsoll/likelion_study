import os
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .choice import *

class Post(models.Model):
    nickname = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='닉네임')
    country = models.CharField(choices=COUNTRY_CHOICES, max_length=10, verbose_name="나라", blank=True, null=True)
    image = models.ImageField(upload_to='images/',verbose_name='이미지', blank=True, null=True)
    greetings = models.CharField(max_length=40, verbose_name='인삿말', blank=True, null=True)


    def __str__(self):
        return self.nickname

    class Meta:
        db_table = 'Boo Post'
        verbose_name = 'Boo Post'
        verbose_name_plural = 'Boo Post'