# -*- encoding: utf-8 -*-

'''
Created on 18/05/2013

@author: romuloigor
'''

import datetime

from django.conf import settings
from django.core.cache import cache, get_cache
from django.utils.importlib import import_module

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

class MultiLoginRestrictMiddleware(object):
    def process_request(self, request):
        if settings.ENABLE_SIMULTANEOUS_SESSIONS_LOGINS:
            if request.user.is_authenticated():
                cache = get_cache('default')
                cache_timeout = settings.SESSION_TIMEOUT
                cache_key = "user_pk_%s_restrict" % request.user.pk
                cache_value = cache.get(cache_key)
                
                if cache_value is not None:
                    if request.session.session_key != cache_value:
                        engine = import_module(settings.SESSION_ENGINE)
                        session = engine.SessionStore(session_key=cache_value)
                        session.delete()
                        cache.set(cache_key, request.session.session_key, cache_timeout)
                else:
                    cache.set(cache_key, request.session.session_key, cache_timeout)
                    
        return None