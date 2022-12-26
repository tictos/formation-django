from pyexpat.errors import messages
from django.shortcuts import render
#from formulaire.forms import ContactForm
from django.forms import EmailInput, ModelForm, Textarea 
from formulaire.models import *
from django.contrib import messages
# Create your views here.

class ContactForm(ModelForm):

    """def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Nom"
        self.fields['firstname'].label = "Prénom"
        self.fields['email'].label = "Email"
"""
    class Meta:

        model = Contact
        fields = ('name', 'firstname', 'email', 'message')
        widgets = {
            'message': Textarea(attrs={'cols':60, 'rows':10}),
            'email': EmailInput(attrs={'class': 'form-control'})
            }





    """  models = Contact
        fields = ('name', 'firstname', 'email', 'message')
        widgets = {
            'name' : Textarea(attrs={'cols':80, 'rows':20})
        }"""

"""class ContactForm2(forms.Form):

    name = forms.CharField(max_length=200, initial = "votre nom", label="nom")
    firstname = forms.CharField(max_length=200, initial='Votre Prénom', label='Votre Prénom')
    email = forms.EmailField(label='email')
    message = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':10}))
"""
def contact(request):
    # instanciée le formulaire
    
    # on test si on est bien en validation de formulaire (POST)
    if request.method == "POST":
        form = ContactForm(request.POST)
        # si oui on recupère les données posté
        

        if form.is_valid():
            new_contact = form.save()

            # le message
            messages.success(request, 'Nouveau contact ' + new_contact.name + ' ' + new_contact.email )

            context = {'pers': new_contact}

            return render(request,'detail.html',context)
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form':form})

def detail(request, cid):
    contact = Contact.objects.get(pk=cid)

    context = {'pers':contact}

    return render(request,'detail.html', context)



"""def contact(request):

    #contact_form = ContactForm()
    contact_form2 = ContactForm2()
    return render(request, 'contact.html', {'contact_form2':contact_form2} )"""