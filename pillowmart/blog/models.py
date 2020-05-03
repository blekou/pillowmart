from django.db import models
# from django.contrib.auth.models import User
from configuration.models import UserAccount
# Create your models here.

class CathegorieArticle(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="images/CathegorieArticle")

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Cathegorie Article'
        verbose_name_plural = 'Cathegories Article'

    def __str__(self):
        return self.nom


class Tag(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.nom

class InstagramFeed(models.Model):
    image = models.ImageField(upload_to="images/InstagramFeed")

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Instagram Feed'
        verbose_name_plural = 'Instagram Feeds'

    def __str__(self):
        return str(self.image)


class Article(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    contenu = models.TextField()
    image = models.ImageField(upload_to="images/Article")
    tague = models.ManyToManyField(Tag, related_name='tag_Article')
    cathegorie = models.ForeignKey(
        CathegorieArticle, on_delete=models.CASCADE, related_name='cathegorie_Article')

    auteur = models.ForeignKey(UserAccount, related_name='auteur_article', on_delete=models.CASCADE, null=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.titre


class Commentaire(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='commentaire_article')
    user = models.ForeignKey(UserAccount, related_name='comment_user', on_delete=models.CASCADE, null=True)
    commentaire = models.TextField()
    # nom = models.CharField(max_length=255)
    # prenom = models.CharField(max_length=255)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    def __str__(self):
        return str(self.user)
