# -*- encoding: utf-8 -*-

'''
Created on 18/05/2013

@author: romuloigor
'''

import datetime

from django.conf import settings
from django.contrib.auth import logout
from django.contrib import messages

class SessionExpiredMiddleware:
    def process_request(self, request):
        if settings.ENABLE_SESSIONS_TIMEOUT:
            if request.user.is_authenticated():
                current_datetime = datetime.datetime.now()
                
                if request.session.has_key('last_activity') and (current_datetime - request.session['last_activity']).seconds > settings.SESSION_TIMEOUT:
                    messages.add_message(request, messages.ERROR, 'Apos um periodo sem atividade sua sessão foi encerrada!' )
                    logout(request)
                else:
                    request.session['last_activity'] = current_datetime
                
        return None