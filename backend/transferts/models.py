from django.db import models

# Create your models here.


class Transfert(models.Model):
    date = models.DateField(auto_now_add=True)
    id_client_source = models.CharField(max_length=30)
    id_client_destination = models.CharField(max_length=30, null=True)
    montant = models.IntegerField()
    id_abonne_source = models.CharField(max_length=30, null=True)
    id_abonne_destination = models.CharField(max_length=30, null=True)
