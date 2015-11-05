# -*- encoding: utf-8 -*-

from django.db import models

class Family(models.Model):
	family_name = models.CharField(max_length=100) #Apellido familiar
	family_count = models.IntegerField(default=0) #Número de componentes de la familia
	family_id = models.CharField(max_length=24) #Id personal de la familia

	def __str__(self):
		return "Familia "+self.family_name
	def get_absolute_url(self):
		return reverse('family-detail', kwargs={'pk': self.pk})

class Member(models.Model):
	member_family_id = models.ForeignKey(Family) #Clave ajena que une al miembro de la familia con su familia
	member_name = models.CharField(max_length=100,label='Nombre') #Nombre del miembro de la familia
	member_surname = models.CharField(max_length=100) #Apellido o Apellidos del miembro de la familia
	member_sex = models.CharField(max_length=20) #Sexo del miembro de la familia
	member_birth = models.DateField('birth_date') #Fecha de nacimiento
	member_rip = models.DateField('rip_date',null=True,blank=True) #Fecha de defunción
	member_profile_image = models.ImageField(null=True,blank=True) #Imagen de perfil del miembro de la familia
	member_partner_id = models.IntegerField(default=0) #ID del cónyuge que sirve de enlace a una nueva familia
	member_email = models.EmailField(null=True,blank=True) #Correo electrónico de contacto

	def __str__(self):
		return self.member_surname+", "+self.member_name
	def get_absolute_url(self):
		return reverse('member-detail', kwargs={'pk': self.pk})
