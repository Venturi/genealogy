from django.conf.urls import url

from . import views
from  .views import FamilyCreate,FamilyUpdate,FamilyDelete,MemberCreate,MemberUpdate,MemberDelete

urlpatterns = [
	url(r'^$', views.family, name='family'),
	url(r'^(?P<req_id>[0-9])+/$', views.reqFamily, name='family'),
	url(r'^member/(?P<mem_id>[0-9])+/$', views.reqMember, name='member'),
	url(r'^add/$', FamilyCreate.as_view(), name='add_family'),
	url(r'^(?P<fam_id>[0-9])+/edit/$', FamilyUpdate.as_view(), name='edit_family'),
	url(r'^(?P<fam_id>[0-9])+/delete/$', FamilyDelete.as_view(), name='delete_family'),
	url(r'^(?P<fam_id>[0-9])+/member/add/$', MemberCreate.as_view(), name='add_member'),
	url(r'^member/(?P<pk>[0-9])+/edit/$', MemberUpdate.as_view(), name='edit_member'),
	url(r'^member/(?P<pk>[0-9])+/delete/$', MemberDelete.as_view(), name='delete_member'),
]
