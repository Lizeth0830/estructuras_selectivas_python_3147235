'''
If anidados:
If dentro de otros if
syntax
If condición1:
    If condición2:
        print("mensaje1")
        If condición3:
            print("mensaje2")
            If condición4:
                print("mensaje3")
    elif condicion5:
        print("mensaje4")
    elif condicion6:
        print("mensaje5")
else:
    print("mensaje")
No confundir con elif (if en cascada)
'''

#Ejemplo 1:
#Modifique el ejercicio de la edad
#para las siguientes condiciones
#1. si es mayor de 18 años
#   pero no tiene documento, no puede votar
#   de lo contrario si puede votar
#2. Si es menor de 18 años
#   no puede votar
#Utilice estructura If anidados
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    documento = input("Tiene documento? (si/no): ")
    if documento == "si":
        print("Puede votar")
    else:
        print("No puede votar, No tiene documento")
else:
    print("No puede votar")