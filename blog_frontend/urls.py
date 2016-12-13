__author__ = 'raulmolinasanchez'
from django.conf.urls import url
from blog_frontend import views

urlpatterns = [
    url(r'^', views.index, name='index'),
]