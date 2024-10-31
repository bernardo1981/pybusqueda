import webbrowser

# Preguntar al usuario qué quiere hacer hoy
actividad = input("¿Qué quieres hacer hoy? ")

# Formatear la búsqueda en Google
busqueda = '+'.join(actividad.split())
url = f"https://www.google.com/search?q={busqueda}"

# Abrir la búsqueda en el navegador
webbrowser.open(url)

print(f"Buscando en Google: {actividad}")
