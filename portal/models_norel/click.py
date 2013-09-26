# -*- encoding: utf-8 -*-

from dynamodb_mapper.model import DynamoDBModel

from datetime import datetime
from django.conf import settings
import pytz

class Click(DynamoDBModel):
    __table__     = u"%s" % settings.DATABASES["default"]["CLICK_TABLE"]
    __hash_key__  = u"page_obj"
    __range_key__ = u"event_id"
    
    __schema__    = { u"page_obj": unicode,
                      u"event_id": datetime,
                      u"user": unicode,
                      u'msg': list,
                      u"param": unicode,
                    }
     
    __defaults__ = {
        u"event_id"   : lambda: datetime.utcnow().replace(tzinfo=pytz.utc),
    }