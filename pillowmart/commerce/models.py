from django.db import models

# Create your models here.
from configuration.models import UserAccount



class Cathegorie(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="images/Cathegorie")

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Cathegorie'
        verbose_name_plural = 'Cathegories'

    def __str__(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/Produit")
    description = models.TextField()
    prix = models.IntegerField()
    cathegorie = models.ForeignKey(Cathegorie, on_delete=models.CASCADE, related_name='cathegorie_Product')

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Produit'
        verbose_name_plural = 'Produits'

    def __str__(self):
        return self.nom


class Panier(models.Model):
    user = models.ForeignKey(UserAccount, related_name='user_panier', on_delete=models.CASCADE, null=True)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='produit_panier')
    quantite = models.PositiveSmallIntegerField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Panier'
        verbose_name_plural = 'Entrepot'

    def __str__(self):
        return str(self.user)
