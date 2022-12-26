from django.contrib import admin

from utilisat.models import *

# Register your models here.

class UtilisateurAdmin(admin.ModelAdmin):

    list_display = ("nom")

class EmailAdmin(admin.ModelAdmin):

    list_display = ("mail", "user")
    
class ListeAdmin(admin.ModelAdmin):

    list_display = ("listName", "email")

admin.site.register(Utilisateur)
admin.site.register(Email)
admin.site.register(ListeDiffusion)