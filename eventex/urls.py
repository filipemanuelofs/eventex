from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('eventex.core.views',
    url(r'^$', 'homepage', name='homepage'),
    #url(r'^admin/', include(admin.site.urls)),
)
