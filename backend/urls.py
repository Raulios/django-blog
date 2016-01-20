__author__ = 'raulmolinasanchez'
from django.conf.urls import url
from backend import views

urlpatterns = [
    url(r'^', views.index, name='user_panel_index'),
]