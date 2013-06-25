from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('form_ajax.views',
    url(r'^contact/$', 'contact', name='contact'),
    url(r'^success/$', 'success', name='success'),
)