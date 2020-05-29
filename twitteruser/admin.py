from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from twitteruser.models import Profile

# Register your models here.

UserAdmin.fieldsets += ('Custom fields set', {'fields': ('following',)}),

admin.site.register(Profile, UserAdmin)
