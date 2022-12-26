from django.shortcuts import render
from .models import *
# Create your views here.

# utilisateur
"""
user1 = Utilisateur(nom="user1")
user2 = Utilisateur(nom="user2")


# Email

email1 = Email(mail="user1@gmail.fr", user=user1)
email2 = Email(mail="user2@bibi.fr", user=user2)

# Listes

liste1 = ListeDiffusion(listeName="liste1")
liste2 = ListeDiffusion(listeName="liste2")
liste3 = ListeDiffusion(listeName="liste3")
liste4 = ListeDiffusion(listeName="liste4")

# sauvegarde

user1.save()
user2.save()

email1.save()
email2.save()

liste1.save()
liste2.save()
liste3.save()
liste4.save()

# rajout des email aux listes

liste1.email.add(email1)
liste1.email.add(email2)
liste3.email.add(email1)
liste3.email.add(email2)
liste4.email.add(email2)
liste2.email.add(email1)
"""

def listdiffuse(request):
    email = Email.objects.filter(mail)
    listed = ListeDiffusion.objects.all()
    
    context = {'listed': listed, 'utilisateurs': email, 'user':user}
    return render(request, 'listed.html', context)


def email_detail(request,pk):
    email = Email.objects.get(id=pk)
    user = email.user
    listes_abonnees = email.listes.all()
    context = {
        'email': email.mail,
        'user': user,
        'listes': listes_abonnees
    }

    return render(request, 'email_detail.html', context)
