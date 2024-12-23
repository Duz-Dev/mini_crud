# CRUD de Animes en Python

Este proyecto es una simulación de un sistema CRUD (Create, Read, Update, Delete) desarrollado en Python 3.12.3. La aplicación permite gestionar una lista de animes mediante una interfaz interactiva en la terminal, con soporte para autosugerencias gracias a la librería `prompt_toolkit`.

## Características

- **Crear**: Añade nuevos animes a la lista con los campos especificados.
- **Leer**: Visualiza la lista completa de animes o busca animes específicos.
- **Actualizar**: Modifica la información de animes existentes.
- **Eliminar**: Borra animes de la lista.
- **Interfaz interactiva**: Utiliza `prompt_toolkit` para mejorar la experiencia en la terminal con autosugerencias.

## Estructura de Datos de un Anime

Cada anime se representa como un diccionario con los siguientes campos:

```python
{
    "titulo": str,       # Título del anime
    "genero": str,       # Género(s) de la obra
    "anio": int,         # Año de publicación
    "estado": str,       # Estado de emisión (por ejemplo, "En emisión", "Finalizado")
    "episodios": int,    # Cantidad de episodios
    "sinopsis": str      # Breve descripción del anime
}
```

## Requisitos

Para ejecutar este proyecto, asegúrate de tener instalado:

- Python 3.12.3
- Librerías adicionales: `prompt_toolkit`

Puedes instalar las dependencias ejecutando:

```bash
pip install prompt_toolkit
```

## Uso

1. Clona este repositorio:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_PROYECTO>
   ```

2. Ejecuta el script principal:

   ```bash
   python main.py
   ```

3. Sigue las instrucciones en la terminal para interactuar con el CRUD.

## Funcionalidades

### Crear

Añade un nuevo anime a la lista. Los campos requeridos son:

- `titulo` (str): Título del anime.
- `genero` (str): Género(s) de la obra.
- `anio` (int): Año de publicación.
- `estado` (str): Estado de emisión (por ejemplo, "En emisión", "Finalizado").
- `episodios` (int): Cantidad de episodios.
- `sinopsis` (str): Breve descripción del anime.

### Leer

- Muestra la lista completa de animes.
- Permite buscar animes por título, género o año.

### Actualizar

- Edita los campos de un anime específico.

### Eliminar

- Elimina un anime de la lista.

### Interfaz interactiva

- Proporciona autosugerencias mientras introduces datos mediante `prompt_toolkit`.

## Opciones

```bash
-----------------------------------------------------
|                 BIBLIOTECA ANIME                  |
-----------------------------------------------------
| OPCIONES |                FUNCIONES               |
-----------------------------------------------------
|   1      | [Ver] lista actual de animes           |
|   2      | [AÑADIR] anime a la biblioteca         |
|   3      | [MODIFICAR] anime de la biblioteca     |
|   4      | [BUSCAR] anime de la biblioteca        |
|   5      | [ELIMINAR] anime de la biblioteca      |
|   6      | [SALIR] Salir del programa             |
-----------------------------------------------------


```

El seguimiento de los animes se hace mediante el dato ["ID"], y los animes se van creando desde el numero cero en adelante.
Por ende, si deseamos buscar el primer anime debemos escribir en en el campo de busqueda como en la opcion 4 el id "0".
