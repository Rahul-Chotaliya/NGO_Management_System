from random import randrange

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import redirect

from core.models import Otp


# def common_function():
