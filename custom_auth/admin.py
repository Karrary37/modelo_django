from django.contrib import admin

from custom_auth.backoffice.customUser import CustomUserAdmin
from custom_auth.models import UserProfile

admin.site.register(UserProfile, CustomUserAdmin)
