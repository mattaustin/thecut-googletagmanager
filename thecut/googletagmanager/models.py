# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from . import managers, receivers
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Container(models.Model):
    """Google Tag Manager container settings for a site.

    Google Tag Manager containers can be created at:
    https://tagmanager.google.com/

    """

    site = models.OneToOneField('sites.Site', unique=True, related_name='+')

    container_id = models.CharField('Container ID', max_length=25)

    is_enabled = models.BooleanField(
        'enabled', default=False, help_text='Is the Google Tag Manager '
                                            'snippet enabled on the website?')

    objects = managers.ContainerManager()

    class Meta(object):
        ordering = ['site']

    def __str__(self):
        return self.site.name

models.signals.post_save.connect(receivers.clear_cache, sender=Container)
models.signals.post_delete.connect(receivers.clear_cache, sender=Container)
