from django.contrib import admin
from .models import Girls

@admin.register(Girls)
class GirlsAdmin(admin.ModelAdmin):
    list_display =('user_name', 'onlyfans_url', 'verified')

