# -*- coding: utf-8 -*-

"""
Created on 12/12/2011
@author: romuloigor@solidit.com.br 
"""

from dynamodb_mapper.model import ConnectionBorg
from portal.models_norel.click import Click
from django.conf import settings

def create_dynamoDB():
    conn = ConnectionBorg()
    conn.set_region( '%s' % settings.DATABASES["default"]["REGION"] ) 

    obj_click = Click()
    try:
        conn.create_table(obj_click, read_units=settings.DATABASES["default"]["READ_UNITS"], write_units=settings.DATABASES["default"]["WRITE_UNITS"], wait_for_active=False)
    except Exception, args:
        print args