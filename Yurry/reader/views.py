from django.http import HttpResponse
from django.template  import Context, loader
import datetime

def hello_reader(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def what_time_is_it(request):
    template = loader.get_template('time.html')
    current_time = datetime.datetime.now()
    context = Context({'current_time' : current_time })
    return HttpResponse(template.render(context))

#http://jhproject.tistory.com/37
