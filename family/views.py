# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404

#Importamos nuestros modelos de datos
from .models import Family, Member

#Importando formularios
from .forms import EditMember

def index(request):
	family_list = Family.objects.all
	context = {'family_list':family_list}
	return render(request, 'family/index.html',context)

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
	
def editMember(request, mem_id):
	member_data = get_object_or_404(Member, pk=mem_id)
	context = {'member_data':member_data}
	return render(request, 'family/edit_member.html',context)

def get_name(request):
	if request.method == 'POST':
		form = EditMember(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/thanks/')
	else:
		form = EditMember()
	return render(request, 'family/edit_member.html', {'form': form})
