from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.CathegorieArticle)
admin.site.register(models.Tag)
admin.site.register(models.Article)
admin.site.register(models.Commentaire)