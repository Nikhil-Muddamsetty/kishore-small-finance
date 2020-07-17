from django.shortcuts import render
from django.views.generic import TemplateView

class IndexClassView(TemplateView):
    template_name = 'authentication/index.html'
