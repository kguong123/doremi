# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Recipe, Foodinfo, Recipeinfo

# Register your models here.
class FoodInline(admin.TabularInline):
    model = Foodinfo
    extra = 1

class RecipeInline(admin.StackedInline):
    model = Recipeinfo
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeInline, FoodInline]
    list_display = ('title', 'foodname')


admin.site.register(Recipe, RecipeAdmin)
