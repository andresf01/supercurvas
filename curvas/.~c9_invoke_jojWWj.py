from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, TemplateView

# Create your views here.
class index(TemplView):
    t = 'index.html'
