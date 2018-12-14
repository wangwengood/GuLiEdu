from django.shortcuts import render, redirect, reverse
from .forms import UserRegisterForm, UserLoginForm
from django.db.models import Q
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request, 'index.html')
def login_register(request):
    if request.method == 'GET':
        user_register_form = UserRegisterForm()
        return render(request, 'register.html', {
            'user_register_form': user_register_form
        })
    else:
        user_register_form = UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            email = user_register_form.cleaned_data['email']
            password = user_register_form.cleaned_data['password']
            user_list = UserProfile.objects.filter(Q(username=email)|Q(email=email))
            if user_list:
                return render(request, 'register.html', {
                    'msg': '用户已经存在'
                })
            else:
                a = UserProfile()
                a.email = email
                a.username = email
                a.set_password(password)
                a.save()
                a.send_mail_code(email,)
                # return redirect(reverse('index'))
        else:
            return render(request, 'register.html', {
                'user_register_form': user_register_form
            })
def my_login(request):
    if request.method == 'GET':
        user_login_form = UserLoginForm()
        return render(request, 'login.html', {
            'user_login_form': user_login_form
        })
    else:

        user_login_form = UserLoginForm(request.POST)
        if user_login_form.is_valid():
            username = user_login_form.cleaned_data['email']
            password = user_login_form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user:
                if user.is_start:
                    login(request, user)
                    return redirect(reverse('index'))
                else:
                    return HttpResponse('请去你的邮箱激活邮件')
            else:
                return render(request, 'login.html', {
                    'msg': '密码或者用户名有错误'
                })
        else:
            return render(request, 'login.html', {
                'user_login_form': user_login_form
            })
def my_logon(request):
    logout(request)
    return redirect(reverse('index'))



























'''
 :param request:
 :return:


    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        user_register_form = UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            email = user_register_form.cleaned_data['email']
            password = user_register_form.cleaned_data['password']

            user_list = UserProfile.objects.filter(Q(username=email)|Q(email=email))
            if user_list:
                return render(request, 'register.html', {
                    'msg': '用户已经存在'
                })
            else:
                a = UserProfile()
                a.username = email
                a.set_password(password)
                a.save()
                return redirect(reverse('index'))
        else:
            return render(request, 'register.html', {
                'user_register_form': user_register_form
            })
'''
