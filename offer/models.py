# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Class offer
class Offer(models.Model):
    customer = models.ForeignKey('auth.User')
    # product
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

def publish(self):
        self.published_date = timezone.now()
        self.save()

def __str__(self):
        return self.title
    
