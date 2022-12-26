from django.db import models

# Create your models here.

class Utilisateur(models.Model):

    nom = models.CharField(max_length=30)

    def __str__(self):
        return  self.nom

class Email(models.Model):
    mail = models.EmailField()
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='emails', null=True)

    def __str__(self):
        return self.mail

class ListeDiffusion(models.Model):
    listeName = models.CharField(max_length=30)
    email = models.ManyToManyField(Email, related_name='listes')

    def __str__(self):
        return self.listeName
        
