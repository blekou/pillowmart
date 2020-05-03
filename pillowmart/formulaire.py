from django import forms
from contact.models import Contact
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from configuration.models import UserAccount



class LoginForm(forms.Form):
    '''
        Formulaire de connexion
    '''
    username = forms.CharField(label=None, widget=forms.TextInput(
            attrs={
                    'id': 'name',
                    'placeholder': 'Username',
                    'class': 'form-control',
                }
    ))
    password = forms.CharField(label=None, widget=forms.PasswordInput(
            attrs={
                    'id':'password',
                    'placeholder':'Password',
                    'class': 'form-control',
                }
    ))



class RegisterForm(forms.ModelForm):
    '''
        Formulaire d'inscription
    '''
    last_name = forms.CharField(label="Nom", widget=forms.TextInput(
            attrs={
                    'placeholder':'Entrez votre nom',
                    'class': 'form-control',
                }
    ))
    first_name = forms.CharField(label="Prenom", widget=forms.TextInput(
            attrs={
                    'placeholder':'Entrez votre prenom',
                    'class': 'form-control',
                }
    ))
    username = forms.CharField(label="Nom d'utilisateur", widget=forms.TextInput(
            attrs={
                    'placeholder':'Nom d\'utilisateur',
                    'class': 'form-control',
                }
    ))
    email = forms.CharField(label='Email', widget=forms.EmailInput(
            attrs={
                    'placeholder':'Email',
                    'class': 'form-control',
                }
    ))
    avatar = forms.ImageField(required=False, label='Email', widget=forms.ClearableFileInput(
            attrs={
                    'placeholder':'Photo de profile',
                    'class': 'form-control',
                }
    ))

    password1 = forms.CharField(label=None, widget=forms.PasswordInput(
            attrs={
                    'placeholder':'Mot de passe',
                    'class': 'form-control',
                }
    ))
    password2 = forms.CharField(label=None, widget=forms.PasswordInput(
            attrs={
                    'placeholder':'Confirmer le mot de passe',
                    'class': 'form-control',
                }
    ))

    class Meta:
        model = UserAccount
        fields = ('last_name', 'first_name', 'username', 'email', 'avatar', 'password1', 'password2')



class ContactForm(forms.ModelForm):
    '''
        Formulaire de contact
    '''
    nom = forms.CharField(label=None, widget=forms.TextInput(
        attrs={
            'id': 'name',
            'class': "form-control",
            'placeholder': "Enter your name",
            'onfocus':"this.placeholder = ''",
            'onblur':"this.placeholder = 'Enter your name'",
        }
    ))
    email = forms.CharField(label=None, widget=forms.EmailInput(attrs={
            'id': 'email',
            'class': "form-control",
            'placeholder': "Enter email address",
            'onfocus':"this.placeholder = ''",
            'onblur':"this.placeholder = 'Enter email address'",
        }
    ))
    sujet = forms.CharField(label=None, widget=forms.TextInput(
        attrs={
            'id': 'subject',
            'class': "form-control",
            'placeholder': "Enter Subject",
            'onfocus':"this.placeholder = ''",
            'onblur':"this.placeholder = 'Enter Subject'",
        }
    ))
    message = forms.CharField(label=None, widget=forms.Textarea(
        attrs={
            'id': 'message',
            'class': "form-control w-100",
            'placeholder': "Enter Message",
            'onfocus':"this.placeholder = ''",
            'onblur':"this.placeholder = 'Enter Message'",
            'cols': "30",
            'rows': "9",
        }
    ))
    class Meta:
        model = Contact
        fields = ('nom', 'email', 'sujet', 'message')
