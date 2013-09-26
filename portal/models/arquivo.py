from django.db import models

# Create your models here.

class Arquivo(models.Model):
    logo = models.ImageField(upload_to='logo')

    class Meta:
        app_label = 'portal'
        ordering = [ 'logo', ]
        db_table = 'arquivo'
        verbose_name = u'Arquivo'
        verbose_name_plural = u'Arquivos'
