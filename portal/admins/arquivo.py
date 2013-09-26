# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.db import models

from portal.models.arquivo import Arquivo
from portal.widgets.preview import PreviewWidget
from portal.functions.click import click
from django.forms.models import model_to_dict

class ArquivoAdmin(admin.ModelAdmin):
    title = u'Arquivo'
    
    formfield_overrides = { models.ImageField: { 'widget': PreviewWidget }, }

    list_display = [ 'id', 'logo', ]

    fieldsets = [
        (None, {'fields': [ 'logo', ]}),
    ]

    def save_model(self, request, obj, form, change):
        click( u"%s" % self.__class__.__name__, user=request.user.username, msg=['action:%s' % change, ], param=model_to_dict(obj) )
        obj.save()

admin.site.register(Arquivo, ArquivoAdmin)