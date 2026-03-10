import requests

opcion = int(input('Introduce una opción (1-Crear fichero de persistencia; 2-Leer fichero de persistencia):'))

if opcion==1:
    reply = requests.get('http://localhost:8000/movies.json')
    status_code=reply.status_code
    if status_code==200:# La petición se ha atendido correctamente
        movie_list = reply.json() # movie_list es un array de diccionarios con datos de películas
        # print(type(movie_list)) # <class 'list'>
        for movie in movie_list:
            print(movie['title'])
            # Crear un objeto con cada película

            # Guardar en un shelve (bbdd) cada una de las películas. La clave será el título.

    else:
        print('Ha ocurrido un error:' + str(status_code))
elif opcion==2:
    while True:
        titulo = input('Introduce un título:')
        # Buscar la película en el fichero shelve y mostrar los datos por pantalla
        # Si no existe, se advierte y se pide otra película.
