'''
Actividad 3:
Elabore un programa que 
permita calcular el salario
neto de un empleado,
despues de descontar los 
descuentos por conceptos de:
Salud, Pension, ARL
1. El programa debe solicitar
    el tipo de empleado
    a - Contrato a termino indefinido
    b - Contrato por prestación 
    de Servicios
    c - Contrato de Aprendizaje
    d - Contrato por Jornal (Freelance)
=> Para el caso de Jornal: 
    Se debe solicitar:
    - El número de horas trabajadas
    - El valor por hora
    * El total de salario se calcula
    de multiplicar el número de horas
    por el valor a pagar por hora
'''
contrato = input("Ingrese el tipo de contrato: ")
#inicializar variables:
# dar valor inicial a una variable
# asi no se utilice en el momento
salario_neto = 0

if contrato == "a":
    print("Eligió: contrato a Termino Indefinido")
elif contrato == "b":
    print("Eligió: contrato de Prestación de Servicios")
elif contrato == "c":
    print("Eligió: contrato de Aprendizaje")
    print("Eligió: Jornal")
    # Variable local:
    # Variable que solo se utiliza 
    # en un bloque de código
    salario_minimo = int(input("Ingrese el salario minimo vigente: "))
    salario_neto = salario_minimo - (salario_minimo * 0.25)
elif contrato == "d":
    print("Eligió: Jornal")
    numero_horas = int(input("Ingrese el número de horas: "))
    valor_hora = int(input("Ingrese el valor a pagar por hora: "))
    salario_neto = numero_horas * valor_hora
else:
    print("Tipo de contrato no existente")
print("El salario neto es: ", salario_neto)
print("Fin del programa")