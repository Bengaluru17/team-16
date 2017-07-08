# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
  name = models.ForeignKey(User, related_name='student')
  isAdmin = models.BooleanField()
  score = models.IntegerField()
  level = models.IntegerField()
  test1 = models.IntegerField(null=True)
  test2 = models.IntegerField(null=True)
  test3 = models.IntegerField(null=True)
  test4 = models.IntegerField(null=True)
  test5 = models.IntegerField(null=True)
  test6 = models.IntegerField(null=True)
  test7 = models.IntegerField(null=True)
  test8 = models.IntegerField(null=True)
  test9 = models.IntegerField(null=True)
  test10 = models.IntegerField(null=True)
  test = models.IntegerField(null=True)

  def __str__(self):
    return self.name


  