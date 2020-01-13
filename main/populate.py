from main.models import Puntuacion, Anime

path = "animeRS_Dataset"

def deleteTables():  
    Puntuacion.objects.all().delete()
    Anime.objects.all().delete()

    
    
def populateAnime():
    print("Loading anime...")
        
    lista=[]
    fileobj=open(path+"/anime.csv", "r",encoding= 'ISO-8859-1')
    for line in fileobj.readlines():
        rip = line.split(';')
        if len(rip) != 5:
            continue
        lista.append(Anime(id_anime=int(rip[0].strip()), titulo=rip[1].strip()), generos = rip[2].strip(), formato_emision= rip[3].strip(), numero_episodios=int(rip[4].strip()))
    fileobj.close()
    Anime.objects.bulk_create(lista)  # bulk_create hace la carga masiva para acelerar el proceso
    
    print("Anime inserted: " + str(Anime.objects.count()))
    print("---------------------------------------------------------")
    
    

def populatePuntuacion():
    print("Loading Ratings...")
        
    lista=[]
    fileobj=open(path+"/ratings.cvs", "r",encoding= 'ISO-8859-1')
    for line in fileobj.readlines():
        rip = line.split(';')
        if len(rip) != 3:
            continue
        lista.append(Puntuacion(id_usuario=int(rip[0].strip()), id_anime=Anime.objects.get(rip[1].strip()), puntuacion= int(rip[2].strip())))
    fileobj.close()
    Puntuacion.objects.bulk_create(lista)
    
    print("Ratings inserted: " + str(Puntuacion.objects.count()))
    print("---------------------------------------------------------")


    
    
def populateDatabase():
    deleteTables()
    populateAnime()
    populatePuntuacion()
    print("Finished database population")
    
if __name__ == '__main__':
    populateDatabase()