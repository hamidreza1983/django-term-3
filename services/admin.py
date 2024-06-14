from django.contrib import admin
from .models import *

class SpecialServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter  = ['status']
    search_fields = ['title']



admin.site.register(SpecialService, SpecialServiceAdmin)
admin.site.register(Team)
admin.site.register(Skills)
admin.site.register(Category)
admin.site.register(Options)
admin.site.register(Services)
admin.site.register(Comments)
# Register your models here.
