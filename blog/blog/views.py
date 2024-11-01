from django.http import HttpResponse
import datetime

def hello_world(request):
    return HttpResponse('Hello_World, Givaldo')

def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html><body>It is now %s.</body></html>' % now
    return HttpResponse(html)
