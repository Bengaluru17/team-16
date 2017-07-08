# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
  name = models.CharField(max_length=100, unique=True)
  email = models.EmailField(max_length=100, unique=True)
  password = models.CharField(max_length=100, default='qwerty')
  isAdmin = models.BooleanField()
  score = models.IntegerField()
  level = models.IntegerField()
  test1 = models.IntegerField()
  test2 = models.IntegerField()
  test3 = models.IntegerField()
  test4 = models.IntegerField()
  test5 = models.IntegerField()
  test6 = models.IntegerField()
  test7 = models.IntegerField()
  test8 = models.IntegerField()
  test9 = models.IntegerField()
  test10 = models.IntegerField()
  test = models.IntegerField()

  def __str__(self):
    return self.name
  