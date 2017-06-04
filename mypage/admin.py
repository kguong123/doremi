# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import RecipeScrap, HoneyTipScrap
# Register your models here.


class RecipeScrapAdmin(admin.ModelAdmin):
    list_display = ('slug', 'user')


class HoneyTipScrapAdmin(admin.ModelAdmin):
    list_display = ('slug', 'user')


admin.site.register(RecipeScrap, RecipeScrapAdmin)
admin.site.register(HoneyTipScrap, HoneyTipScrapAdmin)