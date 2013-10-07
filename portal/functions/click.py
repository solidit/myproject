# -*- encoding: utf-8 -*-

'''
Created on 09/12/2012

@author: romuloigor
'''

from django.conf import settings
from portal.models_norel.click import Click

def click(page_obj, user, msg, param ):
    if settings.ENABLE_CLICK_TRACKING:
        obj_click = Click()
        obj_click.page_obj = page_obj
        obj_click.user = user
        obj_click.msg = msg
        obj_click.param = u'%s' % param
        return obj_click.save()
    else:
        return False