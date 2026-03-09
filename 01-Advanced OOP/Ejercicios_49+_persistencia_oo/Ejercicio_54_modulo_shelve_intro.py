import shelve

equipo = shelve.open('equipo.shv', flag='c')

equipo['1']={'posicion':'portero', 'nombre':'Paco'}
equipo['2']={'posicion':'lateral derecho', 'nombre':'Miguel'}
equipo['3']={'posicion':'lateral izquierdo', 'nombre':'Antonio'}
equipo['4']={'posicion':'central', 'nombre':'Ricardo'}

equipo.close()