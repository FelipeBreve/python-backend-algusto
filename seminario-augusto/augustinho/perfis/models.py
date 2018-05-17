# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class profile(models.Model):
	nome = models.CharField(max_length=120)
	endereco = models.CharField(max_length=120, default='#', null=True)
	telefone = models.CharField(max_length=12, default='00 0 0000 0000')

	def __unicode__(self):
		return self.name