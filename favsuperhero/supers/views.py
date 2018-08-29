from django.shortcuts import render
from django.views.generic.detail import DetailView
from supers.models import Superhero


class SuperheroDetailView(DetailView):
    template_name = 'supers/superhero_detail.html'
    model = Superhero
