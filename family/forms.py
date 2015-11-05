# -*- coding: utf-8 -*-
from django import forms
from .models import Member
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import UpdateView

class MemberUpdateForm(UpdateView):
	model = Member
	fields = '__all__'
