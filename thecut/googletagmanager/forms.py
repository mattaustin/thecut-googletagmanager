# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .models import Container
from django import forms


class ContainerForm(forms.ModelForm):

    class Meta(object):
        fields = ['site', 'container_id', 'is_enabled']
        model = Container

    def __init__(self, *args, **kwargs):
        super(ContainerForm, self).__init__(*args, **kwargs)
        self.fields['container_id'].widget.attrs.update(
            {'placeholder': 'GTM-XXXX'})

    def clean_container_id(self):
        return self.cleaned_data['container_id'].strip()
