from django.contrib import admin
from .models import Girls

@admin.register(Girls)
class GirlsAdmin(admin.ModelAdmin):
    list_display =('user_name', 'user_url', 'verified')

