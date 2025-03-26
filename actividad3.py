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
=> Para el caso de prestación de Servicios
    Se debe solicitar:
    - El valor del contrato
    - el número de meses del contrato
    - La antiguedad del empleado (años)
    El salario neto, en este caso se calcula:
    1 - dividir el valor del salario mensual
        por el número de meses (Salario mensual)
    2 - Restar el 15% de salario mensual,
        por concepto de EPS (Salud)
    3 - Restar el 10% del valor del salario mensual,
        por concepto de pensión
    4 - Si el empleado tiene una antiguedad
        igual o superior a 10 años:
        tendrá una bonificación del 0.5%
        sobre el salario mensual
=> Para el caso de contrato a termino indefinido
    se debe solicitar:
    - Antiguedad (años)
    - Grado o escalafón (1 -5)
    - El salario minimo
    El salario mensual se calcula de acuerdo
    a la siguiente tabla:
    - grado 1: 1.5 SM
    - grado 2: 1.7 SM
    - grado 3: 2.0 SM
    - grado 4: 2.5 SM
    - grado 5: 3.0 SM
    La bonificación estará a corde a
    los siguientes rangos segun la antiguedad:
    - entre 1 - 5 Años: 1% del SM
    - entre 6 - 10 años: 2% del SM
    - superior a 10 años: 3% del SM
    Para este caso los descuentos de ley son:
    - 25% por concepto de Eps
    - 22% por concepto de Pension
    - 0.1% por concepto de ARL

'''
contrato = input("Ingrese el tipo de contrato: ")
#inicializar variables:
# dar valor inicial a una variable
# asi no se utilice en el momento
salario_neto = 0

if contrato == "a":
    print("Eligió: Contrato a termino indefinido ")
    antiguedad = int(input("Ingrese antiguedad del empleado(años): "))
    grado = int(input("Ingrese grado o escalafon(1-5): "))
    salario_minimo = int(input("Ingrese valor del salario minimo: "))
    salario_mensual = 0
    if grado == 1:
        salario_mensual = salario_minimo * 1.5
    elif grado == 2:
        salario_mensual = salario_minimo * 1.7
    elif grado == 3:
        salario_mensual = salario_minimo * 2.0
    elif grado == 4:
        salario_mensual = salario_minimo * 2.5  
    elif grado == 5:
        salario_mensual = salario_minimo * 3.0
    ##calcular bonificacion
    bonificacion = 0
    if antiguedad >= 1 and antiguedad <= 5:
        bonificacion = salario_mensual * 0.01
    if antiguedad > 5 and antiguedad <= 10:
        bonificacion = salario_mensual * 0.02
    if  antiguedad > 10:
        bonificacion = salario_mensual * 0.03
    ##descuentos de ley
    eps = salario_mensual * 0.25
    pension = salario_mensual * 0.22    
    arl = salario_mensual * 0.001  
    salario_neto = salario_mensual - eps - pension - arl + bonificacion
elif contrato == "b":
    print("Eligió: contrato de Prestación de Servicios")
    valor_contrato = int(input("Ingrese el valor del contrato: "))
    numero_meses = int(input("Ingrese el numero de meses: "))
    antiguedad = int(input("Ingrese la antiguedad en años: "))
    salario_mensual = valor_contrato / numero_meses
    eps = salario_mensual * 0.15
    pension = salario_mensual * 0.10
    bonificación = salario_mensual * 0.05
    salario_neto = salario_mensual - eps - pension
    if antiguedad >= 10:
        salario_neto = salario_neto + bonificación
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