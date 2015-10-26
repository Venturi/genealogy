# -*- coding: utf-8 -*-
from django import forms

class EditMember(forms.Form):
	member_name = forms.CharField(label="Nombre:",max_length=100) #Nombre del miembro de la familia
	member_surname = forms.CharField(label="Apellidos:",max_length=100) #Apellido o Apellidos del miembro de la familia
	#member_sex = forms.CharField(max_length=20) #Sexo del miembro de la familia
	#member_birth = forms.DateField('birth_date') #Fecha de nacimiento
	#member_rip = forms.DateField('rip_date',null=True,blank=True) #Fecha de defunción
	#member_profile_image = forms.ImageField(null=True,blank=True) #Imagen de perfil del miembro de la familia
	#member_partner_id = forms.IntegerField(default=0) #ID del cónyuge que sirve de enlace a una nueva familia
