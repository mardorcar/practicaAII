from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator,URLValidator


class Anime(models.Model):
    id_anime = models.TextField(primary_key=True)
    titulo = models.CharField(max_length=100)
    generos = models.CharField(max_length=50)
    formato_emision = models.CharField(max_length=50)
    numero_episodios = models.IntegerField()
    def __str__(self):
        return self.titulo  

    
class Puntuacion(models.Model):
    id_usuario = models.TextField(primary_key=True)
    id_anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    puntuacion = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    def __str__(self):
        return str(self.puntuacion)