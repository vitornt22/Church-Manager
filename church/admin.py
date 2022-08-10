from django.contrib import admin

from .models import Church
from .forms import ChurchFormAdmin


class ChurchAdmin(admin.ModelAdmin):

    form = ChurchFormAdmin


    class Media:
        js = (
            "js/jquery.mask.min.js",
            "js/custom.js",
        )


# Register your models here.
admin.site.register(Church, ChurchAdmin)
