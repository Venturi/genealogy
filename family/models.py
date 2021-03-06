# -*- encoding: utf-8 -*-

from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

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
	member_profile_image = models.ImageField(_('Foto de perfil'),null=True,blank=True) #Imagen de perfil del miembro de la familia
	member_partner_id = models.IntegerField(default=0,null=True,blank=True,verbose_name='ID Pareja') #ID del cónyuge que sirve de enlace a una nueva familia
	member_email = models.EmailField('E-Mail',null=True,blank=True) #Correo electrónico de contacto

	def __str__(self):
		return self.member_surname+", "+self.member_name

#Perfil de usuario
class UserProfile(models.Model):
	user = models.OneToOneField(User)

	member_family_id = models.ForeignKey(Family,verbose_name='ID Familia') #Clave ajena que une al miembro de la familia con su familia
	member_name = models.CharField(verbose_name='Nombre',max_length=100) #Nombre del miembro de la familia
	member_surname = models.CharField(verbose_name='Apellidos',max_length=100) #Apellido o Apellidos del miembro de la familia
	member_sex = models.CharField(verbose_name='Sexo',choices=(('Hombre','Hombre'),('Mujer','Mujer'),('No especificado','No especificado')),max_length=20) #Sexo del miembro de la familia
	member_birth = models.DateField('Fecha de nacimiento',help_text='Fecha en este formato <em>AÑO-MES-DÍA</em>') #Fecha de nacimiento
	member_rip = models.DateField('Fecha de fallecimiento',null=True,blank=True) #Fecha de defunción
	member_profile_image = models.ImageField('Foto de perfil',null=True,blank=True) #Imagen de perfil del miembro de la familia
