# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from honeytip.models import HoneyTip, Contents


class ContentsInline(admin.StackedInline):
    model = Contents
    extra = 2


class ContentsAdmin(admin.ModelAdmin):
    inlines = [ContentsInline]
    list_display = ('title', 'owner')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(HoneyTip, ContentsAdmin)


