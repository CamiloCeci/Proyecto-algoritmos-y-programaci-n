import random
import numpy as np
import colorama
from colorama import *
import os
init()

def main ():
    # Inicialización de las matrices principales para la simulación del Caldo de Cultivo.
    caldo_og = np.full((20,20),0)
    caldo_2 = np.full((20,20),0)
    caldo_clon = np.full((20,20)," ")

    def cadena_car(caldo): 
        """
        Genera una cadena de texto que lista las coordenadas de todas las células vivas (valor 1).
        Formatea cada coordenada con colores y añade un punto al final de la cadena.
        """
        c1 = ""
        # Recorre toda la matriz para encontrar células vivas.
        for i in range (0, len(caldo), 1):
            for j in range(0, len(caldo), 1):
                # Si encuentra una célula viva (valor 1), añade sus coordenadas a la cadena.
                if (caldo[i,j] == 1):
                    c1 += Fore.MAGENTA+"(" # Color magenta para el paréntesis de apertura
                    c1 += Fore.GREEN+str((i)) # Color verde para la coordenada de fila
                    c1 += Fore.MAGENTA+"," # Color magenta para la coma
                    c1 += Fore.GREEN+str((j)) # Color verde para la coordenada de columna
                    c1 += Fore.MAGENTA+"), " # Color magenta para el paréntesis de cierre y la coma separadora

        # Añade un punto al final de la cadena de coordenadas.
        c1 += Fore.MAGENTA+"."

        print()
        print(Fore.CYAN+"----- Posiciones de las células -----"+Fore.RESET) # Título de la sección en cian
        print()
        print(c1 + Fore.RESET) # Imprime la cadena de coordenadas y resetea el color
        print()

    def llenar_matriz(caldo_og):
        """
        Rellena la matriz 'caldo_og' con valores aleatorios de 0 o 1.
        0 representa una celda vacía, y 1 representa una célula viva.
        """
        for i in range(0,len(caldo_og),1):
            for j in range(0,len(caldo_og),1):
                caldo_og[i,j] = random.randint(0,1)

    def mostrar_matriz(caldo):
        """
        Imprime la matriz en la consola, asignando un color diferente a cada valor de celda:
        - Rojo para 0 (celda vacía)
        - Azul para 1 (célula viva)
        - Amarillo para 2 (célula especial/milagro)
        """
        print(Fore.GREEN+"Los elementos de la Matriz son:"+Fore.RESET) # Título en verde
        for i in range(0,len(caldo),1):
            for j in range(0,len(caldo),1):
                valor = caldo[i,j]
                if valor == 0:
                    print(Fore.RED + str(valor) + Fore.RESET, end=" ") # 0 en rojo
                elif valor == 1:
                    print(Fore.BLUE + str(valor) + Fore.RESET, end=" ") # 1 en azul
                elif valor == 2:
                    print(Fore.YELLOW + str(valor) + Fore.RESET, end=" ") # 2 en amarillo
                else:
                    print(str(valor), end=" ") # Otros valores sin color (para robustez, aunque no deberían aparecer)
            print() # Salto de línea para la siguiente fila

    def aplicar_reglas(suma, i, j, caldo_2, caldo_og):
        """
        Aplica las reglas del "Juego de la Vida" a una celda específica (i, j)
        basándose en el número de células vecinas vivas (suma).
        Los resultados se almacenan en 'caldo_2' para la próxima generación.
        """
        # Regla 1: Soledad (si una celda esta ocupada por una celula y tiene una sola o ninguna celula vecina muere)
        # Una célula (1 o 2) con 0 o 1 vecino muere (se convierte en 0).
        if ((suma <= 1) and (caldo_og[i,j] == 1 or caldo_og[i,j] == 2)):
            caldo_2[i,j] = 0
        # Regla 2: Superpoblación (si la celda esta ocupada por una celula y tiene 4 o mas celulas vecinas muere)
        # Una célula (1 o 2) con 4 o más vecinos muere (se convierte en 0).
        elif ((suma >= 4) and (caldo_og[i,j] == 1 or caldo_og[i,j] == 2)):
            caldo_2[i,j] = 0
        # Regla 3: Vecinos (si la celda esta ocupada por una celula y tiene 2 o 3 celulas vecinas sobrevive)
        # Una célula (1 o 2) con 2 o 3 vecinos sobrevive (se mantiene en 1).
        elif((suma == 2 or suma == 3) and (caldo_og[i,j] == 1 or caldo_og[i,j] == 2)):
            caldo_2[i,j] = 1
        # Regla 4: Reproducción (si la celda no esta ocupada y tiene 3 celulas vecinas, nace una nueva celula)
        # Una celda vacía (0) con exactamente 3 vecinos se convierte en una célula viva (1).
        elif((suma == 3) and (caldo_og[i,j] == 0)):
            caldo_2[i,j] = 1
        # Si ninguna regla aplica, la celda mantiene su estado actual (importante para células 0 sin 3 vecinos).

    def mutacion(caldo_og , caldo_2):
        """
        Calcula la próxima generación del caldo de cultivo iterando sobre cada celda,
        sumando sus vecinos y aplicando las reglas del Juego de la Vida.
        Considera casos especiales para esquinas y bordes.
        """
        suma = 0

        # Caso esquinas: Se calculan los vecinos y se aplican las reglas para cada una de las 4 esquinas.
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

        # Iteración general sobre la matriz para casos de bordes y el caso normal.
        for i in range(0,len(caldo_og),1):
            for j in range(0,len(caldo_og),1):

                # Caso bordes: Se calculan los vecinos y se aplican las reglas para celdas en los bordes.
                if (i == 0 and (0 < j < len(caldo_og) - 1)):
                    suma = caldo_og[i,j-1] + caldo_og[i,j+1] + caldo_og[i+1,j-1] + caldo_og[i+1,j] + caldo_og[i+1,j+1]
                    aplicar_reglas(suma , i , j, caldo_2, caldo_og)

                elif (j == 0 and (0 < i < len(caldo_og) - 1)):
                    suma = caldo_og[i-1,j] + caldo_og[i-1,j+1] + caldo_og[i,j+1] + caldo_og[i+1,j] + caldo_og[i+1,j+1]
                    aplicar_reglas(suma , i , j, caldo_2, caldo_og)

                elif (i == len(caldo_og)-1 and (0 < j < len(caldo_og)-1)):
                    suma = caldo_og[i-1,j-1] + caldo_og[i-1,j] + caldo_og[i-1,j+1] + caldo_og[i,j-1] + caldo_og[i,j+1]
                    aplicar_reglas(suma , i , j, caldo_2, caldo_og)

                elif(j == len(caldo_og)-1 and (0 < i < len(caldo_og)-1)):
                    suma = caldo_og[i-1,j-1] + caldo_og[i-1,j] + caldo_og[i,j-1] + caldo_og[i+1,j-1] + caldo_og[i+1,j]
                    aplicar_reglas(suma , i , j, caldo_2, caldo_og)

                elif((0 < i < len(caldo_og)-1) and ((0 < j < len(caldo_og)-1))):
                    suma = caldo_og[i-1,j-1] + caldo_og[i-1,j] + caldo_og[i-1,j+1] + caldo_og[i,j-1] + caldo_og[i,j+1] + caldo_og[i+1,j-1] + caldo_og[i+1,j] + caldo_og[i+1,j+1]
                    aplicar_reglas(suma , i , j, caldo_2, caldo_og)

    def cambio(caldo_2 , caldo_clon):
        """
        Convierte la matriz numérica (0, 1, 2) en una matriz de emojis para visualización.
        - 0 se convierte en "🟥" (cuadrado rojo)
        - 1 se convierte en "🟦" (cuadrado azul)
        - 2 se convierte en "🟨" (cuadrado amarillo)
        """
        for i in range(0,len(caldo_clon),1):
            for j in range(0,len(caldo_clon),1):
                if(caldo_2[i,j]== 0):
                    caldo_clon[i,j] = "🟥"
                elif(caldo_2[i,j]== 1):
                    caldo_clon[i,j] = "🟦"
                elif(caldo_2[i,j]== 2):
                    caldo_clon[i,j] = "🟨"

    # MILAGROS

    def milagro1(caldo): 
        """
        Primer Milagro: Evalúa un porcentaje de ocupación en celdas con coordenadas impares.
        Si el porcentaje es >= 50%, la primera celda vacía se convierte en una célula especial (2).
        El recorrido espiral está implementado para la suma, pero el criterio es sobre coordenadas impares.
        """
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

        # NUEVOS CONTADORES para milagro 1: Cuentan las celdas con coordenadas impares
        contador_coord_impares = 0
        contador_ocupadas = 0

        while celdasvisitadas < totalceldas:
            # 1. Derecha →
            for c in range(columna, limderecha + 1):
                if celdasvisitadas < totalceldas:
                    recorrido_elementos[e] = caldo[fila, c]
                    # Verifica si la fila y la columna son impares
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
                    # Verifica si la fila y la columna son impares
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
                    # Verifica si la fila y la columna son impares
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
                    # Verifica si la fila y la columna son impares
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
        if contador_coord_impares > 0: # Evita división por cero si no hay coordenadas impares
            porcentaje = (contador_ocupadas * 100) // contador_coord_impares
            print(f"Milagro 1: {porcentaje}% de ocupación en coordenadas impares")
            if porcentaje >= 50:
                print("✨ ¡Condición para Milagro 1 cumplida!")
                # Busca la primera celda vacía (0) y la convierte en 2 (célula milagro)
                for i in range(0,len(caldo),1):
                    for j in range(0,len(caldo),1):
                        if (caldo[i,j] == 0):
                            caldo[i,j] = 2
                            return # Sale después de aplicar el milagro a una celda
            else:
                print("⚠️ No se cumple la condición para Milagro 1")
        else:
            print("No se encontraron coordenadas con ambos índices impares para evaluar el Milagro 1.")


    def milagro2(caldo):
        """
        Segundo Milagro: Evalúa el porcentaje de ocupación en celdas cuya coordenada X (fila) es par.
        Si el porcentaje es >= 70%, la primera celda vacía en una fila par se convierte en una célula especial (2).
        """
        contador_x_par = 0      # Cuenta todas las celdas en filas con índice par
        contador_x_ocupados = 0 # Cuenta las celdas vivas (1) en filas con índice par

        # Recorre la matriz para contar las celdas en filas pares.
        for i in range(0, len(caldo), 1):
            if (i % 2 == 0): # Si el índice de la fila es par
                for j in range(0 , len(caldo[0]) , 1):
                    contador_x_par += 1
                    if(caldo[i,j] == 1): # Si la celda está ocupada
                        contador_x_ocupados += 1

        if (contador_x_par > 0): 
            porcentaje = (contador_x_ocupados * 100) // contador_x_par
            print(f"Milagro 2: {porcentaje}% de ocupación en filas con índice par.")
            if porcentaje >= 70:
                print("✨ ¡Condición para Milagro 2 cumplida!")
                for i in range(0, len(caldo), 1):
                    if (i % 2 == 0): 
                        for j in range(0 , len(caldo[0]) , 1):
                            if (caldo[i,j] == 0):
                                caldo[i,j] = 2
                                return 
            else:
                print("⚠️ No se cumple la condición para Milagro 2")
        else:
            print("No se encontraron celdas en filas con índice par para evaluar el Milagro 2.")

    def milagro3(caldo):
        """
        Tercer Milagro: Evalúa el porcentaje de ocupación en celdas cuya coordenada Y (columna) es impar.
        Si el porcentaje es >= 60%, la primera celda vacía en una columna impar se convierte en una célula especial (2).
        """
        contador_y_impares = 0 # Cuenta todas las celdas en columnas con índice impar
        contador_y_ocupadas = 0 # Cuenta las celdas vivas (1) en columnas con índice impar

        # Recorre la matriz para contar las celdas en columnas impares.
        for j in range(0, len(caldo[0]), 1): # Itera sobre las columnas
            if (j % 2 != 0): # Si el índice de la columna es impar
                for i in range (0, len(caldo), 1): # Itera sobre las filas
                    contador_y_impares += 1
                    if (caldo[i,j]== 1): # Si la celda está ocupada
                        contador_y_ocupadas += 1

        if (contador_y_impares > 0): # Evita división por cero
            porcentaje = (contador_y_ocupadas * 100) // contador_y_impares
            print(f"Milagro 3: {porcentaje}% de ocupación en columnas con índice impar.")
            if porcentaje >= 60:
                print("✨ ¡Condición para Milagro 3 cumplida!")
                # Si la condición se cumple, busca la primera celda vacía (0) en una columna impar
                # y la convierte en una célula especial (2).
                for i in range(0,len(caldo),1):
                    for j in range(0,len(caldo),1):
                        if (j % 2 != 0): # Solo busca en columnas con índice impar
                            if (caldo[i,j] == 0):
                                caldo[i,j] = 2
                                return # Sale después de aplicar el milagro a una celda
            else:
                print("⚠️ No se cumple la condición para Milagro 3")
        else:
            print("No se encontraron celdas en columnas con índice impar para evaluar el Milagro 3.")

    def menu_milagros(caldo):
        """
        Muestra un menú interactivo para que el usuario seleccione y active uno de los milagros.
        Después de activar un milagro, muestra el estado actualizado del caldo.
        """
        opcion = 0
        verdad = False

        while True:
            print(Fore.MAGENTA + "=====================================")
            print(Fore.YELLOW + "          MENU DE MILAGROS           ")
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
                if (opcion > 0 and opcion < 5): 
                    verdad = True
                else:
                    print(Fore.RED+"ERROR: Ingrese un número válido (1-4)."+Fore.RESET)

            match opcion:
                case 1:
                    print("✨ Ejecutando el Primer Milagro...")
                    milagro1(caldo) # Llama a la función del primer milagro
                    cambio(caldo, caldo_clon) # Actualiza la representación visual con emojis
                    mostrar_matriz(caldo) # Muestra la matriz numérica actualizada
                    print()
                    mostrar_matriz(caldo_clon) # Muestra la matriz con emojis
                    guardar_archivo(caldo) # Guarda el estado actual del caldo
                    break # Sale del menú de milagros
                case 2:
                    print("✨ Ejecutando el Segundo Milagro...")
                    milagro2(caldo) # Llama a la función del segundo milagro
                    cambio(caldo, caldo_clon)
                    mostrar_matriz(caldo)
                    print()
                    mostrar_matriz(caldo_clon)
                    guardar_archivo(caldo)
                    break
                case 3:
                    print("✨ Ejecutando el Tercer Milagro...")
                    milagro3(caldo) # Llama a la función del tercer milagro
                    cambio(caldo, caldo_clon)
                    mostrar_matriz(caldo)
                    print()
                    mostrar_matriz(caldo_clon)
                    guardar_archivo(caldo)
                    break
                case 4:
                    print("Volviendo al menú principal...")
                    break # Sale del menú de milagros para regresar al menú principal
                case _:
                    print(Fore.RED+"ERROR: Opción no válida."+Fore.RESET) # Mensaje de error para opción inválida

    def leer_archivos():
        """
        Lee los datos de una matriz desde el archivo "utileria/archivo.txt".
        Cada línea del archivo se espera que contenga un número.
        Los números se cargan en la matriz 'caldo_og'.
        """
        caldo_temp = np.full((20, 20), 0) # Matriz temporal para la lectura
        nombre_arc = input(Fore.YELLOW+"Introduce el nombre del archivo (con extensión), ej:archivo.txt: "+Fore.RESET)

        if not os.path.isfile(nombre_arc): #esta es una verificacion que encontramos en internet para ver si si existe
            print(Fore.RED + f"ERROR: El archivo '{nombre_arc}' no existe. Saliendo del programa." + Fore.RESET)
            exit() #Nos salimos del programa si no existe como una combeniencia para nosotros y como es al inicio, no importa si se pierde el caldo_og

        arch2 = open(nombre_arc, "rt")
        i = 0
        j = 0
        for linea in arch2:
            numero = int(linea[0]) 
            caldo_temp[i,j] = numero 
            j += 1 
            if j == len(caldo_temp): 
                j = 0 
                i += 1 
            if i == len(caldo_temp): 
                break 
        arch2.close() 
        copiar_matriz_origendestino(caldo_temp , caldo_og) 
        


    def guardar_archivo(caldo):
        """
        Guarda el estado actual de la matriz 'caldo' en dos archivos:
        - 'datos.txt': Guarda cada valor numérico en una nueva línea.
        - 'datos.bin': Guarda la representación binaria de cada valor en una nueva línea.
        """
        archivo = open('datos.txt', 'wt')
        archivo2 = open('datos.bin', 'wt')

        # Escribir información en datos.bin (representación binaria)
        for i in range(0, len(caldo), 1):
            for j in range(0, len(caldo), 1):
                num = bin(caldo[i,j]) # Convierte el número a su representación binaria (e.g., 0b0, 0b1)
                archivo2.write(f'{num}\n') # Escribe la representación binaria y un salto de línea

        # Escribir información en datos.txt (valor numérico directo)
        for i in range(0, len(caldo), 1):
            for j in range(0, len(caldo), 1):
                num = caldo[i,j]
                archivo.write(f'{num}\n') # Escribe el número y un salto de línea

        # Cerrar los archivos para asegurar que los datos se guarden correctamente
        archivo.close()
        archivo2.close()

    def alguna_viva(caldo):
        """
        Verifica si existe al menos una célula viva (valor 1) en la matriz.
        Útil para determinar si la simulación debe continuar o si todas las células han muerto.
        """
        for i in range(0, len(caldo), 1):
            for j in range(0, len(caldo), 1):
                if(caldo[i,j] == 1):
                    return True # Retorna True tan pronto como encuentra una célula viva
        return False # Si no se encuentra ninguna célula viva después de revisar toda la matriz, retorna False

    def copiar_matriz_origendestino(caldo_origen , caldo_destino):
        """
        Copia todos los elementos de la matriz 'caldo_origen' a la matriz 'caldo_destino'.
        Esto es crucial para actualizar el estado del caldo entre generaciones sin referencia directa.
        """
        for i in range(0,len(caldo_origen),1):
            for j in range(0,len(caldo_origen),1):
                caldo_destino[i,j] = caldo_origen[i,j]

    def aplicar_generaciones(caldo_og , caldo_clon, caldo_2):
        """
        Controla el flujo de las generaciones del Juego de la Vida.
        Solicita al usuario el número de generaciones a simular,
        alterna entre matrices para el cálculo de la próxima generación,
        muestra el estado en cada paso y verifica la extinción de células.
        """
        caldillo = np.full((20,20),0) # Matriz para guardar el estado final de la simulación de generaciones
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
            if(generacion%2 == 1): # Si es una generación impar, caldo_og es la base, caldo_2 el resultado
                mutacion(caldo_og, caldo_2) # Calcula la nueva generación en caldo_2
                cambio(caldo_2, caldo_clon) # Actualiza la matriz de emojis
                print(Fore.BLUE+f'------ Generación ',generacion,'------'+Fore.RESET) # Imprime el número de generación
                print()
                mostrar_matriz(caldo_2) # Muestra la matriz numérica de la nueva generación
                print()
                mostrar_matriz(caldo_clon) # Muestra la matriz de emojis
                cadena_car(caldo_2) # Muestra las coordenadas de las células vivas
                pausa = input(Fore.YELLOW+"Pulse cualquier tecla para continuar: "+Fore.RESET) # Pausa para la visibilidad
                print()
                if (alguna_viva(caldo_2) == False): # Verifica si todas las células han muerto
                    print(Fore.BLUE+f'Todas las celulas murieron en la generacion: ', generacion,''+Fore.RESET)
                    print()
                    mostrar_matriz(caldo_2)
                    break 
                copiar_matriz_origendestino(caldo_2, caldillo) 

            else: # Si es una generación par, caldo_2 es la base, caldo_og el resultado
                mutacion(caldo_2, caldo_og) # Calcula la nueva generación en caldo_og
                cambio(caldo_og, caldo_clon) # Actualiza la matriz de emojis
                print(Fore.BLUE+f'------ Generación ',generacion,'------'+Fore.RESET)
                print()
                mostrar_matriz(caldo_og)
                print()
                mostrar_matriz(caldo_clon)
                cadena_car(caldo_og)
                pausa = input(Fore.YELLOW+"Pulse cualquier tecla para continuar: "+Fore.RESET)
                if (alguna_viva(caldo_og) == False): # Verifica si todas las células han muerto
                    print("Todas las celulas murieron en la generacion: " , generacion) # Posible agregar pausa (revisar)
                    print()
                    mostrar_matriz(caldo_og)
                    break # Termina la simulación
                copiar_matriz_origendestino(caldo_og, caldillo) # Guarda la última matriz activa en 'caldillo'

        # Pregunta al usuario si desea aplicar algún milagro después de las generaciones.
        validador = input(Fore.YELLOW+"¿Quieres implementar algun milagro? (si/no): "+Fore.RESET)
        print()
        # Validación de la respuesta del usuario (si/no, insensible a mayúsculas/minúsculas)
        while (validador != "si" and validador != "no" and validador != "SI" and validador != "NO" and validador != "Si" and validador != "No"):
            print(Fore.RED+"ERROR: Ingrese una opción válida (si/no)."+Fore.RESET)
            validador = input(Fore.YELLOW+"Responde nuevamente con si o no: "+Fore.RESET)
            print()
        if (validador == "si" or validador == "SI" or validador == "Si"): # Si la respuesta es afirmativa, abre el menú de milagros
            menu_milagros(caldillo) # Pasa la matriz final de las generaciones al menú de milagros

    def menu_principal():
        """
        Muestra el menú principal de la aplicación, permitiendo al usuario elegir
        cómo inicializar el caldo de cultivo o salir del programa.
        """
        opcion = 0
        verdad = False # Variable para controlar la validación de la entrada

        while True:
            # Imprime el menú principal con formato y colores
            print(Fore.MAGENTA+"=====================================")
            print(Fore.YELLOW+"          MENU PRINCIPAL             ")
            print(Fore.MAGENTA+"=====================================")
            print(Fore.CYAN+" 1. Generar matriz aleatoriamente    ")
            print(" 2. Matriz personalizada             ")
            print(" 3. Matriz cargada de archivos       ")
            print(Fore.MAGENTA+"-------------------------------------")
            print(Fore.CYAN+" 4. Guardar y Salir                  ")
            print(Fore.MAGENTA+"======================================"+Fore.RESET)

            # Bucle para validar la entrada del usuario en el menú
            while (verdad ==  False):
                opcion = int(input(Fore.YELLOW+"Seleccione una opción: "+Fore.RESET))
                print()
                if (opcion > 0 and opcion < 5): 
                    verdad = True
                else:
                    print(Fore.RED+"ERROR: Ingrese un número válido (1-4)."+Fore.RESET)


            # Utiliza match-case para ejecutar la opción seleccionada por el usuario
            match opcion:
                case 1:
                    print(Fore.LIGHTRED_EX+"Opción 1: Generar matriz aleatoriamente"+Fore.RESET)
                    print()
                    llenar_matriz(caldo_og) # Llama a la función para llenar la matriz aleatoriamente
                    print(Fore.BLUE+"---Caldo de cultivo inicial---"+Fore.RESET)
                    print()
                    cambio(caldo_og, caldo_clon) # Convierte la matriz numérica a su representación con emojis
                    mostrar_matriz(caldo_og) # Muestra la matriz numérica original
                    print()
                    mostrar_matriz(caldo_clon) # Muestra la matriz con emojis
                    cadena_car(caldo_og) # Muestra las coordenadas de las células vivas
                    aplicar_generaciones(caldo_og , caldo_clon, caldo_2) # Inicia la simulación de generaciones
                    break 
                case 2:
                    print(Fore.LIGHTRED_EX+"Opción 2: Matriz personalizada"+Fore.RESET)
                    print()
                    # Instrucciones para el usuario sobre el rango de células
                    print(Fore.YELLOW+f'La cantidad de células que debe tener la matriz tiene que estar comprendida entre', len(caldo_og),'y', (len(caldo_og)*len(caldo_og)),''+Fore.RESET)
                    celulas = int(input(Fore.YELLOW+"Cuántas células quieres que haya en el caldo de cultivo?: "+Fore.RESET))
                    print()
                    while (celulas < len(caldo_og) or celulas > (len(caldo_og)*len(caldo_og))):
                        print(Fore.RED+f'ERROR. La cantidad de células que debe tener la matriz tiene que estar comprendida entre', len(caldo_og),'y', (len(caldo_og)*len(caldo_og)),''+Fore.RESET)
                        celulas = int(input(Fore.YELLOW+"Introduzca nuevamente la cantidad de células que quiere en la matriz:"+Fore.RESET))
                        print()
                    # Coloca las células en posiciones aleatorias 
                    while (celulas > 0):
                        valori = random.randint(0, len(caldo_og)-1)
                        valorj = random.randint(0, len(caldo_og)-1)
                        if(caldo_og[valori, valorj] != 1): # Si la celda no está ocupada, la ocupa
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
                    print(Fore.LIGHTRED_EX+"Opcion 3: Matriz cargada de archivos"+Fore.RESET)
                    print()
                    leer_archivos() 
                    print(Fore.BLUE+"---Caldo de cultivo inicial--- "+Fore.RESET)
                    print()
                    cambio(caldo_og, caldo_clon)
                    mostrar_matriz(caldo_og) 
                    print()
                    mostrar_matriz(caldo_clon)
                    aplicar_generaciones(caldo_og , caldo_clon, caldo_2)
                    break
                case 4:
                    print(Fore.LIGHTRED_EX+"Opcion 4: Guardar y Salir"+Fore.RESET)
                    exit()
                case _:
                    print(Fore.RED+"ERROR: Opcion no valida."+Fore.RESET) 

   
    print(Fore.YELLOW +"UCAB, Realizado por: Camilo Ceci C.I. 31.707.565 , Santhiago Singer C.I. 31.160.338 , Henrique Hopkins C.I. 32.104.763 , Diego González C.I. 31.873.854" +Fore.RESET)
    print()
    menu_principal() 

main()