'''
If else:
Sirve para determinar dos cambios
de ejecución, basados en la evaluación de una condicional
Sintaxis:
if condicional:
    instrucción1
    instrucción2
else:
    instrucción3
    instrucción4
'''
#Ejemplo:
#Elabore un programa en python
#que determine si una persona
#es mayor o menor de edad
#y por tanto, habilitada para
#votar
edad = int(input("Ingrese su edad: "))
documento = input ("Tiene documento? (SI/NO):")
if edad >= 18 and documento == "SI":
    print("Usted es mayor de edad")
    print("Puede votar")
else:
    print("Usted es menor de edad")
    print("o")
    print("No puede votar")
print("Fin del programa")