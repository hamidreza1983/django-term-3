from django.contrib import admin
from .models import SpecialService, Team, Skills

class SpecialServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter  = ['status']
    search_fields = ['title']



admin.site.register(SpecialService, SpecialServiceAdmin)
admin.site.register(Team)
admin.site.register(Skills)
# Register your models here.
