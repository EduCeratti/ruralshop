from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.offer_list),
    url(r'^offer/(?P<pk>[0-9]+)/$', views.offer_detail, name='offer_detail'),
    url(r'^offer/new/$', login_required(views.offer_new), name='offer_new'),
    url(r'^offer/(?P<pk>\d+)/edit/$', views.offer_edit, name='offer_edit'),
    url(r'^login/$', auth_views.login, name='login'),
]

