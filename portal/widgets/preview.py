# -*- encoding: utf-8 -*-

from django import forms

from django.utils import html
from django.utils.safestring import mark_safe

class PreviewWidget(forms.FileInput):
    def __init__(self, attrs={}):
        super(PreviewWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        output = []
        if value and hasattr(value, "url"):
            output.append(('<a target="_blank" href="%s">'
                           '<img class="preview" src="%s" style="height: 100px;" /></a>'
                           % (value.url, value.url)))
        
        output.append(super(PreviewWidget, self).render(name, value, attrs))
        
        return mark_safe(u''.join(output))