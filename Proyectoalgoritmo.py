import random
import numpy as np
import colorama
from colorama import *
init()

def main ():
    #Primer caldo de cultivo

    f1 = np.array([0]*4)
    f2 = np.array([0]*4)
    f3 = np.array([0]*4)
    f1m = np.array([0]*4)
    f2m = np.array([0]*4)
    f3m = np.array([0]*4)

    def imprimir_arreglos(f):
        print("|", end=' ')
        for i in range (0, len(f), 1):
            if(f[i] == 0): #Imprimir de rojo los que son 0
                color = Fore.RED
                print(f"{color}{f[i]}{Style.RESET_ALL}", end=' | ')
            else:   #Imprimir de azul los que son 1
                color = Fore.BLUE
                print(f"{color}{f[i]}{Style.RESET_ALL}", end=' | ')
            
            if (i == 3): #salto
                print(end='\n')

            
    def llenar_arreglos_gen0():
        for i in range (0, len(f1), 1):
            f1[i] = random.randint(0, 1)
            f2[i] = random.randint(0, 1)
            f3[i] = random.randint(0, 1) # Se quito que se rellenara la posicion 1 del areglo f2 con un  "1"

    def regla1(f1, f2, f3): #soledad (si una celda esta ocupada por una celula y tiene una sola o ninguna celula vecina muere)
        # Se aplica la regla a f1
        for i in range (0, len(f1), 1):
            if (f1[0]== 1 and i == 0):
                suma = f1[i+1] + f2[i] + f2[i+1]
                if (suma > 1):
                    f1m[i] = 1
                else:
                    f1m[i] = 0

            if (f1[3]== 1 and i == 3):
                suma = f1[i-1] + f2[i-1] + f2[i]
                if (suma > 1):
                    f1m[i] = 1
                else:
                    f1m[i] = 0
            
            else:
                if(f1[i] == 1):
                    suma = f1[i-1] + f1[i+1] + f2[i-1] + f2[i] + f2[i+1]
                    if (suma > 1):
                        f1m[i] = 1
                    else:
                        f1m[i] = 0

        # Se aplica la regla a f2
        for i in range (0, len(f2), 1):
            if (f2[0]== 1 and i == 0):
                suma = f1[i] + f1[i+1] + f2[i+1] + f3[i] + f3[i+1]
                if (suma > 1):
                    f1m[i] = 1
                else:
                    f1m[i] = 0

            if (f2[3]== 1 and i == 3):
                suma = f1[i-1] + f1[i] + f2[i-1] + f3[i-1] + f3[i]
                if (suma > 1):
                    f2m[i] = 1
                else:
                    f2m[i] = 0

            else:
                if(f2[i] == 1):
                    suma = f1[i-1] + f1[i] + f1[i+1] + f2[i-1] + f2[i+1] + f3[i-1] + f3[i] + f3[i+1]
                    if (suma > 1):
                        f2m[i] = 1
                    else:
                        f2m[i] = 0
            
        # Se aplica la regla a f3
        for i in range (0, len(f3), 1):
            if (f3[0]== 1 and i == 0):
                suma = f3[i+1] + f2[i] + f2[i+1]
                if (suma > 1):
                    f3m[i] = 1
                else:
                    f3m[i] = 0

            if (f3[3]== 1 and i == 3):
                suma = f3[i-1] + f2[i-1] + f2[i]
                if (suma > 1):
                    f3m[i] = 1
                else:
                    f3m[i] = 0

            else:
                if(f3[i] == 1):
                    suma = f3[i-1] + f3[i+1] + f2[i-1] + f2[i] + f2[i+1]
                    if (suma > 1):
                        f3m[i] = 1
                    else:
                        f3m[i] = 0

    def regla2(f1, f2, f3): #superpoblacion (si la celda esta ocupada por una celula y tiene 4 o mas celulas vecinas muere)
        # Se aplica la regla a f1
        for i in range (0, len(f1), 1):
            if (f1[0]== 1 and i == 0):
                suma = f1[i+1] + f2[i] + f2[i+1]
                if (suma >= 4):
                    f1m[i] = 0
                else:
                    f1m[i] = 1

            if (f1[3]== 1 and i == 3):
                suma = f1[i-1] + f2[i-1] + f2[i]
                if (suma >= 4):
                    f1m[i] = 0
                else:
                    f1m[i] = 1

            else:
                if(f1[i] == 1):
                    suma = f1[i-1] + f1[i+1] + f2[i-1] + f2[i] + f2[i+1]
                    if (suma >= 4):
                        f1m[i] = 0
                    else:
                        f1m[i] = 1

        # Se aplica la regla a f2
        for i in range (0, len(f2), 1):
            if (f2[0]== 1 and i == 0):
                suma = f1[i] + f1[i+1] + f2[i+1] + f3[i] + f3[i+1]
                if (suma >= 4):
                    f1m[i] = 0
                else:
                    f1m[i] = 1

            if (f2[3]== 1 and i == 3):
                suma = f1[i-1] + f1[i] + f2[i-1] + f3[i-1] + f3[i]
                if (suma >= 4):
                    f2m[i] = 0
                else:
                    f2m[i] = 1

            else:
                if(f2[i] == 1):
                    suma = f1[i-1] + f1[i] + f1[i+1] + f2[i-1] + f2[i+1] + f3[i-1] + f3[i] + f3[i+1]
                    if (suma >= 4):
                        f2m[i] = 0
                    else:
                        f2m[i] = 1
            
        #Se aplica la regla a f3
        for i in range (0, len(f3), 1):
            if (f3[0]== 1 and i == 0):
                suma = f3[i+1] + f2[i] + f2[i+1]
                if (suma >= 4):
                    f3m[i] = 0
                else:
                    f3m[i] = 1

            if (f3[3]== 1 and i == 3):
                suma = f3[i-1] + f2[i-1] + f2[i]
                if (suma >= 4):
                    f3m[i] = 0
                else:
                    f3m[i] = 1

            else:
                if(f3[i] == 1):
                    suma = f3[i-1] + f3[i+1] + f2[i-1] + f2[i] + f2[i+1]
                    if (suma >= 4):
                        f3m[i] = 0
                    else:
                        f3m[i] = 1

    def regla3(f1, f2, f3): #vecinos (si la celda esta ocupada por una celula y tiene 2 o 3 celulas vecinas sobrevive)
        # Se aplica la regla a f1
        for i in range (0, len(f1), 1):
            if (f1[0]== 0 and i == 0):
                suma = f1[i+1] + f2[i] + f2[i+1]
                if (suma == 2 or suma == 3):
                    f1m[i] = 1
                else:
                    f1m[i] = 0

            if (f1[3]== 1 and i == 3):
                suma = f1[i-1] + f2[i-1] + f2[i]
                if (suma == 2 or suma == 3):
                    f1m[i] = 1
                else:
                    f1m[i] = 0

            else:
                if(f1[i] == 0 and (i == 1 or i == 2)):
                    suma = f1[i-1] + f1[i+1] + f2[i-1] + f2[i] + f2[i+1]
                    if (suma == 2 or suma == 3):
                        f1m[i] = 1
                    else:
                        f1m[i] = 0

        # Se aplica la regla a f2
        for i in range (0, len(f2), 1):
            if (f2[0]== 0 and i == 0):
                suma = f1[i] + f1[i+1] + f2[i+1] + f3[i] + f3[i+1]
                if (suma == 2 or suma == 3):
                    f1m[i] = 1
                else:
                    f1m[i] = 0

            if (f2[3]== 0 and i == 3):
                suma = f1[i-1] + f1[i] + f2[i-1] + f3[i-1] + f3[i]
                if (suma == 2 or suma == 3):
                    f2m[i] = 1
                else:
                    f2m[i] = 0
            
            else:
                if(f2[i] == 0):
                    suma = f1[i-1] + f1[i] + f1[i+1] + f2[i-1] + f2[i+1] + f3[i-1] + f3[i] + f3[i+1]
                    if (suma == 2 or suma == 3):
                        f2m[i] = 1
                    else:
                        f2m[i] = 0
        
        # Se aplica la regla a f3
        for i in range (0, len(f3), 1):
            if (f3[0]== 0 and i == 0):
                suma = f3[i+1] + f2[i] + f2[i+1]
                if (suma == 2 or suma == 3):
                    f3m[i] = 1
                else:
                    f3m[i] = 0

            if (f3[3]== 0 and i == 3):
                suma = f3[i-1] + f2[i-1] + f2[i]
                if (suma == 2 or suma == 3):
                    f3m[i] = 1
                else:
                    f3m[i] = 0

            else:
                if(f3[i] == 0):
                    suma = f3[i-1] + f3[i+1] + f2[i-1] + f2[i] + f2[i+1]
                    if (suma == 2 or suma == 3):
                        f3m[i] = 1
                    else:
                        f3m[i] = 0

    def regla4(f1, f2, f3): #reproduccion (si la celda no esta ocupada por una celula y tiene 3 celulas vecinas, nace una nueva celula)
        # Se aplica la regla a f1
        for i in range (0, len(f1), 1):
            if (f1[0]== 0 and i == 0):
                suma = f1[i+1] + f2[i] + f2[i+1]
                if (suma == 3):
                    f1m[i] = 1
                else:
                    f1m[i] = 0

            if (f1[3]== 0 and i == 3):
                suma = f1[i-1] + f2[i-1] + f2[i]
                if (suma == 3):
                    f1m[i] = 1
                else:
                    f1m[i] = 0
        
            else:
                if(f1[i] == 0):
                    suma = f1[i-1] + f1[i+1] + f2[i-1] + f2[i] + f2[i+1]
                    if (suma == 3):
                        f1m[i] = 1
                    else:
                        f1m[i] = 0

        # Se aplica la regla a f2
        for i in range (0, len(f2), 1):
            if (f2[0]== 0 and i == 0):
                suma = f1[i] + f1[i+1] + f2[i+1] + f3[i] + f3[i+1]
                if (suma == 3):
                    f1m[i] = 1
                else:
                    f1m[i] = 0

            if (f2[3]== 0 and i == 3):
                suma = f1[i-1] + f1[i] + f2[i-1] + f3[i-1] + f3[i]
                if (suma == 3):
                    f2m[i] = 1
                else:
                    f2m[i] = 0


            else:
                if(f2[i] == 0):
                    suma = f1[i-1] + f1[i] + f1[i+1] + f2[i-1] + f2[i+1] + f3[i-1] + f3[i] + f3[i+1]
                    if (suma == 3):
                        f2m[i] = 1
                    else:
                        f2m[i] = 0

        # Se aplica la regla a f3
        for i in range (0, len(f3), 1):
            if (f3[0]== 0 and i == 0):
                suma = f3[i+1] + f2[i] + f2[i+1]
                if (suma == 3):
                    f3m[i] = 1
                else:
                    f3m[i] = 0

            if (f3[3]== 0 and i == 3):
                suma = f3[i-1] + f2[i-1] + f2[i]
                if (suma == 3):
                    f3m[i] = 1
                else:
                    f3m[i] = 0

            else:
                if(f3[i] == 0):
                    suma = f3[i-1] + f3[i+1] + f2[i-1] + f2[i] + f2[i+1]
                    if (suma == 3):
                        f3m[i] = 1
                    else:
                        f3m[i] = 0

    #programa
    print(Fore.YELLOW +"UCAB, Realizado por: Camilo Ceci C.I. 31.707.565 , Santhiago Singer C.I. , Henrique Hopkins C.I. , Diego González C.I. 31.873.850" +Fore.RESET)
        
    llenar_arreglos_gen0()
    print(Fore.CYAN +"Caldo de cultivo" + Fore.RESET)
    imprimir_arreglos(f1)
    imprimir_arreglos(f2)
    imprimir_arreglos(f3)
    regla1(f1, f2, f3)
    regla2(f1m, f2m, f3m) 
    regla3(f1m, f2m, f3m) # Se agrego regla 3 por pedido del profesor 
    regla4(f1m, f2m, f3m)
    print(Fore.GREEN +"Primera Generación"+ Fore.RESET) # Ya no es caldo cultivo modificado sino Primera generacion
    imprimir_arreglos(f1m)
    imprimir_arreglos(f2m)
    imprimir_arreglos(f3m)
    # Se agrego la cadena c1 para el avance 2 y esta guarda el nombre del arreglo y los valores del mismo

    c1 = ""
    c1 += "f1m "
    for i in range (0, len(f1m), 1):
        c1 += "(0,"
        c1 += str((i))
        c1 += ") "
        c1 += "["
        c1 += str(f1m[i])
        c1 += "] "
    c1 += ", f2m "
    for i in range (0, len(f2m), 1):
        c1 += "(1,"
        c1 += str((i))
        c1 += ") "
        c1 += "["
        c1 += str(f2m[i])
        c1 += "] "
    c1 += ", f3m "
    for i in range (0, len(f3m), 1):
        if (i <= 2):
            c1 += "(2,"
            c1 += str((i))
            c1 += ") "
            c1 += "["
            c1 += str(f3m[i])
            c1 += "] "
        else:
            c1 += "(2,"
            c1 += str((i))
            c1 += ") "
            c1 += "["
            c1 += str(f3m[i])
            c1 += "]"
    c1 += "."
    print(Fore.MAGENTA + "Cadena C1: " + c1 + Fore.RESET)

main()