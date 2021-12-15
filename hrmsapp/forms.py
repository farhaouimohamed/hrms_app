from django import forms
from django.contrib.auth.forms import UserCreationForm
from hrmsapp.models import Collaborateur

class RegistraionCollaboratorForm(UserCreationForm):

    class Meta:
        model = Collaborateur
        fields = ('email','password1','password2', 'nom','prenom','matricule','service','fonction','date_debut_fonction','date_fin_fonction','is_responsable','is_developper')
        widgets = {
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),
			'password2':forms.PasswordInput(attrs={'class':'form-control'}),
            'nom':forms.TextInput(attrs={'class':'form-control'}),
            'prenom':forms.TextInput(attrs={'class':'form-control'}),
            'matricule':forms.TextInput(attrs={'class':'form-control'}),
            'service':forms.TextInput(attrs={'class':'form-control'}),
            'fonction':forms.TextInput(attrs={'class':'form-control'}),
            'date_debut_fonction':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'date_fin_fonction':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'is_responsable':forms.CheckboxInput(attrs={'class':'form-control'}),
            'is_developper':forms.CheckboxInput(attrs={'class':'form-control'}),
			
        }
