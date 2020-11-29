# -*- coding: utf-8 -*-

import os
from django.db import models

# Create your models here.

class Guestbook(models.Model):
    nick = models.CharField(max_length=255, verbose_name='Nick')
    content = models.TextField(verbose_name='Content')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'
        
    def __str__(self):              # __unicode__ on Python 2
        return self.nick

    def get_absolute_url(self):
            return u'/%d/' % self.id 
