# -*- encoding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from .models import Family, Member

admin.site.register(Family)
admin.site.register(Member)
