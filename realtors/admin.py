from django.contrib import admin

from .models import Realtor
# Register your models here.

class RealtorAdmin(admin.ModelAdmin):
    list_admin = ('id', 'name', 'email', 'hire_date')
    iist_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25

# Register your models here.
admin.site.register(Realtor)