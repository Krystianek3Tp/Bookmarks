from http.client import HTTPResponse

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

from Account.forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Uwierzytelnianie zakończyło się sukcesem")
                else:
                    return HttpResponse("Konto jest zablokowane")
        else:
            return HttpResponse("Nieprawidłowe dane")
    else:
        form = LoginForm()
    return render(request, template_name='account/login.html',context={'form':form})
