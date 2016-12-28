from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User




 

class Theme(models.Model):

    intitule = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.intitule


    
class Proposition(models.Model):

    ennonce = models.CharField(max_length=200, null=True)
    date_creation = models.DateField (default= timezone.now, null=True)
    categorie =  models.ForeignKey(Theme, null=True, blank = True)
    supporter = models.ManyToManyField(User, through= "Soutien", null =True)
    champ_lexical = models.CharField (max_length = 100000, default = "vide", null = True)

    def __str__(self):
        return self.ennonce


class Lieu (models.Model):
    pays = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    
    def __str__(self):
        return self.ville

class Autre_utilisateur (models.Model):
    user = models.ForeignKey(User, null =True)

    def __str__(self):
        return "utilisateur {0} ".format (self.user)

class Evenement (models.Model):
    titre = models.CharField(max_length = 100, null=True)
    lieu = models.ForeignKey (Lieu, null=True)
    date = models.DateField (null=True)
    description = models.CharField(max_length = 10000, null = True)
    proposition = models.ForeignKey (Proposition, null=True)
    participants= models.ManyToManyField(User, through= "Soutien", null =True)

    def __str__(self):
        return self.titre


class Profile (models.Model):
    utilisateur = models.ForeignKey(User, null=True)
    lieu = models.ForeignKey (Lieu, null=True)
    theme_favoris = models.CharField(max_length = 200, null = True)
    utilisateurs_proches = models.ManyToManyField (Autre_utilisateur, through ="Proximite")

    def __str__(self):
        return "profile de {0}".format(self.utilisateur)




        
class Organisation (models.Model):
    description = models.CharField(max_length = 200, null = True)
    profile = models.ForeignKey(Profile, null=True)
    adherent =  models.ManyToManyField(User, through= "Soutien", null =True)

    def __str__(self):
        return "organisation {0}".format(self.profile)



class Petition(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField("Descrition de la pétition")
    propositions = models.ManyToManyField(Proposition, null=True)
    date_creation = models.DateField("Date de création", auto_now=True)
    date_echeance = models.DateField("Date d'échéance", null=True, blank=True)
    objectif_de_signataires = models.IntegerField(null=True)
    signataires = models.ManyToManyField(User, through="Soutien", null=True)

    """
    def __createur(self):
        soutien = Soutien.objects.filter(petition=self, lien = 'CR')
        return 
    createur = property(__createur)
    """

    def __nb_signataires(self):
        return Soutien.objects.filter(petition=self).count()
    nb_signataires = property(__nb_signataires)


    def __taux_objectif(self):
        if self.objectif_de_signataires != 0:
            return Soutien.objects.filter(petition=self).count() / self.objectif_de_signataires * 100
        else:
            return null
    taux_objectif = property(__taux_objectif)

    def __str__(self):
        return self.titre



class Soutien(models.Model):

    CHOIX_LIEN= (
                ('CR' , 'createur'),
                ('SO', 'soutien')
    )
    propositions = models.ForeignKey(Proposition, null =True)
    user = models.ForeignKey(User, null=True)
    lien = models.CharField(max_length =2, choices= CHOIX_LIEN)

    # Elément soutenu
    evenement = models.ForeignKey(Evenement, null = True)
    organisation = models.ForeignKey(Organisation, null = True)
    petition = models.ForeignKey(Petition, null = True)

    def __str__(self):
        return self.user.username



class Proximite(models.Model):
    profile = models.ForeignKey(Profile, null =True)
    Autre_utilisateur = models.ForeignKey (Autre_utilisateur)
    proba = models.DecimalField( max_digits=5, decimal_places=3)

    def __str__(self):
        return "proximite entre {0} et {1} ".format(self.profile , self.Autre_utilisateur)








