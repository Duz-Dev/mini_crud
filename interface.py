import crud
import sys
from time import sleep
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

estado_anime = WordCompleter(["Finalizado","Emisión"], ignore_case=True)
generos = WordCompleter([
    "Shonen",
    "Shoujo",
    "Seinen",
    "Josei",
    "Kodomo",
    "Slice of Life",
    "Acción",
    "Aventura",
    "Romance",
    "Comedia",
    "Drama",
    "Fantasía",
    "Ciencia Ficción",
    "Horror",
    "Isekai"
    ], ignore_case=True)

def cls_line(line: int = 1):
    """
    ### Cls line. Limpieza de lineas de la terminal
    Argumentos:
            line (int, optional): Ingresa la cantidad de lineas a eliminar. Por defecto tiene valor de: 1.
    """
    for _ in range(line):
        # Mueve el cursor una línea arriba
        sys.stdout.write('\033[F')
        # Borra la línea actual
        sys.stdout.write('\033[K')
        # Asegura que los comandos se ejecuten inmediatamente
        sys.stdout.flush()

def Opciones(lim_inferior:int, lim_superior: int):
    """
    ### Opciones. depura la opción ingresada.

    Argumentos:
        lim_inferior (int): Numero que representa el valor mínimo que se espera de opciones
        lim_superior (int): El valor máximo que se espera de opciones.

    Retornar:
        op (int): El valor numérico dentro del rango pre-establecido.
    """
    #Depuramos opción
    try:
        while True:
            op = input(">> ")
            # VALIDAR SI ES UN NUMERO ENTRE 1 Y 5
            # VALIDAR QUE SEA UN NUMERO
            if (not op.isdigit()) or ( not  lim_inferior <= int(op) <= lim_superior):
                print(f"❌ Error: Debes ingresar un número válido entre {lim_inferior} y {lim_superior}.")
                sleep(1.5)
                cls_line(2)                
            else:
                #Convertimos str op a int 
                op = int(op)
                break
    except Exception as e:
        print("Ocurrió un error inesperado.", e)
    
    return op
        


def ver_anime():
    i = len(crud.biblioteca_anime)
    if i == 0:
        i = f" 0 "
    elif i < 9:
        i = f" 0{i}"
    else:
        i = f"{i}"
    print(
f"""
-----------------------------------------------------
|                 BIBLIOTECA ANIME                  |
-----------------------------------------------------
| CANTIDAD DE ANIMES EN LA BIBLIOTECA:  [ {i} ]     |
-----------------------------------------------------
|                     LISTADO                       |
 - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
)
    # crud.Read()
    return True if crud.Read() else False

def añadir_anime():
    print(
"""
-----------------------------------------------------
|                 AÑADE UN ANIME NUEVO              |
-----------------------------------------------------
Argumentos:
""")
    titulo = input("Titulo del anime:\n>> ")
    genero = prompt("Genero(s):\n>> ",completer=generos)
    anio = int(input("Año de publicación:\n>> "))
    estado = prompt("Estado de emisión:\n>> ", completer=estado_anime)
    episodios = int(input("Cantidad de episodios:\n>> "))
    sinopsis = input("Sinopsis:\n>> ")
    
    crud.Create(titulo,genero,anio,estado,episodios,sinopsis)
    return

def modificar_anime():
    print(
"""
-----------------------------------------------------
|             Modifica UN ANIME existente           |
-----------------------------------------------------
#--     Ingresa el [ID] del anime a modificar     --#
""")
    id = int(input(">> "))
    dict_anime = crud.Read(id,True) #Obtiene el diccionario del anime buscado
    if isinstance(dict_anime,dict):
        titulo = prompt("Titulo del anime:\n>>",default=dict_anime["titulo"])
        genero = prompt("Genero(s):\n>> ",completer=generos,default=dict_anime["genero"])
        anio = int(prompt("Año de publicación:\n>> ",default=str(dict_anime["año de lanzamiento"])))
        estado = prompt("Estado de emisión:\n>> ", completer=estado_anime, default=dict_anime["estado"])
        episodios = int(prompt("Cantidad de episodios:\n>> ",default=str(dict_anime["episodios"])))
        sinopsis = prompt("Sinopsis:\n>> ",default=dict_anime["sinopsis"])
        crud.Update(id,titulo,genero,anio,estado,episodios,sinopsis)
    else:
        print("Aviso. El ID ingresado no existe.")
        return False
    return True

def buscar_anime():
    i = len(crud.biblioteca_anime)
    if i == 0:
        i = f" 0 "
    elif i < 9:
        i = f" 0{i}"
    else:
        i = f"{i}"
    print(f"""
-----------------------------------------------------
|                 BIBLIOTECA ANIME                  |
-----------------------------------------------------
| CANTIDAD DE ANIMES EN LA BIBLIOTECA:  [ {i} ]     |
-----------------------------------------------------
|                    BÚSQUEDA                       |
 - - - - - - - - - - - - - - - - - - - - - - - - - -
Argumento: Ingresa el ID del anime a buscar
""")

    id = int(input(">> "))
    if not crud.Read(id):
        print("[AVISO]: La biblioteca esta vacia. Añade nuevos animes para visualizarlos")
        return False
    return True
    

def eliminar_anime():
    print("""
-----------------------------------------------------
|             ELIMINAR UN ANIME existente           |
-----------------------------------------------------
#--     Ingresa el [ID] del anime a Eliminar      --#
""")
    id = int(input(">> "))
    crud.Delete(id)