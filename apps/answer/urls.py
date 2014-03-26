from django.conf.urls import patterns, url

urlpatterns = patterns('apps.answer.views',
    url(r'^answers/$', 'answers_list'),
    url(r'^answers/(?P<pk>[0-9]+)/$', 'answers_detail'),
)