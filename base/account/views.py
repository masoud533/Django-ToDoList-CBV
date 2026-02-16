from django.shortcuts import render

from django.contrib.auth.views import LoginView
from .mixins import RedirectAuthenticatedUserMixin

class CustomLoginView(RedirectAuthenticatedUserMixin, LoginView):
    template_name = "registration/login.html"