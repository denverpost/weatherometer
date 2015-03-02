from django.conf.urls.defaults import *

urlpatterns = patterns('charts.views',
   
  (r'^edit/$', 'edit'),
  (r'^edit/(?P<cid>\d+)/$', 'edit'),
  (r'^view/(?P<cid>\d+)/$', 'view'),  
     (r'^$', 'chart')
)     
