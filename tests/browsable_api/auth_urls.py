from __future__ import unicode_literals
from django.conf.urls import patterns, url, include

from .views import MockView

urlpatterns = patterns(
    '',
    (r'^$', MockView.as_view()),
    url(r'^auth/', include('drf2.urls', namespace='drf2')),
)
