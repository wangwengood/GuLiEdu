from django import forms
from captcha.fields import CaptchaField

class UserRegisterForm(forms.Form):
    email = forms.EmailField(required=True, error_messages={
        'required': '用户名不能为空'
    })
    password = forms.CharField(required=True, min_length=4, max_length=10, error_messages={
        'required': '密码不能为空',
        'min_length': '密码最少4位',
        'max_length': '密码最大10位',
    })
    captcha = CaptchaField()
class UserLoginForm(forms.Form):
    email = forms.EmailField(required=True, error_messages={
        'required': '用户名不能为空'
    })
    password = forms.CharField(required=True, min_length=4, max_length=10, error_messages={
        'required': '密码不能为空',
        'min_length': '密码最少4位',
        'max_length': '密码最大10位',
    })
    captcha = CaptchaField()
