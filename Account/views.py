from django.shortcuts import render

from Account.forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        pass
    else:
        form = LoginForm()
    return render(request, template_name='account/login.html',context={'form':form})
