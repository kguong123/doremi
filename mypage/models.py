# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from recipe.models import Recipe, Foodinfo, Recipeinfo
# Create your models here.s

class RecipeScrap(models.Model):
	slug = models.CharField('slug',max_length=50)
	user = models.CharField('user',max_length=50)



class HoneyTipScrap(models.Model):
	slug = models.CharField('slug',max_length=50)
	user = models.CharField('user',max_length=50)
