from django.contrib import admin

from . import models

# Ajouter du HTML pour obtenir un rendu de l'image
from django.utils.safestring import mark_safe

from actions import Action


class CommentaireInline(admin.StackedInline):
    model = models.Commentaire
    extra = 1


class CathegorieArticleInline(admin.TabularInline):
    model = models.Article
    extra = 1


class CathegorieArticleAdmin(Action):
    list_display = ('nom', 'date_add', 'date_update',
                    'status', 'images_view')
    list_filter = ('status', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info Cathegorie', {'fields': ['nom', 'description', 'image']}),
                 ('Standare', {'fields': ['status']})
                 ]
    inlines = [CathegorieArticleInline]

    def images_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image.url))


class TagAdmin(Action):
    list_display = ('nom', 'date_add', 'date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info Tag', {'fields': ['nom', 'description']}),
                 ('Standare', {'fields': ['status']})
                 ]


class ArticleAdmin(Action):
    list_display = ('titre', 'date_add', 'date_update',
                    'status', 'images_view')
    list_filter = ('status', )
    search_fields = ('titre', )
    date_hierarchy = 'date_add'
    list_display_links = ['titre']
    ordering = ['titre']
    list_per_page = 10
    fieldsets = [('Info Article', {'fields': ['titre', 'contenu', 'description', 'image', 'tague', 'cathegorie']}),
                 ('Info Auteur', {'fields': ['auteur']}),
                 ('Standare', {'fields': ['status']}),
                 ]
    inlines = [CommentaireInline]

    def images_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image.url))


class InstagramFeedAdmin(Action):
    list_display = ('images_view', 'date_add', 'date_update', 'status')
    list_filter = ('status', )
    date_hierarchy = 'date_add'
    list_display_links = ['date_add', 'date_update']
    ordering = ['date_update']
    list_per_page = 14
    fieldsets = [('Image', {'fields': ['image', ]}),
                 ('Standare', {'fields': ['status']})
                 ]

    def images_view(self, obj):
        return mark_safe('<img src="{url}" style="height:100px; width:100px">'.format(url=obj.image.url))



# class CommentaireAdmin(Action):
#     list_display = ('nom', 'prenom', 'article', 'date_add',
#                     'date_update', 'status')
#     list_filter = ('nom', )
#     search_fields = ('article', )
#     date_hierarchy = 'date_add'
#     list_display_links = ['article']
#     ordering = ['article']
#     list_per_page = 10
#     fieldsets = [('Info Commentaire', {'fields': ['article', 'nom', 'commentaire']}),
#                  ('Standare', {'fields': ['status']})
#                  ]


class CommentaireAdmin(Action):
    list_display = ('user', 'article', 'date_add',
                    'date_update', 'status')
    list_filter = ('status', 'user', 'article')
    search_fields = ('article', 'user')
    date_hierarchy = 'date_add'
    list_display_links = ['article']
    ordering = ['article']
    list_per_page = 10
    fieldsets = [('Info Commentaire', {'fields': ['article', 'user', 'commentaire']}),
                 ('Standare', {'fields': ['status']})
                 ]

def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Tag, TagAdmin)
_register(models.InstagramFeed , InstagramFeedAdmin)
_register(models.Article, ArticleAdmin)
_register(models.Commentaire, CommentaireAdmin)
_register(models.CathegorieArticle, CathegorieArticleAdmin)
