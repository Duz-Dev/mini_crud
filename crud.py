
#!mini_crud

biblioteca_anime = []

ids = [] #recopila los ids ya creados
count = 0 #LLevar un conteo del id del ultimo anime creado.

def Create(titulo:str,genero:str,anio:int,estado:str,episodios:int,sinopsis:str) -> None:
    """
    ### Create. Añade los elementos
    Argumentos:
        titulo (str): titulo del anime
        genero (str): genero(s) de la obra
        anio (int): Año de publicación
        estado (str): Estado de emisión
        episodios (int): Cantidad de episodios
        sinopsis (str): Breve descripción del anime

    Returns:
        None
    """
    global count
    
    anime = {}
    
    anime["ID"] = count
    anime["titulo"] = titulo
    anime["genero"] = genero
    anime["año de lanzamiento"] = anio
    anime["estado"] = estado
    anime["episodios"] = episodios
    anime["sinopsis"] = sinopsis
    
    #Añadiendo elemento a la biblioteca
    biblioteca_anime.append(anime)

    #Añado el id a la lista de ids
    ids.append(count)
    
    #Aumentado el contador:
    count += 1
    return None

def Read(id=None,dict: bool = False):
    
    if not(biblioteca_anime):#Verifica si existe mas de 0 elementos, si no ejecuta lo sig:
        #print("[AVISO]: La biblioteca esta vacia. Añade nuevos animes para visualizarlos")
        return False
    elif id is None: #Significa que la persona no ingreso un id y por defecto le mostrara toda la lista.
        for i in range(len(biblioteca_anime)):
            if i != 0:
                print("---"*25)
                
            for clave,valor in biblioteca_anime[i]. items():
                print(f"{clave}: {valor}")
        return True
    else: #Entonces la persona si ingreso el id
        if not comprobar_ids(id):
            return False
            
        if dict: #Si la persona ingreso True en el parámetro dict, devele el diccionario en este caso
            return biblioteca_anime[id]
        else:# De lo contrario si colo false u otro dato imprimirá dicho diccionario
            for clave,valor in biblioteca_anime[id].items():
                print(f"{clave}: {valor}")
            return True
    

def comprobar_ids(id: int) -> bool:
    if not(id in ids):
            print("[AVISO]: El Anime buscado no existe o fue eliminado. ID disponibles:",str(ids))
            return False
    else:
        return True


def Update(id:int,titulo:str,genero:str,anio:int,estado:str,episodios:int,sinopsis:str) -> None:

    anime = biblioteca_anime[id]
    #Actualizando elementos
    anime["titulo"] = titulo
    anime["genero"] = genero
    anime["año de lanzamiento"] = anio
    anime["estado"] = estado
    anime["episodios"] = episodios
    anime["sinopsis"] = sinopsis
    
    return


def Delete(id:int):
    if comprobar_ids(id):
        dato = biblioteca_anime[id]
        biblioteca_anime.remove(dato)
        return True
    return False


