# -*- coding: utf-8 -*-
from django import forms
from .models import Member, UserProfile
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User

class MemberUpdateForm(UpdateView):
	model = Member
	fields = '__all__'

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('member_name','member_surname','member_family_id','member_sex','member_birth','member_rip','member_profile_image')
