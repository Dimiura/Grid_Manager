from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.
def register_view (request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('content')
    else:
            user_form = UserCreationForm()
    return render(request, 'register.html', {'user_form': user_form}) 


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'content') 
            return redirect(next_url)
        else:
            error_message = "Credenciais inválidas. Tente novamente."
            login_form = AuthenticationForm()
            return render(request, 'login.html', {'login_form': login_form, 'error_message': error_message})
    else:
        login_form = AuthenticationForm()
        return render(request, 'login.html', {'login_form': login_form})
     

def logout_view(request):
    logout(request)
    return redirect('welcome')