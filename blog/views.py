from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponse
from . import forms


# Create your views here.
def login(request):

    context = {}
    context["form"] = forms.Login
    if request.method == "POST":
        isExist = authenticate(username=request.POST.get("username"), password=request.POST.get("password")) 
        if isExist :
            context["error"] = "connection is sucessfull"
        else:
            context["error"] = "connection is failed"
    return render(request, "account/login.html", context)