# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
  name = models.CharField(max_length=100, blank=True, null=True)
  email = models.CharField(max_length=100, blank=True, null=True)
  password = models.CharField(max_length=100, blank=True, null=True)
  isAdmin = models.BooleanField()
  score = models.IntegerField()
  level = models.IntegerField()

  def __str__(self):
    return self.name
  
  