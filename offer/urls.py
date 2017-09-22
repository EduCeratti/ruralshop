from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.offer_list),
    url(r'^offer/(?P<pk>[0-9]+)/$', views.offer_detail, name='offer_detail'),
    url(r'^offer/new/$', views.offer_new, name='offer_new'),
]

