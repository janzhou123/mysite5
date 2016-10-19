#-*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
import datetime
def hello(request):
    return HttpResponse("Hello World!")

def curr_datetime(request):
    now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    return render_to_response('current_datetime.html', {'current_date': now})



def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise  Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    # html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    # return HttpResponse(html)
    return render_to_response('hours_ahead.html', {'hour_offset': offset, 'next_time': dt})