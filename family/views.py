# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404

#Autenticación
from django.contrib.auth.decorators import login_required

#Importamos nuestros modelos de datos
from .models import Family, Member

#reCaptcha
from captcha.fields import ReCaptchaField

#Forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

def index(request):
	return render(request, 'index.html')

@login_required(login_url='/')
def family(request):
	family_list = Family.objects.all
	captcha = ReCaptchaField()
	context = {'family_list':family_list}
	return render(request, 'family/family.html',context)

def reqFamily(request, req_id):
	family = get_object_or_404(Family, pk=req_id)
	members = Member.objects.filter(member_family_id=req_id)
	context = {'family':family,'members':members}
	return render(request, 'family/viewFamily.html',context)
	
def reqMember(request, mem_id):
	member_data = get_object_or_404(Member, pk=mem_id)
	fam_id = member_data.member_family_id.id
	family_data = get_object_or_404(Family, pk=fam_id)
	context = {'member_data':member_data,'family_data':family_data}
	return render(request, 'family/viewFamMember.html',context)

class FamilyCreate(CreateView):
	model = Family
	template_name = 'family/create_family.html'
	fields = '__all__'
	success_url = '/family/'

class FamilyUpdate(UpdateView):
	model = Family
	template_name = 'family/edit_family.html'
	fields = '__all__'
	success_url = '/family/'

class FamilyDelete(DeleteView):
	model = Family
	success_url = reverse_lazy('family-list')

class MemberCreate(CreateView):
	model = Member
	fam_id = Member.member_family_id
	template_name = 'family/create_member.html'
	fields = '__all__'
	success_url = '/family/'

class MemberUpdate(UpdateView):
	model = Member
	template_name = 'family/edit_member.html'
	fields = ['member_name','member_surname','member_sex','member_profile_image','member_birth','member_rip','member_email']
	success_url = '/family/'

class MemberDelete(DeleteView):
	model = Member
	success_url = reverse_lazy('member-list')
