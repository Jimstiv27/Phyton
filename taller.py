''''''''''''''''''''''''''''''''''''''''''''
'''Author:JimStiv27                     '''
'''Email:chsj-7@hotmail.co              '''
'''Ejercicios Python Nivel I            '''
''''''''''''''''''''''''''''''''''''''''''''
#Se asigna true a la variable que controla las excepciones interacciones del menú
BandMenu = True
while BandMenu == True:
    try:
        #Se lista el menú, según el taller
        OpcMenu = int(input("Seleccione el ejercicio a realizar:\n1. Programa de Edad\n2. Número menor\n3. Diferencia entre números\n4. Conteo de caracter específico en cadena\n5. Caja registradora\n6. Pirámide base 15\n"))
        
        #Se condiciona la ejecución de los ejercicios según valor ingresado en consola
        if OpcMenu == 1:

            #Bandera para el capturador de excepciones y ejecución de interacciones
            Band1 = True
            while Band1 == True: 
                try:
                    #Se solicita la edad 
                    Edad = float(input("Ingrese su edad\n"))

                    #Se condicionan las impresiones según el valor ingresado por consola
                    if Edad >= 90:
                        print("La edad ingresada es mayor o igual a 90. Ingrese un nuevo valor.")
                        #Se asigna true a la variable bandera para que vuelva a preguntar la edad por consola
                        Band1 = True
                    elif Edad >= 18 and Edad <= 32:
                        print("Usted es un joven\n")
                    elif Edad > 32 and Edad < 90:
                        print("Usted es mayor\n")
                    elif Edad >= 0 and Edad < 18:
                        print("Usted es un niño\n")
                    #Se asigna por defecto false a la variable bandera
                    if Band1 == False:    
                        break
                    else:
                        #Se asigna true a la variable repetidora para el control del datos del ejercicio
                        Repeat = True
                        while Repeat == True:
                            Repeat = False
                            Var1 = input("¿Desea ingresar una nueva edad? Y/N\n")
                            if Var1== "y" or  Var1== "Y":
                                Band1 = True
                            elif Var1 == "n" or  Var1== "N":
                                #Se da por terminada la ejecución del proceso
                                Band1 = False
                                break
                            #Se capturan los valores no aceptados y se muestra nuevamente el menú de ingresar la edad
                            else:
                                Var1 = input("Solo son aceptados los valores Y/N.\n")
                                Repeat = True
                #Se capturan los valores no numéricos ingresados en el input de edad                
                except ValueError:
                    print("El valor ingresado no es aceptado para el ejercicio.\n")
        elif OpcMenu == 2:
            #Bandera para el capturador de excepciones y ejecución de interacciones
            band2 = True
            #Se inicializa la variable que controlará el menor valor ingresado
            menor = 0
            while band2 == True:
                try:
                    #Bucle para manejo de números ingresados    
                    for x in range(5):    
                        numero = float(input("Ingresa un número\n"))
                        #Se condiciona para que en la primera interacción del bucle se asigne el valor a la variable menor
                        if x == 0:
                            menor = numero
                        else:
                            #Se valida si el número ingresado es menor a la variable menor para asignarlo en caso tal de ser correcto
                            if menor > numero:
                                menor = numero
                    #Se imprime el resultado            
                    print("El número menor ingresado es:", menor)
                    #Se asigna por defecto false a la variable bandera
                    if band2 == False:    
                        break
                    else:
                        #Se asigna true a la variable repetidora para el control del datos del ejercicio
                        Repeat = True
                        while Repeat == True:
                            Repeat = False
                            Var1 = input("¿Desea repetir el ejercicio? Y/N\n")
                            if Var1== "y" or  Var1== "Y":
                                band2 = True
                            elif Var1== "n" or  Var1== "N":
                                #Se da por terminada la ejecución del proceso
                                band2 = False
                                break
                            else:
                                Var1 = input("Solo son aceptados los valores Y/N.\n")
                                Repeat = True
                #Se capturan los valores no numéricos ingresados en los input
                except ValueError:
                    print("El valor ingresado no corresponde a un número")
        elif OpcMenu == 3:
            #Bandera para el capturador de excepciones y ejecución de interacciones
            band3 = True
            while band3 == True:
                try:
                    numero1 = int(input("Ingrese un número\n"))
                    numero2 = int(input("Ingrese un número mayor al anterior\n"))
                    suma = 0
                    #Condición para validar que el segundo número sea mayor al primero
                    if numero2 < numero1:
                        print("El segundo número ingresado no cumple con la condición de ser mayor que el primero")
                        break
                    else:
                        #Ciclo para sumar la diferencia entre ambos números
                        for x in range(numero1+1,numero2):
                            #Función sum encargada de la operación
                            suma = sum(range(numero1+1,numero2))
                    #Impresión del resultado de la ejecución        
                    print("La suma total es:", suma)
                    #Se asigna por defecto false a la variable bandera
                    if band3 == False:    
                        break
                    else:
                        #Se asigna true a la variable repetidora para el control del datos del ejercicio
                        Repeat = True
                        while Repeat == True:
                            Repeat = False
                            Var1 = input("¿Desea repetir el ejercicio? Y/N\n")
                            if Var1== "y" or  Var1== "Y":
                                band3 = True
                            elif Var1== "n" or  Var1== "N":
                                #Se da por terminada la ejecución del proceso
                                band3 = False
                                break
                            else:
                                Var1 = input("Solo son aceptados los valores Y/N.\n")
                                Repeat = True                        
                #Se capturan los valores no numéricos ingresados en los input
                except ValueError:
                    print("El valor ingresado no corresponde a un número")

        elif OpcMenu == 4:
            #Bandera para el capturador de excepciones y ejecución de interacciones
            band4 = True
            while band4 == True:
                try:
                    cadena = input("Ingrese una cadena de texto de más de 50 caracteres\n")
                    #Validación de longitud de cadena
                    if len(cadena) >= 50:
                        caracter = input("Ingrese el caracter a buscar\n")
                        #Función count que permite saber cuantas veces está un subtring en un string inicial
                        print("El caracter ", caracter,"se encuentra ",cadena.count(caracter)," veces en el texto ingresado")
                    else:
                        print("La cadena no cumple con la cantidad de caracteres solicitados\n")
                        band4 = True
                    #Se asigna por defecto false a la variable bandera
                    if band4 == False:    
                        break
                    else:    
                        Repeat = True
                        while Repeat == True:
                            Repeat = False
                            Var1 = input("¿Desea repetir el ejercicio? Y/N\n")
                            if Var1== "y" or  Var1== "Y":
                                band4 = True
                            elif Var1== "n" or  Var1== "N":
                                #Se da por terminada la ejecución del proceso
                                band4 = False
                                break
                            else:
                                Var1 = input("Solo son aceptados los valores Y/N.\n")
                                Repeat = True
                #Se capturan los valores no numéricos ingresados en los input                
                except ValueError:
                    print("Los valores ingresados no corresponden a lo solicitado")
        elif OpcMenu == 5:
            #Bandera para el capturador de excepciones y ejecución de interacciones
            band5 = True
            while band5 == True:
                try:
                    comprador = input("Ingrese su nombre\n")
                    cantProductos = int(input("Ingrese la cantidad de referencias a registrar\n"))
                    #Declaración de vectores
                    nomProductos = []
                    cantxProductos = []
                    valorUnitario = []
                    subtotal = []
                    for x in range(cantProductos):
                        nomProductos.append(input("Ingrese el nombre del producto\n"))
                        cantxProductos.append(int(input("Ingrese la cantidad de unidades por producto\n")))
                        valorUnitario.append(float(input("Ingrese el valor unitario del producto\n")))
                        #Se calcula el subtotal por producto
                        subtotal.append(cantxProductos[x] * valorUnitario[x])
                    #Se imprime la factura de compra
                    print("\nDetalle de la compra")
                    total = 0
                    desc = 0
                    for y in range(cantProductos):
                        print("Producto: ",nomProductos[y],"\nCantidad: ", cantxProductos[y],"\nValor Unitario: ",valorUnitario[y],"\nSubtotal:", subtotal[y],"\n")
                        total +=  cantxProductos[y] * valorUnitario[y]
                        print("Precio Total Neto ",total,"\n")
                    #Se calcula el descuento según el total de compra
                    if total > 1000000:
                       total*= 0.85
                       desc = 15
                    elif total > 500000:
                       total*= 0.9
                       desc = 10
                    #Impresión del valor total de compra   
                    print("Descuento",desc,"% \nTotal Compra $",total)
                    if band5 == False:    
                        break
                    else:
                        Repeat = True
                        while Repeat == True:
                            Repeat = False
                            Var1 = input("¿Desea repetir el ejercicio? Y/N\n")
                            if Var1== "y" or  Var1== "Y":
                                band5 = True
                            elif Var1== "n" or  Var1== "N":
                                #Se da por terminada la ejecución del proceso
                                band5 = False
                                break
                            else:
                                Var1 = input("Solo son aceptados los valores Y/N.\n")
                                Repeat = True
                #Se capturan los valores errados en los input   
                except ValueError:
                    print("Los valores ingresados no corresponden a lo solicitado")
        elif OpcMenu == 6:
            var1 = " "
            var2 = "*"
            #Se asigna valor a las variables que controlan el contorno de la pirámide
            Num1 = 7
            num2 = 1
            #Se imprime la primera fila
            print((var1*Num1)+(var2*num2)+(var1*Num1))

            #Bucle para la impresión
            for t in range(7):
                Num1 -=1
                #Condición para la base
                if Num1 == 0:
                    num2 +=2
                    print(var2*num2)
                else:
                    #impresión de los niveles diferentes a la base
                    print((var1*Num1)+(var2)+(var1*num2)+(var2)+(var1*Num1))
                num2 +=2
    #Controlador de excepciones del menú del ejercicio                  
    except ValueError:
        print("Has seleccionado una opción no válida. Por favor ingresar nuevamente.\n")