from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register_view (request):
    if request.metod == "POST":
        user_form = UserCreationForm(request.POST)
        return render(request, 'register.html', {'user_form': user_form}) 