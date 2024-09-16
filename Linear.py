# Pedir el tamaño de la matriz
registros = int(input("Ingrese el número de registros: "))
columnas= 2
variable_dependiente = []
variable_independiente= []

# Inicializar una matriz vacía para almacenar todos los datos
matriz = []

# Pedir al usuario que ingrese los elementos
for i in range(registros):  
    y_elemento = float(input(f"Ingrese el {i+1} elemento de la variable dependiente y: "))
    x_elemento = float(input(f"Ingrese el {i+1} elemento de la variable independiente x:"))
    variable_dependiente.append(y_elemento)
    variable_independiente.append(x_elemento)
    
matriz.append(variable_dependiente)
matriz.append(variable_independiente)


# Mostrar los valores
print("Valores de la variable dependiente:")
for elemento in range(registros):
    print(matriz[0][i])

print("Valores de la variable independiente:")
for elemento in range(registros):
    print(matriz[1][i])

def calcular_sumatorias():
    # definir las variables de las sumatorias hasta arriba de todo esto para volverlas accesibles por las demás funciones
    print("Realizar los calculos")

def calcular_b1():
    print("Realizar los calculos")

def calcular_b0():
    print("Realizar los calculos")

def calcular_r2():
    print("Realizar los calculos")
 
def calcular_rv():
    print("Realizar los calculos")
 
def calcular_t():
    print("Realizar los calculos")


 
 
