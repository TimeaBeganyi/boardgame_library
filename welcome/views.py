from django.shortcuts import render
from django.views.generic import TemplateView


class WelcomeTemplateView(TemplateView):
    template_name = "welcome/welcome.html"
