# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import apps


class AppConfig(apps.AppConfig):

    label = 'googletagmanager'

    name = 'thecut.googletagmanager'

    verbose_name = 'Google Tag Manager'
