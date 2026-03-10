import requests
import shelve

class Movie:
    pass

opcion = int(input('Introduce una opción (1-Crear fichero de persistencia; 2-Leer fichero de persistencia):'))

if opcion==1:
    peliculas = shelve.open('peliculas.sqlite', flag='c')
    reply = requests.get('http://localhost:8000/movies.json')
    status_code=reply.status_code
    if status_code==200:# La petición se ha atendido correctamente
        movie_list = reply.json() # movie_list es un array de diccionarios con datos de películas
        # print(type(movie_list)) # <class 'list'>
        for movie in movie_list:
            # Crear un objeto con cada película
            new_movie = Movie()
            new_movie.__dict__ = movie
            # Guardar en un shelve (bbdd) cada una de las películas. La clave será el título.
            peliculas[new_movie.title]=new_movie.__dict__
            print(f'Película {new_movie.title} almacenada')
    else:
        print('Ha ocurrido un error:' + str(status_code))
    peliculas.close()
elif opcion==2:
    peliculas = shelve.open('peliculas.sqlite', flag='r')
    while True:
        titulo = input('Introduce un título (Pulsa ENTER para salir):')
        if titulo=='': break
        # Buscar la película en el fichero shelve y mostrar los datos por pantalla
        if titulo in peliculas:
            pelicula_encontrada = Movie()
            pelicula_encontrada.__dict__=peliculas[titulo]
            for k, v in pelicula_encontrada.__dict__.items():
                print(f'{k}:{v}')
        else:
            print('No existe esa película, introduce otro título')
        # Si no existe, se advierte y se pide otra película.
    peliculas.close()