from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)

        if form.is_valid():
            form.save()
            return redirect("/login")
        
    else:
        form = RegisterForm()

    return render(response, "register_account/register_account.html", {
        "register_form" : form
    })

def logout(request):
    return render(request, "register_account/logout.html")