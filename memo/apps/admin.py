from django.contrib import admin

from .models import App


class AppAdmin(admin.ModelAdmin):
    model = App

admin.site.register(App)