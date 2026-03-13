# Formulario de registro
# Solicitar nombre de usuario
# Email
# password
# Botón de aceptar

import tkinter as tk

def saludar():
    print('Hola')

ventana_principal = tk.Tk()

# Asigna un título a la ventana
ventana_principal.title('Hola Mundo App v1.0')
# Asignando tamaño a la ventana
ventana_principal.geometry('640x480')
# Creando los widgets
label_nombre = tk.Label(ventana_principal, text='Nombre:')
label_email = tk.Label(ventana_principal, text='Email:')
label_password = tk.Label(ventana_principal, text='Password:')
entry_nombre = tk.Entry(ventana_principal)
entry_email = tk.Entry(ventana_principal)
entry_password = tk.Entry(ventana_principal)
aceptar = tk.Button(ventana_principal, text='Aceptar', command=saludar)
# Posicionamiento de los widgets
label_nombre.place(x=10, y=10, width=50, height=20)
label_email.place(x=10, y=30, width=50, height=20)
label_password.place(x=10, y=50, width=50, height=20)
entry_nombre.place(x=70, y=10, width=50, height=20)
entry_email.place(x=70, y=30, width=50, height=20)
entry_password.place(x=70, y=50, width=50, height=20)
aceptar.place(x=10, y=80, width=100, height=40)

# Bucle
ventana_principal.mainloop()