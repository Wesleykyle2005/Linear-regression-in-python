# Pedir el tamaño de la matriz
registros = int(input("Ingrese el número de registros: "))
columnas = 2
variable_dependiente = []
variable_independiente = []

# Inicializar una matriz vacía para almacenar todos los datos
matriz = []

# Pedir al usuario que ingrese los elementos
for i in range(registros):  
    y_elemento = float(input(f"Ingrese el {i+1} elemento de la variable dependiente y: "))
    x_elemento = float(input(f"Ingrese el {i+1} elemento de la variable independiente x: "))
    variable_dependiente.append(y_elemento)
    variable_independiente.append(x_elemento)
    
matriz.append(variable_dependiente)
matriz.append(variable_independiente)

# Mostrar los valores
print("Valores de la variable dependiente:")
for elemento in range(registros):
    print(matriz[0][elemento])

print("Valores de la variable independiente:")
for elemento in range(registros):
    print(matriz[1][elemento])

# Variables globales para almacenar las sumatorias
suma_x = suma_y = suma_x2 = suma_y2 = suma_xy = 0

# Función para calcular sumatorias
def calcular_sumatorias():
    global suma_x, suma_y, suma_x2, suma_y2, suma_xy
    suma_x = sum(variable_independiente)
    suma_y = sum(variable_dependiente)
    suma_x2 = sum([x**2 for x in variable_independiente])
    suma_y2 = sum([y**2 for y in variable_dependiente])
    suma_xy = sum([variable_independiente[i] * variable_dependiente[i] for i in range(registros)])

    print(f"Suma de x: {suma_x}")
    print(f"Suma de y: {suma_y}")
    print(f"Suma de x^2: {suma_x2}")
    print(f"Suma de y^2: {suma_y2}")
    print(f"Suma de x*y: {suma_xy}")

    return suma_x, suma_y, suma_x2, suma_xy

# Llamar a la función de sumatorias
suma_x, suma_y, suma_x2, suma_xy = calcular_sumatorias()

# Función para calcular b1 usando la fórmula correcta
def calcular_b1():
    n = registros
    b1 = (suma_xy - (suma_x * suma_y) / n) / (suma_x2 - (suma_x**2) / n)
    return b1

# Calcular y mostrar b1
b1 = calcular_b1()
print(f"El valor de b1 (pendiente) es: {b1}")

# Funciones adicionales para otros cálculos
def calcular_b0():
    n = registros
    b0 = (1/n)*(suma_y-(b1*suma_x))
    return b0

b0 = calcular_b0()
print(f"El valor de b0 es: {b0}")

def calcular_r2():
    n = registros
    numerador = b1 * (suma_xy - (suma_x * suma_y) / n)
    denominador = suma_y2 - (suma_y**2 / n)
    r2 = numerador / denominador
    return r2

r2 = calcular_r2()
print(f"El valor de R^2 es: {r2}")

def calcular_rv():
    print("Realizar los cálculos")

def calcular_t():
    print("Realizar los cálculos")

