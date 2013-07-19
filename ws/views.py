# -*- encoding: utf-8 -*-
'''
Created on 19/07/2013
@author: romuloigor@gmail.com
'''

from django.views.decorators.cache import never_cache
from django.http import HttpResponse

def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

@never_cache
def ws(request):

    resultado = []

    for x in range(100):
        resultado.append( "<spam>%s=%s</spam></br>" % (x,fibonacci(x)) )

    return HttpResponse(resultado, content_type="text/html; charset=utf-8")
