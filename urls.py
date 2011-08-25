from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

from taskmanager import views

urlpatterns = patterns('',
    url(r'^/?$', views.index, name="taskmanager_index"),
    url(r'^admin/', include(admin.site.urls)),
)
