from django.conf.urls import patterns, include, url
from Yurry.views import hello
from reader.views import hello_reader
from reader.views import what_time_is_it
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Yurry.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
   url(r'^hello/$', hello),
   url(r'^reader/$',hello_reader),
   url(r'^time/$',what_time_is_it),
)
