from django.conf.urls.defaults import patterns
from django.views.generic import ListView, DetailView
from terminator.models import Glossary, Concept

urlpatterns = patterns('terminator.views',
    (r'^$', 'terminator_index'),
    (r'^glossaries/$', ListView.as_view(
        model=Glossary,
        context_object_name="glossary_list",
    )),
    (r'^glossaries/(?P<pk>\d+)/$', DetailView.as_view(
        model=Glossary,
    )),
    (r'^concepts/(?P<pk>\d+)/$', DetailView.as_view(
        model=Concept,
    )),
)

