from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	#url(r'(?P<req_id>)/', views.reqFamily, name='family'),
	url(r'^(?P<req_id>[0-9])+/$', views.reqFamily, name='family'),
	url(r'^member/(?P<mem_id>[0-9])+/$', views.reqMember, name='member'),
	url(r'^member/edit/(?P<mem_id>[0-9])+/$', views.editMember, name='member_data'),
]
