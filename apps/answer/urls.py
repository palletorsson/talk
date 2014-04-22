from django.conf.urls import patterns, url

urlpatterns = patterns('apps.answer.views',
    url(r'^answers/$', 'answers_list'),
    url(r'^answers/learning/tranform$', 'make_sentence', name='make_sentence'),
)
