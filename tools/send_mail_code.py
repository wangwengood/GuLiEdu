from users.models import EmailVerifyCode
from django.core.mail import send_mail
from random import choice
def get_random_code(code_length):
    code_course = '123456789qwertyuiopasdfghjklzxcvbnmQEWRTYUODSAHFGLJKCZNVBMP'
    code = ''
    for i in range(0, len(code_course)-1):
        code += choice(code_course)
    return code

def send_mail_code(email, type):
    a = EmailVerifyCode()
    a.email = email
    a.send_type = type
    a.code = get_random_code(6)