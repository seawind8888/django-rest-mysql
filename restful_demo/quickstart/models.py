# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Message(models.Model):
    # key是保留字
    class Meta:
        db_table = 'news'
    title = models.TextField(max_length=20)
    url = models.CharField(max_length=140)

# Create your models here.
