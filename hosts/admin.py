import whois
from datetime import datetime
from sys import argv,exit
import requests
from django.contrib import admin
from .models import Host

now = datetime.now()


def toggle_check_hosts(modeladmin, request, queryset):
    for item in queryset:
        try:
            r = requests.get(item.host_name)
            print(f'{item.host_name} {r.status_code}')
            if r.status_code == 200:
                item.status = True
            else:
                item.status = False
        except requests.RequestException:
            item.status = False
        w = whois.whois(item.host_name)
        a = w.expiration_date
        x = w.text
        item.save()


toggle_check_hosts.short_description = 'Проверить'


@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    list_display = ('host_name', 'port', 'status', 'created', 'updated')
    actions = [toggle_check_hosts]

