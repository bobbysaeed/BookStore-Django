from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePageview(TemplateView):
    template_name = 'home.html'