from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from supers.models import Superhero, User


class SuperheroDetailView(DetailView):
    template_name = 'supers/superhero_detail.html'
    model = Superhero


class SuperheroPlayerListView(ListView):
    template_name = 'supers/superhero_list.html'
    model = Superhero

    def get(self, request, *args, **kwargs):
        self.player = kwargs['player']
        return super().get(self, request, *args, **kwargs)

    def get_queryset(self):
        player = User.objects.filter(username=self.player)[0]
        return Superhero.objects.filter(player=player)
