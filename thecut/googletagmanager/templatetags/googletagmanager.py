# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import template
from thecut.googletagmanager.models import Container


register = template.Library()


@register.inclusion_tag('googletagmanager/_snippet.html', takes_context=True)
def googletagmanager_snippet(context):
    """Google Tag Manager code snippet.

    https://developers.google.com/tag-manager/quickstart

    """

    try:
        container = Container.objects.get_current()
    except Container.DoesNotExist:
        container = False

    return {'container': container, 'request': context.get('request')}
