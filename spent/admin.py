from django.contrib import admin

from .models import Spent


# Register your models here.
class SpentAdmin(admin.ModelAdmin):
    ...


# Register your models here.
admin.site.register(Spent, SpentAdmin)
