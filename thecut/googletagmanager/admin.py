# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .forms import ContainerForm
from .models import Container
from django.contrib import admin


class ContainerAdmin(admin.ModelAdmin):

    fields = ['site', 'container_id', 'is_enabled']

    form = ContainerForm

    list_display = ['site', 'container_id', 'is_enabled']


admin.site.register(Container, ContainerAdmin)
