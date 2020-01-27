from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm


# Create your views here.
# 在request对象（或者说HttpRequest对象）的诸多方法中，常用的有request.method、request.GET和request.POST。
def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # cd引用的是一个字典类型数据
            cd = login_form.cleaned_data
            # 其作用是检验此用户是否为本网站项目的用户，以及其密码是否正确。如果都对上号了，就返回User的一个实例对象，否则返回None。
            user = authenticate(username=cd['username'],password=cd['password'])
            if user:
                login(request, user)
                return HttpResponse('welcome You')
            else:
                return HttpResponse('sorry')
        else:
            return HttpResponse('Invalid login')

    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'account/login.html', {'form': login_form})