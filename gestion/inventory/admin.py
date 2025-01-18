from django.contrib import admin
from .models import Client, Medicament, Fournisseur, Commande

admin.site.register(Client)
admin.site.register(Medicament)
admin.site.register(Fournisseur)
admin.site.register(Commande)
