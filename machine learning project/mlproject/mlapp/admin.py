from django.contrib import admin

from .models import NewsHeadlinePrediction

# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'entry_date', 'status')
    list_display_links = ('name', 'email', 'entry_date', 'status')
    readonly_fields = ('prediction',)
    ordering = ('-entry_date',)

admin.site.register(NewsHeadlinePrediction, AccountAdmin)
