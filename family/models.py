# -*- encoding: utf-8 -*-

from django.db import models
from django import forms
from django.contrib.auth.models import User

#Modelos de datos
class Family(models.Model):
	family_name = models.CharField('Apellidos familiares',max_length=100) #Apellidos familiares
	family_id = models.CharField('ID personalizado',max_length=24) #Id personal de la familia

	def __str__(self):
		return "Familia "+self.family_name

class Member(models.Model):
	member_family_id = models.ForeignKey(Family,verbose_name='ID Familia') #Clave ajena que une al miembro de la familia con su familia
	member_name = models.CharField(verbose_name='Nombre',max_length=100) #Nombre del miembro de la familia
	member_surname = models.CharField(verbose_name='Apellidos',max_length=100) #Apellido o Apellidos del miembro de la familia
	member_sex = models.CharField(verbose_name='Sexo',choices=(('Hombre','Hombre'),('Mujer','Mujer'),('No especificado','No especificado')),max_length=20) #Sexo del miembro de la familia
	member_birth = models.DateField('Fecha de nacimiento',help_text='Fecha en este formato <em>AÑO-MES-DÍA</em>') #Fecha de nacimiento
	member_rip = models.DateField('Fecha de fallecimiento',null=True,blank=True) #Fecha de defunción
	member_profile_image = models.ImageField('Foto de perfil',null=True,blank=True) #Imagen de perfil del miembro de la familia
	member_partner_id = models.IntegerField(default=0,null=True,blank=True,verbose_name='ID Pareja') #ID del cónyuge que sirve de enlace a una nueva familia
	member_email = models.EmailField('E-Mail',null=True,blank=True) #Correo electrónico de contacto

	def __str__(self):
		return self.member_surname+", "+self.member_name
#Perfil de usuario
class UserProfile(models.Model):
	# This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User)

	member_family_id = models.ForeignKey(Family,verbose_name='ID Familia') #Clave ajena que une al miembro de la familia con su familia
	member_name = models.CharField(verbose_name='Nombre',max_length=100) #Nombre del miembro de la familia
	member_surname = models.CharField(verbose_name='Apellidos',max_length=100) #Apellido o Apellidos del miembro de la familia
	member_sex = models.CharField(verbose_name='Sexo',choices=(('Hombre','Hombre'),('Mujer','Mujer'),('No especificado','No especificado')),max_length=20) #Sexo del miembro de la familia
	member_birth = models.DateField('Fecha de nacimiento',help_text='Fecha en este formato <em>AÑO-MES-DÍA</em>') #Fecha de nacimiento
	member_rip = models.DateField('Fecha de fallecimiento',null=True,blank=True) #Fecha de defunción
	member_profile_image = models.ImageField('Foto de perfil',null=True,blank=True) #Imagen de perfil del miembro de la familia
	member_partner_id = models.IntegerField(default=0,null=True,blank=True,verbose_name='ID Pareja') #ID del cónyuge que sirve de enlace a una nueva familia
	member_email = models.EmailField('E-Mail',null=True,blank=True) #Correo electrónico de contacto

#Modelos para formularios
class RegUser(forms.Form):
	reg_username = forms.CharField(label='Usuario',max_length=100) #Login del usuario nuevo
	reg_password = forms.CharField(label='Contraseña',min_length=8,max_length=32, widget=forms.PasswordInput) #Password usuario nuevo
	reg_repassword = forms.CharField(label='Vuelva a introducirla',min_length=8,max_length=32, widget=forms.PasswordInput)
	reg_email = forms.EmailField(label='E-Mail') #Email usuario nuevo
	reg_firstname = forms.CharField(label='Nombre', max_length=100) #Nombre del usuario nuevo
	reg_surname = forms.CharField(label='Apellidos',max_length=200) #Apellidos del usuario nuevo
	reg_birth = forms.DateField(label='Fecha de nacimiento') #Fecha de nacimiento
	reg_profile_image = models.ImageField('Foto de perfil',null=True,blank=True)
	class Meta:
		model = User
		fields = '__all__'
	def save(self,commit=False):
		user = super(RegUser, self).save(commit=False)
		user.set_password(self.cleaned_data["reg_password"])
		if commit:
			user.save()
		return user
