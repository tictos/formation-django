from formulaire.models import Contact
from django.forms import ModelForm, Textarea

class ContactForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Nom"
        self.fields['firstname'].label = "Prénom"
        self.fields['email'].label = "Email"

    class Meta:

        models = Contact
        fields = ('name', 'firstname', 'email', 'message')
        widgets = {'message': Textarea(attrs={'cols':60, 'rows':10}),}