from django.contrib import admin

from .forms import AccountFormAdmin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    form = AccountFormAdmin

    class Media:
        js = (
            "js/jquery.mask.min.js",
            "js/custom.js",
        )


# Register your models here.
admin.site.register(Account, AccountAdmin)
