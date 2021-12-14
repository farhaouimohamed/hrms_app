from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout

from account.forms import AccountAuthenticationForm

def login_view(request):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("/home")
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
           email = request.POST['email']
           password = request.POST['password']
           print(email)
           print(password)
           user = authenticate(email=email, password=password) 
           
           if user:
               login(request,user)
               return redirect("/home")
        else:
            print("************")
    else:
        form = AccountAuthenticationForm()
    context['login_form'] = form
    return render(request, "login.html", context)
   

def pageAcceuil(request):
    return render(request, 'home.html',{})

def logout_view(request):
	logout(request)
	return redirect('/home')