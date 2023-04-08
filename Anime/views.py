from django.shortcuts import render

from .models import Anime as an

# Create your views here.
def Anime(request):
    searchTerm = request.GET.get('searchAnime')
    if searchTerm: 
       animes = an.objects.filter(title__icontains=searchTerm) 
    else: 
        animes = an.objects.all()
    return render(request, 'anime.html', {'searchTerm':searchTerm, 'Animes': animes})

def about(request):
    return render(request, 'about.html')

