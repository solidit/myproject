# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.db import models

from portal.models.arquivo import Arquivo
from portal.widgets.preview import PreviewWidget

class ArquivoAdmin(admin.ModelAdmin):
    title = u'Arquivo'
    
    formfield_overrides = { models.ImageField: { 'widget': PreviewWidget }, }

    list_display = [ 'id', 'logo', ]

    fieldsets = [
        (None, {'fields': [ 'logo', ]}),
    ]

admin.site.register(Arquivo, ArquivoAdmin)