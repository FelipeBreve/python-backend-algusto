# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Msg(models.Model):
    # ID is implicit, create automatically
    content = models.CharField(max_length=256)
    author = models.CharField(max_length=32)

# Create your models here.
