# admin.py
from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email_confirmed', 'created_at')  # show these columns
    search_fields = ('user__username', 'user__email')         # searchable
    ordering = ('-created_at',)                               # newest first
    fieldsets = (
        ('User Info', {'fields': ('user', 'image')}),
        ('Verification', {'fields': ('email_confirmed',)}),
    )
