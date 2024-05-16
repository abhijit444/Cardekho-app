from django.contrib import admin
from .models import carlist, showroomlist, review



admin.site.site_header = 'Cardekho Project'
admin.site.site_title = 'Car showroom management system'
admin.site.index_title = "Dashboard"

class showroomlistAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'website')
    search_fields = ('name',)
    list_filter = ('name',)

class carlistAdmin(admin.ModelAdmin):
    list_display = ('model', 'description', 'price')
    search_fields = ('model','price')
    list_filter = ('model',)

class reviewlistAdmin(admin.ModelAdmin):
    list_display = ('rating', 'comments', 'cars', 'created', 'updated')
    search_fields = ('cars','created')
    list_filter = ('rating',)

# Register your models here.
admin.site.register(carlist, carlistAdmin)
admin.site.register(showroomlist, showroomlistAdmin)
admin.site.register(review, reviewlistAdmin)

