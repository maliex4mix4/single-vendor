from django.shortcuts import render

from .models import Users, Cart
from .forms import LoginForm, RegisterForm

def loginDisp(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form": form
    }
    return render(request, "default/login.html", context=context)

def registerDisp(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form": form
    }
    return render(request, "", context=context)

def index(request):
    context = {}
    return render(request, 'default/index.html', context=context)