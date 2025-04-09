#diccionario:
# Colección de datos que
# los alamacena en pares
# clave-valor
# - un diccionario comienza y termina 
#   con llaves (curly braces) 
# - la clave se seprara del valor 
#   por dos puntos (:) 
# - la clave siempre es un string 
# - el valor puede ser de cualquier tipo
# - cada elemento (propiedad) del 
#   diccionario se separa por una coma
 
# Ejemplo: diccionario 
# que almacene los datos de un 
# pais
pais1 = {
            'nombre': 'Argentina',
            'capital': 'Bunos Aires',
            'moneda': 'Peso Argentino',
            'ciudades': [
                            "Cordoba",
                            "Rosario",
                            "Mendoza",
                        ],
            'poblacion':{
                            "censo": 46,
                            "densidad": 16,
                        }
        } 
pais2 = {
            'nombre': 'Ecuador',
            'capital': 'Quito',
            'moneda': 'Dolar',
            'ciudades': [
                            "Guayaquil",
                            "Cuenca",
                        ],
            'poblacion':{
                            "censo": 16,
                            "densidad": 52,
                        }
        } 
pais3 = {
            'nombre': 'Paraguay',
            'capital': 'Asunción',
            'moneda': 'Guaraní',
            'ciudades': [
                            "Concepción",
                            "Encarnación",
                            "Pedro Juan Caballero",
                            "Ciudad del Este",
                        ],
            'poblacion':{
                            "censo": 6,
                            "densidad": 12,
                        }
        } 
# Acceder a la información del pais
print(pais1['moneda'])
print(pais2['capital'])
# Acceder a una ciudad del pais1
print(pais1['ciudades'][1])
print("-----------------")
# iterar las ciudades del pais1
for ciudad in pais1['ciudades']:
    print(ciudad)
# Acceder a datos poblacionales
print("-----------------")
print("Censo:", pais1['poblacion']['censo'], "millones de habitantes")
# Acceder a la densidad
print("Densidad:", pais1['poblacion']['densidad'], " por Km2")