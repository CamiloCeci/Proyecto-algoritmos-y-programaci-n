import numpy as np # Asumo que 'caldo' es una matriz numpy, si no lo es, por favor indícalo
from colorama import Fore, Style # Importar Style si quieres resetear el color después de Fore.RESET

def cadena_car(caldo):
    celulas_vivas = []
    for i in range(len(caldo)):
        for j in range(len(caldo[0])):  # Asumo que caldo es una matriz rectangular, si es cuadrada puedes usar len(caldo)
            if caldo[i, j] == 1:
                celulas_vivas.append(f"({i},{j})") # Usamos f-string para formatear la tupla

    if celulas_vivas: # Solo si hay células vivas
        c1 = "Posiciones de las células: "
        c1 += ", ".join(celulas_vivas) # Unimos los elementos con ", "
        c1 += "."  # Agregamos el punto al final
    else:
        c1 = "No hay células vivas." # O el mensaje que desees si no hay células

    print(Fore.MAGENTA + c1 + Fore.RESET)

# --- Ejemplos de uso ---
# Ejemplo 1: Matriz con células
caldo1 = np.array([
    [0, 1, 0],
    [1, 0, 1],
    [0, 0, 1]
])
print("--- Ejemplo 1 ---")
cadena_car(caldo1)

# Ejemplo 2: Matriz sin células
caldo2 = np.array([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
])
print("\n--- Ejemplo 2 ---")
cadena_car(caldo2)

# Ejemplo 3: Matriz más grande (similar a tu caso de uso)
caldo3 = np.zeros((20, 20), dtype=int)
# Añadir algunas células vivas de ejemplo
caldo3[0, 2] = 1
caldo3[0, 3] = 1
caldo3[1, 5] = 1
caldo3[19, 19] = 1 # La última célula
caldo3[18, 0] = 1
caldo3[19, 0] = 1


print("\n--- Ejemplo 3 ---")
cadena_car(caldo3)