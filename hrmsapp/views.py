from enum import auto
from django.http.response import JsonResponse
from django.shortcuts import redirect, render

from hrmsapp.forms import AbsenceModelForm, RegistraionCollaboratorForm, AccountAuthenticationForm
from hrmsapp.models import Absence, Collaborateur, Mail
from django.contrib.auth import login, authenticate, logout

###################################################################################################### Login


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        if user.is_developper == True:
            return redirect("/developpeur/profile")
        elif user.is_responsable == True:
            return redirect("/responsable/profile")
        elif user.is_admin == True:
            return redirect("/admin_iga/profile")
    else:
        if request.POST:
            form = AccountAuthenticationForm(request.POST)
            if form.is_valid():
                email = request.POST['email']
                password = request.POST['password']
                user = authenticate(email=email,password=password)
                if user:
                    login(request,user)
                    if user.is_developper == True:
                        return redirect("/developpeur/liste_autorisations_validees")
                    elif user.is_responsable == True:
                        return redirect("/responsable/liste_collaborateur")
                    elif user.is_admin == True:
                        return redirect("/admin_iga/profile")
                else:
                    form = AccountAuthenticationForm()
                    context['login_form'] = form
                    return render(request,'login.html',context)
            else:
                print("form is invalid")
                form = AccountAuthenticationForm()
                context['login_form'] = form
                return render(request,'login.html',context)
        else:
            form = AccountAuthenticationForm()
            context['login_form'] = form
            return render(request,'login.html',context)

def logout_view(request):
    logout(request)
    return redirect('/login')

###################################################################################################### Admin

def profil_admin(request):
    return render(request,'admin_iga/profil.html',{})

def ajouter_collaborateur(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        if user.is_admin == True:
            if request.method == 'GET':
                form = RegistraionCollaboratorForm()
                responsables = Collaborateur.objects.filter(is_responsable=True)
                context = {'form':form,'responsables':responsables}
                return render(request,'admin_iga/addCollaborateur.html',context)
            if request.method == 'POST':
                form = RegistraionCollaboratorForm(request.POST)    
                if form.is_valid():
                    id_responsable=request.POST['inputNomResponsable']
                    print(id_responsable)
                    collaborateur=Collaborateur()
                    collaborateur=form.save(commit=False)
                    collaborateur.responsable_id=id_responsable
                    collaborateur.save()
            return redirect("/admin_iga/liste_collaborateurs")
        else:
            return JsonResponse("Vous n'avez pas d'accés sur cette page !!!!",safe=False)
    else:
        return render(request,'login.html',context)

def list_collaborateur_admin(request):
    collaborateurs = Collaborateur.objects.all()
    return render(request,'admin_iga/listCollaborateurs.html',{"collaborateurs":collaborateurs})


###################################################################################################### Responsable

def profil_responsable(request):
    return render(request,'responsable/profil.html',{})


def list_collaborateur_resp(request):
    user=request.user
    if user.is_authenticated:
        if user.is_responsable == True:
            collaborateurs = Collaborateur.objects.filter(responsable_id=user.id)
            return render(request,'responsable/listCollaborateurs.html',{"collaborateurs":collaborateurs})
        else:
            return JsonResponse("Vous n'avez pad d'acces sur cette page !!!!!!!!",safe=False)
    else:
        return render(request,"login.html",{})
    

def list_autorisations_resp(request):
    user = request.user
    if user.is_authenticated:
        if user.is_responsable == True:
            user=request.user
            autorisations=Absence.objects.filter(responsable_id=user.id)
            return render(request,'responsable/listAutorisations.html',{"autorisations":autorisations})
        else:
            return JsonResponse("Vous n'avez pad d'acces sur cette page !!!!!!!!",safe=False)
    else:
        return render(request,"login.html",{})

def list_autorisations_validees_resp(request):
    user = request.user
    if user.is_authenticated:
        if user.is_responsable == True:
            user=request.user
            collaborateurs = Collaborateur.objects.filter(responsable_id=user.id)
            autorisations = []
            for collaborateur in collaborateurs:
                autorisations.extend(list(Absence.objects.filter(developpeur_id=collaborateur.id).filter(statut="validee")))
            return render(request,'responsable/list_autorisations_validees.html',{"autorisations":autorisations})
        else:
            return JsonResponse("Vous n'avez pad d'acces sur cette page !!!!!!!!",safe=False)
    else:
        return render(request,"login.html",{})

def list_autorisations_en_cours_resp(request):
    user = request.user
    if user.is_authenticated:
        if user.is_responsable == True:
            user=request.user
            collaborateurs = Collaborateur.objects.filter(responsable_id=user.id)
            autorisations = []
            for collaborateur in collaborateurs:
                autorisations.extend(list(Absence.objects.filter(developpeur_id=collaborateur.id).filter(statut="en_cours")))
            return render(request,'responsable/list_autorisations_en_cours.html',{"autorisations":autorisations})
        else:
            return JsonResponse("Vous n'avez pad d'acces sur cette page !!!!!!!!",safe=False)
    else:
        return render(request,"login.html",{})

def list_autorisations_non_validees_resp(request):
    user = request.user
    if user.is_authenticated:
        if user.is_responsable == True:
            user=request.user
            collaborateurs = Collaborateur.objects.filter(responsable_id=user.id)
            absences = []
            for collaborateur in collaborateurs:
                absences.extend(list(Absence.objects.filter(developpeur_id=collaborateur.id).filter(statut="non_validee")))
            return render(request,'responsable/list_autorisations_non_validees.html',{"absences":absences})
        else:
            return JsonResponse("Vous n'avez pad d'acces sur cette page !!!!!!!!",safe=False)
    else:
        return render(request,"login.html",{})



def valider_autorisation(request,pk):
    user = request.user
    if user.is_authenticated:
        if user.is_responsable == True:
            if request.method == 'GET':
                collaborateurs=Collaborateur.objects.filter(responsable_id=user.id)
                autorisation=Absence.objects.get(id=pk)
                mail=autorisation.mail_set.all()
                return render(request,'responsable/detail_autorisation.html',{"collaborateurs":collaborateurs,"mail":mail,"autorisation":autorisation})
            if request.method == 'POST':
                print()
        else:
            return JsonResponse("Vous n'avez pad d'acces sur cette page !!!!!!!!",safe=False)
    else:
        return render(request,"login.html",{})
            
    
###################################################################################################### Developpeur

def demander_autorisation(request):
    user = request.user
    if user.is_authenticated:
        if user.is_developper == True:
            if request.method == 'GET':
                form = AbsenceModelForm()
                context = {'form':form}
                return render(request,'developpeur/demande_autorisation.html',context)
            if request.method == 'POST':
                form = AbsenceModelForm(request.POST)
                if form.is_valid():
                    autorisation = form.save(commit=False)
                    titre = request.POST['inputTitre']
                    collaborateur = Collaborateur.objects.get(email=user.email)
                    responsable = Collaborateur.objects.get(id=collaborateur.responsable_id)
                    destinataire = responsable.email
                    contenu="bla bla bla"+request.POST['date_debut']+"bla bla bla"+request.POST['date_fin']+"bla bla bla"+request.POST['nbr_jours']+"bla bla bla"+request.POST['codification']
                    mail = Mail()
                    mail.objet=titre
                    mail.body=contenu
                    mail.email_source=user.email
                    mail.email_destination=destinataire
                    autorisation.developpeur=collaborateur
                    autorisation.save()
                    mail.absence=autorisation
                    mail.save()
                    return redirect("/developpeur/liste_autorisations_validees")
                else:
                    print("Form is not valid")
                    context = {'form':form}
                    return render(request,'developpeur/demande_autorisation.html',context)
        else:
            return JsonResponse("Vous n'avez pad d'acces sur cette page !!!!!!!!",safe=False)
    else:
        return render(request,"login.html",{})

def list_autorisations_validees(request):
    user = request.user
    if user.is_authenticated:
        if user.is_developper == True:
            autorisations = Absence.objects.filter(developpeur_id=user.id).filter(statut="validee")
            return render(request,"developpeur/list_autorisations_validees.html",{'autorisations':autorisations})
        else:
            return JsonResponse("Vous n'avez pad d'acces sur cette page !!!!!!!!",safe=False)
    else:
        return render(request,"login.html",{})

def list_autorisations_non_validees(request):
    user = request.user
    if user.is_authenticated:
        if user.is_developper == True:
            autorisations = Absence.objects.filter(developpeur_id=user.id).filter(statut="non_validee")
            return render(request,"developpeur/list_autorisations_non_validees.html",{'autorisations':autorisations})
        else:
            return JsonResponse("Vous n'avez pad d'acces sur cette page !!!!!!!!",safe=False)
    else:
        return render(request,"login.html",{})

def list_autorisations_en_cours(request):
    user = request.user
    if user.is_authenticated:
        if user.is_developper == True:
            autorisations = Absence.objects.filter(developpeur_id=user.id).filter(statut="en_cours")
            return render(request,"developpeur/list_autorisations_en_cours.html",{'autorisations':autorisations})
        else:
            return JsonResponse("Vous n'avez pad d'acces sur cette page !!!!!!!!",safe=False)
    else:
        return render(request,"login.html",{})
        

def detail_autorisation(request,pk):
    user = request.user
    if user.is_authenticated:
        if user.is_developper == True:
            autorisation = Absence.objects.get(id=pk)
            mail = Mail.objects.get(absence_id=autorisation.id)
            return render(request,"developpeur/detail_autorisation.html",{'autorisation':autorisation,'mail':mail})
        else:
            return JsonResponse("Vous n'avez pad d'acces sur cette page !!!!!!!!",safe=False)
    else:
        return render(request,"login.html",{})



######################################################################################################

def addAdminUser(request):
    if request.method == 'GET':
        form = RegistraionCollaboratorForm()
        context = {'form':form}
        return render(request,'addUser.html',context)
    if request.method == 'POST':
        form = RegistraionCollaboratorForm(request.POST)
        if form.is_valid():
            form.save()
    form = RegistraionCollaboratorForm()
    context = {'form':form}
    return render(request,'addUser.html',context)