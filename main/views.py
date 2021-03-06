from main.models import Anime, Puntuacion
from django.shortcuts import render, get_object_or_404
from main.populate import populateDatabase
from main.forms import animeGenreForm, animeForm
import shelve
from main.recommendations import  transformPrefs, calculateSimilarItems, getRecommendations, getRecommendedItems, topMatches

    
#  CONJUNTO DE VISTAS

def index(request): 
    return render(request,'index.html')

def populateDB(request):
    populateDatabase() 
    return render(request,'populate.html')

# APARTADO A
def animes_genero(request):
    formulario = animeGenreForm()
    animes = None
    if request.method == 'POST':
        formulario = animeGenreForm(request.POST)
        print(formulario.is_valid())
        if formulario.is_valid():
            print(1)
            animes = Anime.objects.filter(generos__icontains=formulario.cleaned_data['genero'])
            
    return render(request, 'animes_genero.html', {'formulario':formulario, 'animes':animes})

# APARTADO B
def mejores_animes(request):
    cuenta = [0,0]
    lista = [0,0]
    animes = Anime.objects.all()
    for a in animes:
        puntuacion = Puntuacion.objects.filter(puntuacion=10).filter(id_anime = a).count()
        if (puntuacion > cuenta[1]):
            cuenta[1] = puntuacion
            lista[1] = a
        elif (puntuacion > cuenta[0]):
            cuenta[0] = puntuacion
            lista[0] = a
            cuenta.sort(reverse=True)
    return render(request,'mejores_animes.html', {'lista':lista})

def recomendar(request):
    return None


def similarAnimes(request):
    anime = None
    if request.method=='GET':
        form = animeForm(request.GET, request.FILES)
        if form.is_valid():
            id_anime = form.cleaned_data['id']
            anime = get_object_or_404(Anime, pk=id_anime)
            shelf = shelve.open("dataRS.dat")
            ItemsPrefs = shelf['ItemsPrefs']
            shelf.close()
            recommended = topMatches(ItemsPrefs, int(id_anime),n=1)
            animes = []
            similar = []
            for re in recommended:
                animes.append(Anime.objects.get(pk=re[1]))
                similar.append(re[0])
            items= zip(films,similar)
            return render(request,'similarAnimes.html', {'anime': anime,'animes': items})
    form = animeForm()
    return render(request,'search_film.html', {'form': form})
