# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect #Necesario para el redirect al hacer logout

#Autenticación
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

#Importamos nuestros modelos de datos
from .models import Family, Member, UserProfile
from .forms import UserForm, UserProfileForm

#reCaptcha
from captcha.fields import ReCaptchaField

#Forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def regForm(request):
	new_user = RegUserForm()
	context = {'new_user':new_user}
	return render(request, 'register.html',context)

def logForm(request):
	log_user = LoginForm()
	context = {'log_user':log_user}
	return render(request, 'index.html',context)

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

def register(request):
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			if 'member_profile_image' in request.FILES:
				profile.picture = request.FILES['member_profile_image']
			profile.save()
			registered = True
		else:
			print user_form.errors, profile_form.errors
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	return render(request,
			'register.html',
			{'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

#Edición del Usuario para agregar o modificar datos de su perfil
class UserUpdate(UpdateView):
	model = UserProfile
	template_name = 'family/edit_member.html'
	fields = ['member_name','member_surname','member_sex','member_profile_image','member_birth','member_rip','member_email']
	success_url = '/family/'
	def get_context_data(self, **kwargs):
		context = super(MemberUpdate, self).get_context_data(**kwargs)
		context['member_data'] = self.object
		return context


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
	fields = ['member_name','member_surname','member_sex','member_profile_image','member_birth','member_rip','member_email']
	success_url = '/family/'
	def get_context_data(self, **kwargs):
		context = super(MemberCreate, self).get_context_data(**kwargs)
		context['family_data'] = self.object
		return context

class MemberUpdate(UpdateView):
	model = Member
	template_name = 'family/edit_member.html'
	fields = ['member_name','member_surname','member_sex','member_profile_image','member_birth','member_rip','member_email']
	success_url = '/family/'
	def get_context_data(self, **kwargs):
		context = super(MemberUpdate, self).get_context_data(**kwargs)
		context['member_data'] = self.object
		return context

class MemberDelete(DeleteView):
	model = Member
	success_url = reverse_lazy('member-list')
