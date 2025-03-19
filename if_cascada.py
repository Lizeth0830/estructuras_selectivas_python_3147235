'''instruccion2
elif condicional2:
    instruccion3
    instruccion4
elif condicional3:
    instruccion5
    instruccion6
NOTA: Cada condicional
es MUTUAMENTE EXCLUYENTE
'''
#Ejemplo:
#Vamos a hacer un pequeño 
#traductor.
#el programa debe permitir
#leer una fruta en español
#y debe mostrar esa fruta 
#en ingles
Fruta_es = input("Ingrese Una Fruta: ")
if Fruta_es == "manzana" or Fruta_es == "Manzana":
    print("Apple")
elif Fruta_es == "naranja" or Fruta_es == "Naranja":
    print("Orange")
elif Fruta_es == "uva" or Fruta_es == "Uva":
    print("Grape")
elif Fruta_es == "mandarina" or Fruta_es == "Mandarina":
    print("Tangerine")
elif Fruta_es == "banano" or Fruta_es == "Banano":
    print("Banana")
#Caso por defecto
#default
else: 
    print("No Se Encontró Traducción")