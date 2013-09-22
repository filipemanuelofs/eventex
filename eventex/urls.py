from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'eventex.core.views.homepage',
        name='homepage'),
    url(r'^inscricao/$', 'eventex.subscriptions.views.subscribe',
        name='subscribe'),
    url(r'^inscricao/(\d+)/$', 'eventex.subscriptions.views.detail',
        name='detail'),
)
