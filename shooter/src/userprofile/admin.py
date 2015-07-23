from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .models import Person, User, Clubmember


class PersonAdmin(admin.ModelAdmin):
	class Meta:
		model = Person

admin.site.register(Person, PersonAdmin)

class MyUserAdmin(admin.ModelAdmin):
	class Meta:
		model = User

admin.site.register(User, MyUserAdmin)

admin.site.unregister(Group)

class ClubmemberAdmin(admin.ModelAdmin):
	class Meta:
		model = Clubmember

admin.site.register(Clubmember, ClubmemberAdmin)
