from django.contrib import admin

from . import models

# Register your models here.


from django.utils.safestring import mark_safe


class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'sujet',
                    'date_add', 'date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['date_add']
    list_per_page = 15
    fieldsets = [('Info Contact', {'fields': ['nom', 'email', 'sujet', 'message']}),
                 ('Standare', {'fields': ['status']})
                 ]


class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'date_add', 'date_update', 'status')
    list_filter = ('id', )
    search_fields = ('email', )
    date_hierarchy = 'date_add'
    list_display_links = ['email']
    ordering = ['id', 'email']
    list_per_page = 10
    fieldsets = [('Info NewsLetter', {'fields': ['email']}),
                 ('Standare', {'fields': ['status']})
                 ]


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Contact, ContactAdmin)
_register(models.NewsLetter, NewsLetterAdmin)
