from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.SocialAccount)
admin.site.register(models.SiteInfo)
admin.site.register(models.Presentation)
admin.site.register(models.Temoignage)