from django.conf.urls import patterns, include, url
from django.contrib import admin

from base import views as base_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ProjectManagement.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', base_views.index, name='show_group_list_map'),
    # url(r'^weixin/show_group_list_map$', weixin_views.show_group_list_map, name='show_group_list_map'),
)
