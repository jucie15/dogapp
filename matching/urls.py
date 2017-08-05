from django.conf.urls import url
from matching import views

urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^result/(?P<pk>\d+)/$', views.result, name='result'),
]
