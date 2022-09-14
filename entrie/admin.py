from django.contrib import admin

from .models import Entrie


# Register your models here.
class EntrieAdmin(admin.ModelAdmin):
    ...


# Register your models here.
admin.site.register(Entrie, EntrieAdmin)
