from django.contrib import admin

from . import models

from django.utils.safestring import mark_safe

from actions import Action


class SocialAccountAdmin(Action):
    list_display = ('nom', 'lien', 'date_add',
                    'date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['lien']
    ordering = ['nom']
    list_per_page = 10

    fieldsets = [
        ('Info SocialAccount', {
            'fields': ['nom', 'lien', 'icon']
        }),
        ('Standare', {
            'fields': ['status']
        })
    ]


class SiteInfoAdmin(Action):
    list_display = ('logo_view', 'email', 'date_add',
                    'date_update', 'status')
    list_filter = ('email', )
    search_fields = ('email', )
    date_hierarchy = 'date_add'
    list_display_links = ['email']
    ordering = ['email']
    list_per_page = 10
    fieldsets = [('Info du site', {'fields': ['email', 'logo', 'map_url']}),
                 ('Stavideondare', {'fields': ['status']})
                 ]

    def logo_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.logo.url))


class PresentationAdmin(Action):
    list_display = ('images_view', 'nom', 'date_add',
                    'date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info Presentation', {'fields': ['nom', 'description', 'image', 'video']}),
                 ('Stavideondare', {'fields': ['status']})
                 ]

    def images_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image.url))


class TemoignageAdmin(Action):
    list_display = ('images_view', 'nom', 'prenom', 'date_add',
                    'date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info Temoignage', {'fields': ['nom', 'prenom', 'message', 'photo']}),
                 ('Stavideondare', {'fields': ['status']})
                 ]

    def images_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.photo.url))


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.SocialAccount, SocialAccountAdmin)
_register(models.Presentation, PresentationAdmin)
_register(models.SiteInfo, SiteInfoAdmin)
_register(models.Temoignage, TemoignageAdmin)
