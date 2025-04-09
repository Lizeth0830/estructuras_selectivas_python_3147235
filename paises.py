paises =[
            {
                "nombre":"Venezuela",
                "capital":"Caracas",
                "moneda":"Bolivar",
                "poblacion":{
                                "censo": 26,
                                "densidad": 31,
                            },
                "ciudades": [
                                "Maracaibo",
                                "Valencia",
                                "Barquisimeto",
                                "Carabobo",
                            ],
                "superficie": 916,
            },
            {
                "nombre":"Brasil",
                "capital":"Brasilia",
                "moneda":"Real",
                "poblacion":{
                                "censo": 213,
                                "densidad": 25,
                            },
                "ciudades": [
                                "Rio de Janeiro",
                                "Salvador de bahia",
                                "Natal",
                            ],
                "superficie": 8,
                    },
            {
                "nombre":"Paraguay",
                "capital":"Asuncion",
                "moneda":"Guaraní",
                "poblacion":{
                                "censo": 7,
                                "densidad": 16, 
                            },
                "ciudades": [
                                "Concepción",
                                "Encarnación",
                                "Pedro Juan Caballero",
                                "Ciudad del Este",
                                "Villarica",
                            ],
                "superficie": 406,
            },
        ]
#Recorrer Todos Los Paises:
print("Recorriendo Todos Los Paises")

for pais in paises:
    print("Ciudades principales: ")
    for ciudad in pais ["ciudades"]:
        print("-", ciudad)
    print("Nombre:", pais["nombre"])
    print("Capital:", pais["capital"])
    print("Poblacion:")
    print("- Censo: ", pais["poblacion"]["densidad"],"millones")
    print("- Densidad: ", pais["poblacion"]["densidad"], "por Km2")
    print("Superficie:", pais["superficie"], "millones de Km2")
    print("-----------------")