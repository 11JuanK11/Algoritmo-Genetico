import random
import copy
import tkinter as tk

# Piezas de ajedrez
origen = [' ', '♟', '♞', '♝', '♜', '♛', '♚', '♙', '♘', '♗', '♖', '♕', '♔']

# Tablero objetivo
destino = [
    ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖'],
    ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
    ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']
]

def definir_poblacion():
    return [[random.choice(origen) for _ in range(8)] for _ in range(8)]

def funcion_objetivo(individuo):
    return sum(1 for i in range(8) for j in range(8) if individuo[i][j] == destino[i][j])

def cruce(individuo, destino):
    individuo_cruzado = copy.deepcopy(individuo)
    fila = random.randint(0, 5)
    columna = random.randint(0, 5)
    
    for i in range(fila, fila + 3):
        for j in range(columna, columna + 3):
            individuo_cruzado[i][j] = destino[i][j]
    
    return individuo_cruzado

def mutacion(individuo, origen):
    individuo_mutado = copy.deepcopy(individuo)
    fila = random.randint(0, 6)
    columna = random.randint(0, 6)
    
    for i in range(fila, fila + 2):
        for j in range(columna, columna + 2):
            nuevo_valor = random.choice(origen)
            if individuo_mutado[i][j] != nuevo_valor:
                individuo_mutado[i][j] = nuevo_valor
    
    return individuo_mutado

def dibujar_tablero(frame, tablero, es_hijo=False):
    for widget in frame.winfo_children():
        widget.destroy()

    for i in range(8):
        for j in range(8):
            pieza = tablero[i][j]
            color = "#DDB88C" if (i + j) % 2 == 0 else "#A66D4F"  # Alternar colores del tablero
            
            if es_hijo and tablero[i][j] == destino[i][j]:  # Resaltar piezas correctas en verde
                color = "#4CAF50"

            label = tk.Label(frame, text=pieza, font=("Arial", 24), width=2, height=1, bg=color)
            label.grid(row=i, column=j, padx=2, pady=2)

def iniciar_interfaz(padre, hijo):
    root = tk.Tk()
    root.title("Evolución del Tablero de Ajedrez")

    tk.Label(root, text="Tablero Inicial", font=("Arial", 14, "bold")).grid(row=0, column=0)
    tk.Label(root, text="Tablero Final", font=("Arial", 14, "bold")).grid(row=0, column=1)

    frame_padre = tk.Frame(root, borderwidth=2, relief="solid")
    frame_padre.grid(row=1, column=0, padx=10, pady=10)

    frame_hijo = tk.Frame(root, borderwidth=2, relief="solid")
    frame_hijo.grid(row=1, column=1, padx=10, pady=10)

    dibujar_tablero(frame_padre, padre)
    dibujar_tablero(frame_hijo, hijo, es_hijo=True)

    root.mainloop()

def mostrar_poblacion(poblacion):
    for i in range(0,len(poblacion)):
        individuo = poblacion[i]
        for i in range(0,8):
            string = ""
            for j in range(0,8):
                string += individuo[i][j] + " "
            print(string)
        print("")

# Parámetros de evolución
PROBABILIDAD_MUTACION = 0.4
PROBABILIDAD_CRUCE = 0.5

padre = definir_poblacion()
adaptacion_padre = funcion_objetivo(padre)
iteraciones = 0

# Guardar una copia del padre inicial
padre_inicial = copy.deepcopy(padre)
hijo_final = copy.deepcopy(padre)

while True:
    iteraciones += 1
    
    if random.random() < PROBABILIDAD_MUTACION:
        hijo = mutacion(padre, origen)
    else:
        hijo = copy.deepcopy(padre)
    
    if random.random() < PROBABILIDAD_CRUCE:
        hijo = cruce(hijo, destino)
    
    adaptacion_hijo = funcion_objetivo(hijo)
    
    if adaptacion_padre < adaptacion_hijo:
        hijo_final = copy.deepcopy(hijo)
        padre = hijo
        adaptacion_padre = adaptacion_hijo
    
    print("iteracion", iteraciones)
    mostrar_poblacion([hijo])
    if adaptacion_hijo == 64:
        break

# Mostrar el tablero inicial y final con gráficos mejorados
iniciar_interfaz(padre_inicial, hijo_final)
