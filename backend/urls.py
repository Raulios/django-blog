__author__ = 'raulmolinasanchez'
from django.conf.urls import url
from backend import views

urlpatterns = [

    url(r'^$', views.index, name='user_panel_index'),

    url(r'^posts/$', views.posts, name='user_panel_posts'),
    url(r'^posts/(?P<post_id>[0-9]+)/$', views.edit_post, name='user_panel_edit_post'),
    url(r'^delete_post/(?P<post_id>[0-9]+)/$', views.delete_post, name='user_panel_delete_post'),
    url(r'^add_post/$', views.add_post, name='user_panel_add_post'),

    url(r'^categories/$', views.categories, name='user_panel_categories'),
    url(r'^categories/(?P<category_id>[0-9]+)/$', views.edit_category, name='user_panel_edit_category'),
    url(r'^delete_category/(?P<category_id>[0-9]+)/$', views.delete_category, name='user_panel_delete_category'),
    url(r'^add_category/$', views.add_category, name='user_panel_add_category'),
]