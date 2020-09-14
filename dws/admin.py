# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Area, Level

class LevelInline(admin.StackedInline):
    model = Level
    extra = 1

class AreaAdmin(admin.ModelAdmin):
    fields = ['name', 'picnic_table', 'exit_sign']
    inlines = [LevelInline]

admin.site.register(Area, AreaAdmin)