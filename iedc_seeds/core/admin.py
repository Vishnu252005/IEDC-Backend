from django.contrib import admin
from core.models import Registrant

@admin.register(Registrant)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ['name']
