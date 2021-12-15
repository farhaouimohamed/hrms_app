from django.shortcuts import render

from hrmsapp.forms import RegistraionCollaboratorForm

# Create your views here.
def ajouter_collaborateur(request):
    if request.method == 'GET':
        form = RegistraionCollaboratorForm()
        context = {'form':form}
        return render(request,'addUser.html',context)
    if request.method == 'POST':
        form = RegistraionCollaboratorForm(request.POST)
        if form.is_valid():
            print("7777")
    return render(request,'addUser.html',{})
    
def demander_autorisation(request):
    return render(request,'developpeur/absence/demandeAbsence.html',{})