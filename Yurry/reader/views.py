from django.http import HttpResponse
from django.template  import Context, loader
import datetime
import requests
import json

def hello_reader(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def what_time_is_it(request):
    template = loader.get_template('time.html')
    current_time = datetime.datetime.now()
    context = Context({'current_time' : current_time })
    return HttpResponse(template.render(context))

def group_home(request):
    # call facebook group feed
    GROUP_ID='352245738171385'
    ACCESS_TOKEN='CAACEdEose0cBADBCeCL3N8a3iwjeVb5E9QMRAxV55rZAoT7FzPHAlxMYCrWZAUatXcMKgRhZCGYibY1Tn2ZCqS15EG94xCeZAXP3o0QoWHuoe7I4toRsNnNI5Rpe7HdmxsP5IwGhTSkJqMH91kR1tVJAjW7HssyTq20PWSnkByq5OaukNg5taktipJ76Yk6h24kf8WoH0BwZDZD'
    feed = inqury_group_feed(GROUP_ID,ACCESS_TOKEN) 
    # send the json feed result to template thru context
    context = Context({'f':feed['data']})
    template = loader.get_template("group_home.html")
    # rendering
    return HttpResponse(template.render(context))
#http://jhproject.tistory.com/37

def inqury_group_feed(group_id,access_token):
    url = 'https://graph.facebook.com/' + group_id +'/feed?access_token='+access_token
    r = requests.get(url)
    j = r.json()
    return j
    
    
