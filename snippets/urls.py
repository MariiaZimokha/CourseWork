from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = patterns('',
			#url(r'^snippets/$', views.index),
			url(r'^snippets/$', views.SnippetList.as_view()),
			url(r'^user/$', views.UserAPI.as_view()),
			url(r'^serials/$', views.SerialList.as_view()),
			url(r'^subscribe/(?P<registrationId>[^/]+)$',views.SubscribeList.as_view()),
			
			url(r'^send$', views.my_scheduled_job),
			
# 			url(r'^snippets/$', views.get_list_of_serials),
 			url(r'^snippets/(?P<pk>[0-9]+)$', views.SnippetDetail.as_view()),
                       #url(r'^serials/(?P<pk>[0-9]+)$', views.SerialDetail.as_view()),
            url(r'^serials/(?P<pk>[0-9]+)&(?P<registrationId>[^/]+)$', views.SerialDetail.as_view(),name='detail'),
#  			url(r'^serials/(?P<pk>)/Season/$', views.SerialDetail.as_view()),
            
			)

urlpatterns = format_suffix_patterns(urlpatterns)
