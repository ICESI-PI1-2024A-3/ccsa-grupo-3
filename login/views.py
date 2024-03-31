from django.shortcuts import render, redirect
# Decorador
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.



@login_required

def index2(request):
        return render(request, 'base2.html')


@login_required
def indexHome(request):
    return render(request, 'baseAppLogin.html')





