from django.urls import path
from supers.views import SuperheroDetailView

urlpatterns = [
    path(
        'superhero/<slug:slug>/',
        SuperheroDetailView.as_view(),
        name='superhero_detail'
    )
]
