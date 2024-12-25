from django.shortcuts import render
from .models import Ghibli_Movies
from django.db.models import Q

def home_view(request):
    search = request.GET.get('Search', '').strip()
    if search:
        gbh_movies = Ghibli_Movies.objects.filter(
            Q(title__icontains=search)
        )
    else:
        gbh_movies = Ghibli_Movies.objects.all()

    return render(request, 'home/home.html', {'gbh_movies': gbh_movies, 'search': search})
