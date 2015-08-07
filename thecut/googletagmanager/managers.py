# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib.sites.models import Site
from django.db.models import Manager


TAGMANAGER_CACHE = {}


class ContainerManager(Manager):

    def get_current(self):
        """Returns the ``Container`` for the current site.

        The ``Container`` object is cached the first time it's
        retrieved from the database.

        """

        site = Site.objects.get_current()
        container = TAGMANAGER_CACHE.get(site.pk, None)
        if container is None:
            container = self.get(site=site)
            TAGMANAGER_CACHE[site.pk] = container
        return container

    def clear_cache(self):
        """Clears the ``Container`` object cache."""

        global TAGMANAGER_CACHE
        TAGMANAGER_CACHE = {}
