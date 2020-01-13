from main.models import Anime, Puntuacion
from django.shortcuts import render, get_object_or_404
from main.populate import populateDatabase
from main.forms import animeGenreForm, animeForm
    
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
    puntuacion = Puntuacion.objects.filter(puntuacion=10)
    animes = Anime.objects.annotate(notas=Sum(puntuacion)).order_by('-notas')[:2]
    return render(request,'mejores_animes.html', {'animes':animes})

# APARTADO C
def similar_anime(request):
    anime = None
    if request.method=='GET':
        form = FilmForm(request.GET, request.FILES)
        if form.is_valid():
            idFilm = form.cleaned_data['id']
            film = get_object_or_404(Film, pk=idFilm)
            shelf = shelve.open("dataRS.dat")
            ItemsPrefs = shelf['ItemsPrefs']
            shelf.close()
            recommended = topMatches(ItemsPrefs, int(idFilm),n=3)
            films = []
            similar = []
            for re in recommended:
                films.append(Film.objects.get(pk=re[1]))
                similar.append(re[0])
            items= zip(films,similar)
            return render(request,'similarFilms.html', {'film': film,'films': items})
    form = FilmForm()
    return render(request,'search_film.html', {'form': form})

def recomendar(request):
    return None