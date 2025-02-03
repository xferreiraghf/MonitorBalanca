from django.contrib import admin
from .models import Host

@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'operating_system', 'ip_address', 'flask_port')
    search_fields = ('name', 'company', 'ip_address')
    list_filter = ('company', 'operating_system')
