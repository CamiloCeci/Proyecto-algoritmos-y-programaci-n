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
            f3[i] = random.randint(0, 1)
        f2[1] = 1

    def regla1(f1, f2, f3): #soledad
        for i in range (0, len(f2), 1):
            if (f2[3]== 1):
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

    def regla2(f1, f2, f3): #superpoblacion
        for i in range (0, len(f2), 1):
            if (f2[3]== 1):
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

    def regla4(f1, f2, f3): #reproduccion
        for i in range (0, len(f2), 1):
            if (f2[3]== 0):
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

    #programa
    print(Fore.YELLOW +"UCAB, Realizado por: Camilo Ceci C.I. 31.707.565 , Santhiago Singer C.I. , Henrique Hopkins C.I. , Diego González C.I." +Fore.RESET)
        
    llenar_arreglos_gen0()
    print(Fore.CYAN +"Caldo de cultivo" + Fore.RESET)
    imprimir_arreglos(f1)
    imprimir_arreglos(f2)
    imprimir_arreglos(f3)
    regla1(f1, f2, f3)
    regla2(f1, f2m, f3) #Regla 3 ya esta comprendida entre regla 1 y 2
    regla4(f1, f2m, f3)
    print(Fore.GREEN +"Caldo de cultivo modificado" + Fore.RESET)
    imprimir_arreglos(f1)
    imprimir_arreglos(f2m)
    imprimir_arreglos(f3)
main()