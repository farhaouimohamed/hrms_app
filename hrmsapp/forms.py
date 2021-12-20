from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from hrmsapp.models import Absence, Collaborateur
from django.contrib.auth import authenticate

class RegistraionCollaboratorForm(UserCreationForm):

    class Meta:
        model = Collaborateur
        fields = ('email','password1','password2', 'nom','prenom','matricule','service','fonction','date_debut_fonction','date_fin_fonction','is_responsable','is_developper','is_admin')
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
            'is_admin':forms.CheckboxInput(attrs={'class':'form-control'}),

        }


class AbsenceModelForm(forms.ModelForm):
    class Meta:
        model = Absence
        fields = ('date_debut','date_fin','codification','nature','nbr_jours')
        widgets = {
            'date_debut':forms.DateInput(attrs={'class':'form-control','type':'datetime-local'}),
            'date_fin':forms.DateInput(attrs={'class':'form-control','type':'datetime-local'}),
            'codification':forms.TextInput(attrs={'class':'form-control'}),
            'nature':forms.TextInput(attrs={'class':'form-control'}),
            'nbr_jours':forms.NumberInput(attrs={'class':'form-control'}),
        }

class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(label='Adresse mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))

	class Meta:
		model = Collaborateur
		fields = ('email', 'password')

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid login")
