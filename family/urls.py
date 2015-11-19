# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth.decorators import login_required, permission_required

from . import views
from  .views import FamilyCreate,FamilyUpdate,FamilyDelete,MemberCreate,MemberUpdate,MemberDelete

urlpatterns = [
	url(r'^$', login_required(views.family), name='family'),
	url(r'^(?P<req_id>[0-9])+/$', login_required(views.reqFamily), name='family'),
	url(r'^member/(?P<mem_id>[0-9])+/$', login_required(views.reqMember), name='member'),
	url(r'^add/$', login_required(FamilyCreate.as_view()), name='add_family'),
	url(r'^(?P<fam_id>[0-9])+/edit/$', login_required(FamilyUpdate.as_view()), name='edit_family'),
	url(r'^(?P<fam_id>[0-9])+/delete/$', login_required(FamilyDelete.as_view()), name='delete_family'),
	url(r'^(?P<fam_id>[0-9])+/member/add/$', login_required(MemberCreate.as_view()), name='add_member'),
	url(r'^member/(?P<pk>[0-9])+/edit/$', login_required(MemberUpdate.as_view()), name='edit_member'),
	url(r'^member/(?P<pk>[0-9])+/delete/$', login_required(MemberDelete.as_view()), name='delete_member'),
]
