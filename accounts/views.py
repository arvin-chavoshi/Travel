from django.shortcuts import render, redirect
from django.contrib.auth import login
from accounts.forms import SignUpForm
# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect("website:index")
    form = SignUpForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("website:index")
    return render(request, "registration/signup.html", {"form" : form})