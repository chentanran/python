from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm, UserProfileForm, UserInfoForm, UserForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile, UserInfo
from django.contrib.auth.models import User
from django.views.decorators.clickjacking import xframe_options_exempt

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


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid()*userprofile_form.is_valid():
            new_user = user_form.save(commit=False) # 结果是数据并没有被保存到数据库，而仅生成了一个数据对象
            new_user.set_password(user_form.cleaned_data['password']) # 设置了该数据对象的密码
            new_user.save() # 数据保存到数据库中
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            return HttpResponse('success')
        else:
            return HttpResponse('not register')
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request, 'account/register.html', {'form': user_form, 'profile': userprofile_form})

@login_required()
def myself(request):
    userprofile = UserProfile.objects.get(user=request.user) if hasattr(request.user, 'userprofile') else UserProfile.objects.create(user=request.user)
    userinfo = UserInfo.objects.get(user=request.user) if hasattr(request.user, 'userinfo') else UserInfo.objects.create(user=request.user)
    return render(request, 'account/myself.html', {'user': request.user, 'userinfo':userinfo, 'userprofile':userprofile})


@login_required(login_url='/account/login/')
def myself_edit(request):
    userprofile = UserProfile.objects.get(user=request.user) if hasattr(request.user, 'userprofile') else UserProfile.objects.create(user=request.user)

    userinfo = UserInfo.objects.get(user=request.user) if hasattr(request.user, 'userinfo') else UserInfo.objects.create(user=request.user)
    if request.method == "POST":
        user_form = UserForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        userinfo_form = UserInfoForm(request.POST)
        if user_form.is_valid() * userprofile_form.is_valid()*userinfo_form.is_valid():
            user_cd = user_form.cleaned_data
            userprofile_cd = userprofile_form.cleaned_data
            userinfo_cd = userinfo_form.cleaned_data
            request.user.email = user_cd['email']
            userprofile.birth = userprofile_cd['birth']
            userprofile.phone = userprofile_cd['phone']
            userinfo.school = userinfo_cd['school']
            userinfo.company = userinfo_cd['company']
            userinfo.profession = userinfo_cd['profession']
            userinfo.address = userinfo_cd['address']
            userinfo.aboutme = userinfo_cd['aboutme']
            request.user.save()
            userprofile.save()
            userinfo.save()
        return HttpResponseRedirect('/account/my-information/')  # ②
    else:
        user_form = UserForm(instance=request.user)
        userprofile_form = UserProfileForm(initial={"birth": userprofile.birth,
                                                    "phone": userprofile.phone})
        userinfo_form = UserInfoForm(initial={"school": userinfo.school,
                                              "company": userinfo.company,
                                              "profession": userinfo.profession,
                                              "address": userinfo.address,
                                              "aboutme": userinfo.aboutme})
        return render(request, "account/myself_edit.html",
                      {"user_form": user_form,
                       "userprofile_form": userprofile_form,
                       "userinfo_form": userinfo_form})


@xframe_options_exempt
def my_image(request):
    if request.method == 'POST':
        img = request.POST['img']
        userinfo = UserInfo.objects.get(user=request.user.id)
        userinfo.photo = img
        userinfo.save()
        return HttpResponse('1')
    else:
        return render(request, 'account/imagecrop.html',)



