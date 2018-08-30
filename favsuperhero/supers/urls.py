from django.urls import path
from supers.views import SuperheroDetailView, SuperheroPlayerListView

urlpatterns = [
    path(
        'superhero/<slug:slug>/',
        SuperheroDetailView.as_view(),
        name='superhero_detail'
    ),
    path(
        'superheroes_by_player/<player>/',
        SuperheroPlayerListView.as_view(),
        name='superhero_list_by_player'
    )
]
