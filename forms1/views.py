from django.shortcuts import render, redirect

from forms1.form import UserForm, LoginUserForm
from forms1.models import User


def index(request):
    if request.method == 'GET':
        user = LoginUserForm()
        return render(request, 'index1.html', locals())
    elif request.method == 'POST':
        user = LoginUserForm(request.POST)
        if user.is_valid():
            # 做模型层相关的操作
            return redirect('/')
        else:
            return render(request, 'index1.html', locals())
