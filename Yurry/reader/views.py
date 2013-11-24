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
    ACCESS_TOKEN='CAACEdEose0cBAISubYFbL8dTGmlQ3jKSN17nKXggS44Bu7onp7dS1UNZC3xhx0GVDcdFZBDsXITiOCsyfMJXHxzSSmUDmukflTlld8J1ZAhoQZBSqRhd9dMvKdlMY12GVflmd75upXaOccUaYutZCnSZBLWuszpReMHGF5lSPjku22Qilyj0w8API48xbYAZBOXStfFBsSYIgZDZD'
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
    
    
