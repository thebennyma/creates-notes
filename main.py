"""

Proyecto python mysql:
  - Abrir asistente
  - Login o registro

  Registro: 
    - Si elegimos registro, creara un usuario en la bd

  Login: 
    - Si elegimos login, identificara al usuario y nos preguntara:
      - Crear nota
      - Mostrar nota
      - Borrar nota


"""

from usuarios import acciones

print("""
Acciones del sistema
      - registro
      - login
""")

hazEl = acciones.Acciones()

accion = input("¿Que quieres hacer? : ")

if accion == "registro":
    hazEl.registro()

elif accion == "login":
    hazEl.login()
