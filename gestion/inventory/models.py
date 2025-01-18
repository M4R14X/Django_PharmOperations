from django.db import models

class Fournisseur(models.Model):
    nom_fournisseur = models.CharField(max_length=50)
    adress_fournisseur = models.CharField(max_length=50)
    tele_fournisseur = models.CharField(max_length=15)
    email_fournisseur = models.EmailField()

    def __str__(self):
        return self.nom_fournisseur

class Medicament(models.Model):
    nom_medicament = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    prix = models.DecimalField(max_digits=15, decimal_places=3)
    quantite_stock = models.PositiveIntegerField()
    date_exp = models.DateField()
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, related_name="medicaments")

    def __str__(self):
        return self.nom_medicament

class Client(models.Model):
    nom_prenom_client = models.CharField(max_length=50)
    tele_client = models.CharField(max_length=15)
    email_client = models.EmailField()
    adress_client = models.CharField(max_length=50)

    def __str__(self):
        return self.nom_prenom_client

class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="commandes")
    medicament = models.ManyToManyField(Medicament, through="CommandeDetail")
    total = models.DecimalField(max_digits=15, decimal_places=3)
    date_commande = models.DateField()

    def __str__(self):
        return f"Commande {self.id} - Client: {self.client.nom_prenom_client}"

class CommandeDetail(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.commande} - {self.medicament} (x{self.quantite})"
