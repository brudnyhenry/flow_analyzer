from django.contrib import admin
from .models import Traffic, Client
# Register your models here.

admin.site.register(Client)
admin.site.register(Traffic)