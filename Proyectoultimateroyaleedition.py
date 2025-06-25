import random
import numpy as np
import colorama
from colorama import *
init()

def main ():
    #Primer caldo de cultivo
    caldo_og = np.full((20,20),0)
    caldo_2 = np.full((20,20),0)
    caldo_clon = np.full((20,20)," ")

    def cadena_car(caldo): # (ERROR. En la posicion final tiene que tener un punto, pero sale despegado y con una coma)
        c1 = ""
        for i in range (0, len(caldo), 1):
            for j in range(0, len(caldo), 1):
                if (caldo[i,j] == 1):
                    c1 += Fore.MAGENTA+"("
                    c1 += Fore.GREEN+str((i))
                    c1 += Fore.MAGENTA+","
                    c1 += Fore.GREEN+str((j))
                    c1 += Fore.MAGENTA+"), "
        c1 += Fore.MAGENTA+"."

        print()
        print(Fore.CYAN+"----- Posiciones de las células -----"+Fore.RESET)    
        print()        
        print(c1 + Fore.RESET)
        print()

    def llenar_matriz(caldo_og):
        for i in range(0,len(caldo_og),1):
            for j in range(0,len(caldo_og),1):
                caldo_og[i,j] = random.randint(0,1)

    def mostrar_matriz(caldo):
        print(Fore.GREEN+"Los elementos de la Matriz son:"+Fore.RESET)
        for i in range(0,len(caldo),1):
            for j in range(0,len(caldo),1):
                print(caldo[i,j],end=" ")
            print()

    def aplicar_reglas(suma, i, j, caldo_2, caldo_og):
        # Regla 1: Soledad (si una celda esta ocupada por una celula y tiene una sola o ninguna celula vecina muere)
        if ((suma <= 1) and (caldo_og[i,j] == 1 or caldo_og[i,j] == 2)):
            caldo_2[i,j] = 0
        # Regla 2: Superpoblación (si la celda esta ocupada por una celula y tiene 4 o mas celulas vecinas muere)
        elif ((suma >= 4) and (caldo_og[i,j] == 1 or caldo_og[i,j] == 2)):
            caldo_2[i,j] = 0
        # Regla 3: Vecinos (si la celda esta ocupada por una celula y tiene 2 o 3 celulas vecinas sobrevive)
        elif((suma == 2 or suma == 3) and (caldo_og[i,j] == 1 or caldo_og[i,j] == 2)):
            caldo_2[i,j] = 1
        # Regla 4: Reproducción (si la celda no esta ocupada y tiene 3 celulas vecinas, nace una nueva celula)
        elif((suma == 3) and (caldo_og[i,j] == 0)):
            caldo_2[i,j] = 1

    def mutacion(caldo_og , caldo_2): # Recorre la matriz, suma los vecinos y aplica las reglas a cada celda
        suma = 0
        
        # Caso esquinas:
        # [0,0] (esquina superior izquierda)
        suma = caldo_og[0, 1] + caldo_og[1,0] + caldo_og[1,1]
        aplicar_reglas(suma , 0 , 0, caldo_2, caldo_og)

        # [len,0] (esquina inferior izquierda)
        suma = caldo_og[len(caldo_og)-2, 0] + caldo_og[len(caldo_og)-2 , 1] + caldo_og[len(caldo_og)-1 , 1]
        aplicar_reglas(suma , len(caldo_og)-1 ,  0, caldo_2, caldo_og)

        # [0,len] (esquina superior derecha)
        suma = caldo_og[0, len(caldo_og)-2] + caldo_og[1,len(caldo_og)-2] + caldo_og[1,len(caldo_og)-1]
        aplicar_reglas(suma , 0 , len(caldo_og)-1, caldo_2, caldo_og)

        #4 [len, len] (esquina inferior derecha)
        suma = caldo_og[len(caldo_og)-1 , len(caldo_og)-2] + caldo_og[len(caldo_og)-2 , len(caldo_og) -2] + caldo_og[len(caldo_og)-2 , len(caldo_og)-1]
        aplicar_reglas(suma , len(caldo_og)-1 , len(caldo_og)-1, caldo_2, caldo_og)
        
        for i in range(0,len(caldo_og),1):
            for j in range(0,len(caldo_og),1):
        
        # Caso bordes:
                # Fila limite superior
                if (i == 0 and (0 < j < len(caldo_og) - 1)): 
                    suma = caldo_og[i,j-1] + caldo_og[i,j+1] + caldo_og[i+1,j-1] + caldo_og[i+1,j] + caldo_og[i+1,j+1]
                    aplicar_reglas(suma , i , j, caldo_2, caldo_og)
                
                # Columna limite izquierda
                elif (j == 0 and (0 < i < len(caldo_og) - 1)): 
                    suma = caldo_og[i-1,j] + caldo_og[i-1,j+1] + caldo_og[i,j+1] + caldo_og[i+1,j] + caldo_og[i+1,j+1]
                    aplicar_reglas(suma , i , j, caldo_2, caldo_og)

                # Fila limite inferior 
                elif (i == len(caldo_og)-1 and (0 < j < len(caldo_og)-1)): 
                    suma = caldo_og[i-1,j-1] + caldo_og[i-1,j] + caldo_og[i-1,j+1] + caldo_og[i,j-1] + caldo_og[i,j+1]
                    aplicar_reglas(suma , i , j, caldo_2, caldo_og)

                # Columna limite derecha  
                elif(j == len(caldo_og)-1 and (0 < i < len(caldo_og)-1)): 
                    suma = caldo_og[i-1,j-1] + caldo_og[i-1,j] + caldo_og[i,j-1] + caldo_og[i+1,j-1] + caldo_og[i+1,j] 
                    aplicar_reglas(suma , i , j, caldo_2, caldo_og)

        # Caso normal:
                elif((0 < i < len(caldo_og)-1) and ((0 < j < len(caldo_og)-1))):
                    suma = caldo_og[i-1,j-1] + caldo_og[i-1,j] + caldo_og[i-1,j+1] + caldo_og[i,j-1] + caldo_og[i,j+1] + caldo_og[i+1,j-1] + caldo_og[i+1,j] + caldo_og[i+1,j+1]
                    aplicar_reglas(suma , i , j, caldo_2, caldo_og)
               
    def cambio(caldo_2 , caldo_clon):
        for i in range(0,len(caldo_clon),1):
            for j in range(0,len(caldo_clon),1):
                if(caldo_2[i,j]== 0):
                    caldo_clon[i,j] = "🟥"
                elif(caldo_2[i,j]== 1):
                    caldo_clon[i,j] = "🟦"
                elif(caldo_2[i,j]== 2):
                    caldo_clon[i,j] = "🟨"
        
    # MILAGROS

    def milagro1(caldo): #Recorrido espiral cajon
        filas_max = len(caldo)
        columnas_max = len(caldo[0]) if filas_max > 0 else 0

        limsuperior = 0
        liminferior = filas_max - 1
        limderecha = columnas_max - 1
        limizquierda = 0

        fila = 0
        columna = 0
        totalceldas = filas_max * columnas_max

        recorrido_elementos = np.empty(totalceldas, dtype=caldo.dtype)

        e = 0
        celdasvisitadas = 0

        # NUEVOS CONTADORES para milagro 1
        contador_coord_impares = 0
        contador_ocupadas = 0

        while celdasvisitadas < totalceldas:
            # 1. Derecha →
            for c in range(columna, limderecha + 1):
                if celdasvisitadas < totalceldas:
                    recorrido_elementos[e] = caldo[fila, c]
                    if fila % 2 != 0 and c % 2 != 0:
                        contador_coord_impares += 1
                        if caldo[fila, c] == 1:
                            contador_ocupadas += 1
                    e += 1
                    celdasvisitadas += 1
            fila += 1
            limsuperior += 1
            columna = limderecha

            # 2. Abajo ↓
            for r in range(fila, liminferior + 1):
                if celdasvisitadas < totalceldas:
                    recorrido_elementos[e] = caldo[r, columna]
                    if r % 2 != 0 and columna % 2 != 0:
                        contador_coord_impares += 1
                        if caldo[r, columna] == 1:
                            contador_ocupadas += 1
                    e += 1
                    celdasvisitadas += 1
            columna -= 1
            limderecha -= 1
            fila = liminferior

            # 3. Izquierda ←
            for c in range(columna, limizquierda - 1, -1):
                if celdasvisitadas < totalceldas:
                    recorrido_elementos[e] = caldo[fila, c]
                    if fila % 2 != 0 and c % 2 != 0:
                        contador_coord_impares += 1
                        if caldo[fila, c] == 1:
                            contador_ocupadas += 1
                    e += 1
                    celdasvisitadas += 1
            fila -= 1
            liminferior -= 1
            columna = limizquierda

            # 4. Arriba ↑
            for r in range(fila, limsuperior - 1, -1):
                if celdasvisitadas < totalceldas:
                    recorrido_elementos[e] = caldo[r, columna]
                    if r % 2 != 0 and columna % 2 != 0:
                        contador_coord_impares += 1
                        if caldo[r, columna] == 1:
                            contador_ocupadas += 1
                    e += 1
                    celdasvisitadas += 1
            columna += 1
            limizquierda += 1
            fila = limsuperior

        # Evaluar la condición del milagro
        if contador_coord_impares > 0:
            porcentaje = (contador_ocupadas * 100) // contador_coord_impares
            print(f"Milagro 1: {porcentaje}% de ocupación en coordenadas impares")
            if porcentaje >= 50:
                print("✨ ¡Condición para Milagro 1 cumplida!")
                for i in range(0,len(caldo),1):
                    for j in range(0,len(caldo),1):
                        if (caldo[i,j] == 0):
                            caldo[i,j] = 2
                            return
                    
            else:
                print("⚠️ No se cumple la condición para Milagro 1")
            
    def milagro2(caldo):
        contador_x_par = 0  # Todos los x pares
        contador_x_ocupados = 0 # Los x pares que estan ocupados
 
        for i in range(0, len(caldo), 1): # Hasta la diagonal secundaria (de izquierda a derecha)
            for j in range(0 , i+1 , 1): 
                if(i%2 == 0):
                    contador_x_par += 1
                    if(caldo[i-j,j] == 1):
                        contador_x_ocupados += 1

        for i in range(1, len(caldo), 1): # Matriz inferior 
            for j in range(0 , len(caldo)-i , 1): 
                if(i%2 == 0):
                    contador_x_par += 1
                    if(caldo[len(caldo)-1 -j, i+j] == 1):
                            contador_x_ocupados += 1
        
        if (contador_x_par > 0): 
            porcentaje = (contador_x_ocupados * 100) // contador_x_par
            print(f"Milagro 2: {porcentaje}% de ocupación en coordenadas impares")
            if porcentaje >= 70:
                print("✨ ¡Condición para Milagro 2 cumplida!")
                for i in range(0, len(caldo), 1): #Pone un dos en caso de que si sirva
                    for j in range(0 , i+1 , 1):
                        if (caldo[i-j,j] == 0):
                            caldo[i-j,j] = 2
                            return
                for i in range(1, len(caldo), 1): # pone un dos en caso de que no se encuentre en la anterior 
                    for j in range(0 , len(caldo)-i , 1): 
                        if(caldo[len(caldo)-1 -j, i+j] == 0):
                            caldo[len(caldo)-1 -j, i+j] = 2
                            return
                               
            else:
                print("⚠️ No se cumple la condición para Milagro 2")

    def milagro3(caldo):
        
        contador_y_impares = 0
        contador_y_ocupadas = 0

        for j in range(len(caldo)-1, -1, -1):
            if (j % 2 == 1):
                for i in range (0, len(caldo), 1):
                    contador_y_impares += 1
                    if (caldo[i,j]== 1):
                        contador_y_ocupadas += 1
                        
        if (contador_y_impares > 0):
            porcentaje = (contador_y_ocupadas * 100) // contador_y_impares
            print(f"Milagro 3: {porcentaje}% de ocupación en coordenadas impares")
            if porcentaje >= 60:
                print("✨ ¡Condición para Milagro 3 cumplida!")
                for i in range(0,len(caldo),1):
                    for j in range(0,len(caldo),1):
                        if (caldo[i,j] == 0):
                            caldo[i,j] = 2
                            return
                    
            else:
                print("⚠️ No se cumple la condición para Milagro 3")
        
    def menu_milagros(caldo):
        opcion = 0
        verdad = False

        while True:
            print(Fore.MAGENTA + "=====================================")
            print(Fore.YELLOW + "           MENU DE MILAGROS          ")
            print(Fore.MAGENTA + "=====================================")
            print(Fore.CYAN + " 1. Primer Milagro                   ")
            print(" 2. Segundo Milagro                  ")
            print(" 3. Tercer Milagro                   ")
            print(Fore.MAGENTA + "-------------------------------------")
            print(Fore.CYAN + " 4. Volver al menú principal         ")
            print(Fore.MAGENTA + "=====================================" + Fore.RESET)

            while (verdad ==  False):
                    opcion = int(input(Fore.YELLOW+"Seleccione una opción: "+Fore.RESET))
                    print()
                    if (opcion > 0 or opcion > 4):
                        verdad = True
                    else:
                        print(Fore.RED+"ERROR: Ingrese un número válido."+Fore.RESET)

            match opcion:
                case 1:
                    print("✨ Ejecutando el Primer Milagro...")
                    milagro1(caldo)
                    cambio(caldo, caldo_clon)
                    mostrar_matriz(caldo)
                    print()
                    mostrar_matriz(caldo_clon)
                    guardar_archivo(caldo)
                    print(Fore.GREEN+"Thanks for playing *con voz de Luigi*"+Fore.RESET)
                    break
                case 2:
                    print("✨ Ejecutando el Segundo Milagro...")
                    milagro2(caldo)
                    cambio(caldo, caldo_clon)
                    mostrar_matriz(caldo)
                    print()
                    mostrar_matriz(caldo_clon)
                    guardar_archivo(caldo)
                    print(Fore.GREEN+"Thanks for playing *con voz de Luigi*"+Fore.RESET)
                    break   
                case 3:
                    print("✨ Ejecutando el Tercer Milagro...")
                    milagro3(caldo)
                    cambio(caldo, caldo_clon)
                    mostrar_matriz(caldo)
                    print()
                    mostrar_matriz(caldo_clon)
                    guardar_archivo(caldo)
                    print(Fore.GREEN+"Thanks for playing *con voz de Luigi*"+Fore.RESET)
                    break
                case 4:
                    print("Volviendo al menú principal...")
                    break
        
    def leer_archivos():
            caldo = np.full((20, 20), 0)
            arch2 = open("utileria/archivo.txt", "rt")
        
            i = 0
            j = 0
        
            for linea in arch2: #1
                numero = int(linea[0])
                caldo[i,j] = numero
                j += 1
                if j == len(caldo):
                    j = 0
                    i += 1
                if i == len(caldo):
                    break
                
            arch2.close()
            copiar_matriz_origendestino(caldo , caldo_og)

    def guardar_archivo(caldo): 
        # Abrir archivo en modo escritura ('w' sobrescribe, 'a' agrega)
        archivo = open('datos.txt', 'wt')
        archivo2 = open('datos.bin', 'wt')

        # Escribir información
        for i in range(0, len(caldo), 1):
            for j in range(0, len(caldo), 1):
                num = bin(caldo[i,j])
                archivo2.write(f'{num}\n')

        for i in range(0, len(caldo), 1):
            for j in range(0, len(caldo), 1):
                num = caldo[i,j]
                archivo.write(f'{num}\n')

        # Cerrar el archivo
        archivo.close()
        archivo2.close()  
    
    def alguna_viva(caldo):
        for i in range(0, len(caldo), 1):
            for j in range(0, len(caldo), 1):
                if(caldo[i,j] == 1):
                    return True
        return False
    
    def copiar_matriz_origendestino(caldo_origen , caldo_destino): # caldillo es clave (mentira, caldillo es una mierda) (Actualizacion: caldillo es la clave)
        for i in range(0,len(caldo_og),1):
            for j in range(0,len(caldo_og),1):
                caldo_destino[i,j] = caldo_origen[i,j]

    def aplicar_generaciones(caldo_og , caldo_clon, caldo_2):
        caldillo = np.full((20,20),0)
        generacion = 0
        repeticiones = int(input(Fore.YELLOW+"¿Cuántas generaciones quieres que se reproduzcan?: "+Fore.RESET))
        print()
        while (repeticiones < 1):
            print(Fore.RED+"ERROR. La cantidad de generaciones tiene que ser mínimo 1."+Fore.RESET)
            repeticiones = int(input(Fore.YELLOW+"Introduzca nuevamente la cantidad de generaciones que quiere que se reproduzcan: "+Fore.RESET))
            print()
        while(repeticiones > 0):
            repeticiones -= 1
            generacion += 1
            if(generacion%2 == 1):
                mutacion(caldo_og, caldo_2)
                cambio(caldo_2, caldo_clon)
                print(Fore.BLUE+f'------ Generación ',generacion,'------'+Fore.RESET)
                print()
                mostrar_matriz(caldo_2)
                print()
                mostrar_matriz(caldo_clon)
                cadena_car(caldo_2)
                pausa = input(Fore.YELLOW+"Pulse cualquier tecla para continuar: "+Fore.RESET)
                print()
                if (alguna_viva(caldo_2) == False):
                    print(Fore.BLUE+f'Todas las celulas murieron en la generacion: ', generacion,''+Fore.RESET)
                    print()
                    mostrar_matriz(caldo_2)
                    # Las celulas murieron, la esperanza se ha ido, la civilizacion se queda a las puestas de su era dorada, es todo tu culpa, eres un dios engreido, reevalua tus decisiones, se mejor
                copiar_matriz_origendestino(caldo_2, caldillo)
            
            else:
                mutacion(caldo_2, caldo_og)
                cambio(caldo_og, caldo_clon)
                print(Fore.BLUE+f'------ Generación ',generacion,'------'+Fore.RESET)
                print()
                mostrar_matriz(caldo_og)
                print()
                mostrar_matriz(caldo_clon)
                cadena_car(caldo_og)
                pausa = input(Fore.YELLOW+"Pulse cualquier tecla para continuar: "+Fore.RESET)
                if (alguna_viva(caldo_og) == False):
                    print("Todas las celulas murieron en la generacion: " , generacion) # Posible agregar pausa (revisar)
                    print()
                    mostrar_matriz(caldo_og)
                copiar_matriz_origendestino(caldo_og, caldillo) 
        validador = input(Fore.YELLOW+"¿Quieres implementar algun milagro? (si/no): "+Fore.RESET)
        print()
        while (validador != "si" and validador != "no" and validador != "SI" and validador != "NO" and validador != "Si" and validador != "No"):
            print(Fore.RED+"ERROR: Ingrese una opción válida (si/no)."+Fore.RESET)
            validador = input(Fore.YELLOW+"Responde nuevamente con si o no: "+Fore.RESET)
            print()
        if (validador == "si" or validador == "SI" or validador == "Si"): # Arreglen esta verga
            menu_milagros(caldillo)
        else: 
            print(Fore.GREEN+"Thanks for playing *con voz de Luigi*"+Fore.RESET)

    def menu_principal():
        opcion = 0
        verdad = False
        while True:
            print(Fore.MAGENTA+"=====================================")
            print(Fore.YELLOW+"         MENU PRINCIPAL              ")
            print(Fore.MAGENTA+"=====================================")
            print(Fore.CYAN+" 1. Generar matriz aleatoriamente    ")
            print(" 2. Matriz personalizada             ")
            print(" 3. Matriz cargada de archivos       ")
            print(Fore.MAGENTA+"-------------------------------------")
            print(Fore.CYAN+" 4. Guardar y Salir                  ")
            print(Fore.MAGENTA+"======================================"+Fore.RESET)
            # verificacion numero valido
            while (verdad ==  False):
                opcion = int(input(Fore.YELLOW+"Seleccione una opción: "+Fore.RESET))
                print()
                if (opcion > 0 or opcion > 4):
                    verdad = True
                else:
                    print(Fore.RED+"ERROR: Ingrese un número válido."+Fore.RESET)
                

            match opcion:
                case 1:
                    print(Fore.LIGHTRED_EX+"Opción 1: Generar matriz aleatoriamente"+Fore.RESET)
                    print()
                    llenar_matriz(caldo_og)
                    print(Fore.BLUE+"---Caldo de cultivo inicial---"+Fore.RESET)
                    print()
                    cambio(caldo_og, caldo_clon)
                    mostrar_matriz(caldo_og)
                    print()
                    mostrar_matriz(caldo_clon)
                    cadena_car(caldo_og)
                    aplicar_generaciones(caldo_og , caldo_clon, caldo_2)
                    break
                    
                case 2:
                    print(Fore.LIGHTRED_EX+"Opción 2: Matriz personalizada"+Fore.RESET)
                    print()
                    print(Fore.YELLOW+f'La cantidad de células que debe tener la matriz tiene que estar comprendida entre', len(caldo_og),'y', (len(caldo_og)*len(caldo_og)),''+Fore.RESET)
                    celulas = int(input(Fore.YELLOW+"¿Cuántas células quieres que haya en el caldo de cultivo?: "+Fore.RESET))
                    print()
                    while (celulas < len(caldo_og) or celulas > (len(caldo_og)*len(caldo_og))):
                            print(Fore.RED+f'ERROR. La cantidad de células que debe tener la matriz tiene que estar comprendida entre', len(caldo_og),'y', (len(caldo_og)*len(caldo_og)),''+Fore.RESET)
                            celulas = int(input(Fore.YELLOW+"Introduzca nuevamente la cantidad de células que quiere en la matriz:"+Fore.RESET))
                            print()
                    while (celulas > 0):
                        valori = random.randint(0, len(caldo_og)-1)
                        valorj = random.randint(0, len(caldo_og)-1)
                        if(caldo_og[valori, valorj] != 1):
                            caldo_og[valori, valorj] = 1
                            celulas -= 1
                    cambio(caldo_og, caldo_clon)
                    print(Fore.BLUE+"---Caldo de cultivo inicial---"+Fore.RESET)
                    print()
                    mostrar_matriz(caldo_og)
                    print()
                    mostrar_matriz(caldo_clon)
                    cadena_car(caldo_og)
                    aplicar_generaciones(caldo_og , caldo_clon, caldo_2)
                    break
                        
                case 3:
                    print(Fore.LIGHTRED_EX+"Opción 3: Matriz cargada de archivos"+Fore.RESET)
                    print()
                    leer_archivos()
                    print(Fore.BLUE+"---Caldo de cultivo inicial--- "+Fore.RESET)
                    print()
                    cambio(caldo_og, caldo_clon)
                    mostrar_matriz(caldo_clon)
                    aplicar_generaciones(caldo_og , caldo_clon, caldo_2)
                    break
                case 4:
                    print(Fore.LIGHTRED_EX+"Opción 4: Guardar y Salir"+Fore.RESET)
                    print(Fore.GREEN+"Thanks for playing *con voz de Luigi*"+Fore.RESET)
                    exit()
                case _:
                    print(Fore.RED+"ERROR: Opción no válida."+Fore.RESET)

        
    #Programa principal
    print(Fore.YELLOW +"UCAB, Realizado por: Camilo Ceci C.I. 31.707.565 , Santhiago Singer C.I. 31.160.338 , Henrique Hopkins C.I. , Diego González C.I. 31.873.850" +Fore.RESET)
    print()
    menu_principal()

main()
               
# Lista de tareas:
#
# 1. Que la cadena de caracteres (cadena_car) de las posiciones de las celulas se 
#    imprima correctamente (error con el "." final)
# 2. Que se imprima con colores las matrices de numeros (rojo para 0, azul para 1, amarillo para 2)
# 3. Poner mas bonito visualmente el programa (frontend)
# 4. Quitar comentarios trol 
# 5. Agregar comentarios explicativos en el codigo para que sea mas facil a la hora de la defensa para apoyarse
# 6. Verifiquen cedulas y nombres
# 7. (Agregar robustez) Cuando se pide la cantidad de repeticiones para saber cuantas generaciones se van a producir
#    Si colocas algo que no sea un numero explota (tal vez una funcion para no tener que repetirlo varias veces en el programa)
# 8. Trabajen perritas

