import os
from django.conf import settings
from django.db import models
from .choice import *

class Post(models.Model):
    nickname = models.CharField(max_length=10, verbose_name='닉네임', null=True)
    country = models.CharField(choices=COUNTRY_CHOICES, max_length=10, verbose_name="나라", null=True)
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    greetings = models.CharField(max_length=40, verbose_name='인삿말', null=True)


    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Boo Post'
        verbose_name = 'Boo Post'
        verbose_name_plural = 'Boo Post'