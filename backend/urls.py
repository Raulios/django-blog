__author__ = 'raulmolinasanchez'
from django.conf.urls import url
from backend import views

urlpatterns = [

    url(r'^$', views.index, name='user_panel_index'),
    url(r'^posts/$', views.posts, name='user_panel_posts'),
    url(r'^posts/(?P<post_id>[0-9]+)/$', views.edit_post, name='user_panel_edit_post'),
]