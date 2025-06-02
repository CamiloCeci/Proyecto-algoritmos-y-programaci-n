import random
import numpy as np
import colorama
from colorama import *
init()

def main():
    # Definición de los arreglos
    n = 4  # Tamaño de los arreglos
    f1 = np.array([0]*n)
    f2 = np.array([0]*n)
    f3 = np.array([0]*n)
    f1m = np.array([0]*n)
    f2m = np.array([0]*n)
    f3m = np.array([0]*n)

    def imprimir_arreglos(f):
        print("|", end=' ')
        for i in range(len(f)):
            if f[i] == 0:  # Imprimir de rojo los que son 0
                color = Fore.RED
                print(f"{color}{f[i]}{Style.RESET_ALL}", end=' | ')
            else:  # Imprimir de azul los que son 1
                color = Fore.BLUE
                print(f"{color}{f[i]}{Style.RESET_ALL}", end=' | ')
        print()  # Salto de línea

    def llenar_arreglos_gen0():
        for i in range(n):
            f1[i] = random.randint(0, 1)
            f2[i] = random.randint(0, 1)
            f3[i] = random.randint(0, 1)

    def aplicar_reglas(f1, f2, f3, f1m, f2m, f3m):
        # Aplicar las reglas de la vida a cada arreglo
        for i in range(n):
            # Regla 1: Soledad
            suma_f1 = (f1[i-1] if i > 0 else 0) + (f1[i+1] if i < n-1 else 0) + f2[i]
            f1m[i] = 1 if f1[i] == 1 and suma_f1 > 1 else 0

            suma_f2 = (f2[i-1] if i > 0 else 0) + (f2[i+1] if i < n-1 else 0) + f1[i] + f3[i]
            f2m[i] = 1 if f2[i] == 1 and suma_f2 > 1 else 0

            suma_f3 = (f3[i-1] if i > 0 else 0) + (f3[i+1] if i < n-1 else 0) + f2[i]
            f3m[i] = 1 if f3[i] == 1 and suma_f3 > 1 else 0

            # Regla 2: Superpoblación
            if f1[i] == 1 and suma_f1 >= 4:
                f1m[i] = 0
            if f2[i] == 1 and suma_f2 >= 4:
                f2m[i] = 0
            if f3[i] == 1 and suma_f3 >= 4:
                f3m[i] = 0

            # Regla 3: Sobrevivencia
            if f1[i] == 1 and (suma_f1 == 2 or suma_f1 == 3):
                f1m[i] = 1
            if f2[i] == 1 and (suma_f2 == 2 or suma_f2 == 3):
                f2m[i] = 1
            if f3[i] == 1 and (suma_f3 == 2 or suma_f3 == 3):
                f3m[i] = 1

            # Regla 4: Reproducción
            if f1[i] == 0 and suma_f1 == 3:
                f1m[i] = 1
            if f2[i] == 0 and suma_f2 == 3:
                f2m[i] = 1
            if f3[i] == 0 and suma_f3 == 3:
                f3m[i] = 1

    # Programa principal
    print(Fore.YELLOW + "UCAB, Realizado por: Camilo Ceci C.I. 31.707.565 , Santhiago Singer C.I. , Henrique Hopkins C.I. , Diego González C.I. 31.873.850" + Fore.RESET)

    llenar_arreglos_gen0()
    print(Fore.CYAN + "Caldo de cultivo" + Fore.RESET)
    imprimir_arreglos(f1)
    imprimir_arreglos(f2)
    imprimir_arreglos(f3)

    aplicar_reglas(f1, f2, f3, f1m, f2m, f3m)

    print(Fore.GREEN + "Primera Generación" + Fore.RESET)
    imprimir_arreglos(f1m)
    imprimir_arreglos(f2m)
    imprimir_arreglos(f3m)

    # Generar cadena de caracteres
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