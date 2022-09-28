# Register your models here.
from django.contrib import admin

from .models import Report


# Register your models here.
class ReportAdmin(admin.ModelAdmin):
    ...


# Register your models here.
admin.site.register(Report, ReportAdmin)
