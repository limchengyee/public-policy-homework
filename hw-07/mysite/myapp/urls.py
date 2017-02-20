from django.conf.urls import url
from . import views
#import from this apps, i want views

app_name = ' myapp '
urlpatterns = [
    url(r'^$', views.index , name= 'index'),
    url(r'^farewell/$', views.farewell , name= 'farewell'),
    url(r'^table/$', views.table , name= 'table'),
    url(r'^greet/(?P<who>[A-Za-z\- ]+)/$', views.index , name= 'index'),
    url(r'^add/(?P<n1>[0-9]+)/(?P<n2>[0-9])/$', views.add , name= 'add'),
    url(r'^csv/$', views.csv , name= 'csv'),


]

#views.index is a function we wrote
#
