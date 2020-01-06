from django.contrib import admin

from .models import Page, Property, Apartment, Size, Status, Sector



class PageAdmin(admin.ModelAdmin):
    list_display = ('title','update_date')
    ordering = ('title',)
    search_fields = ('title',)


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ('name',)


class SizeAdmin(admin.ModelAdmin):
    list_display = ('size',)
    ordering = ('size',)
    search_fields = ('size',)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('status',)
    ordering = ('status',)
    search_fields = ('status',)


class SectorAdmin(admin.ModelAdmin):
    list_display = ('sector',)
    ordering = ('sector',)
    search_fields = ('sector',)


class AptAdmin(admin.ModelAdmin):
    list_display = ('property','aptNumber','size',)
    ordering = ('property',)
    search_fields = ('property',)


admin.site.register(Page, PageAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Apartment, AptAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Sector, SectorAdmin)