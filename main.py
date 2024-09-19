import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

from statistics_functions import (
    calcular_sumatorias,
    calcular_b1,
    calcular_b0,
    calcular_r2,
    calcular_rv,
    calcular_t,
    calcular_F
)

# Datos
#registros = 18
#variable_dependiente = [12, 22, 30, 18, 32, 36, 30, 34, 46, 40, 44, 50, 44, 60, 64, 64, 68, 76]
#variable_independiente = [0.5, 0.5, 0.5, 1, 1, 1, 1.5, 1.5, 1.5, 2, 2, 2, 2.5, 2.5, 2.5, 3, 3, 3]
registros=0
variable_dependiente=[]
variable_independiente=[]
  
# Calcular sumatorias

def generar_campos():
    try:
        num_datos= int(entry_num_datos.get())
        num_actual=len(variable_dependiente)

        if num_datos > num_actual:
            for i in range(num_actual, num_datos):
                variable_independiente.append(tk.DoubleVar())
                variable_dependiente.append(tk.DoubleVar())

        elif num_datos< num_actual:
            variable_independiente[:] = variable_independiente[:num_datos]
            variable_dependiente[:] = variable_dependiente[:num_datos]

        for widget in frame_campos.winfo_children():
            widget.destroy()

        for i in range(num_datos):
            label_x = tk.Label(frame_campos, text=f"X{i+1}:")
            label_x.grid(row=i, column=0)
                
            entry_x = tk.Entry(frame_campos, textvariable=variable_independiente[i])
            entry_x.grid(row=i, column=1)
                        
            label_y = tk.Label(frame_campos, text=f"Y{i+1}:")
            label_y.grid(row=i, column=2)
                        
            entry_y = tk.Entry(frame_campos, textvariable=variable_dependiente[i])
            entry_y.grid(row=i, column=3)
        boton_calcular = tk.Button(frame_campos, text="Calcular", command=realizar_calculos)
        boton_calcular.grid(row=num_datos, columnspan=4)
    except ValueError:
        print("Ingresar un número válido")




     

def realizar_calculos():
    # Convertir los valores de tk.DoubleVar a float
    x_values = [var.get() for var in variable_independiente]
    y_values = [var.get() for var in variable_dependiente]
    registros = len(x_values)  # Actualizar el número de registros

    # Calcular sumatorias
    suma_x, suma_y, suma_x2, suma_xy, suma_y2 = calcular_sumatorias(x_values, y_values, registros)

    # Calcular b1 y b0
    b1 = calcular_b1(suma_x, suma_y, suma_x2, suma_xy, registros)
    b0 = calcular_b0(suma_x, suma_y, b1, registros)

    # Calcular R^2 y otros valores
    r2, r, scr, stc = calcular_r2(b1, suma_xy, suma_x, suma_y, suma_y2, registros)

    # Calcular el valor de rv
    rv, mcr, sce, mce = calcular_rv(scr, stc, registros)

    # Calcular t
    t_calculado, t_critico = calcular_t(b1, suma_x2, suma_x, registros, mce)

    # Calcular F
    F_calculado, F_2calculado, F_critico = calcular_F(rv, t_calculado, registros)

    # Imprimir resultados
    imprimir_resultados(b1, b0, r2, r, scr, stc, rv, mcr, sce, mce, t_calculado, t_critico, F_calculado, F_2calculado, F_critico)
    mostrar_grafica(x_values,y_values, b1, b0)


def imprimir_resultados(b1, b0, r2, r, scr, stc, rv, mcr, sce, mce, t_calculado, t_critico, F_calculado, F_2calculado, F_critico):
    print(f"El valor de b1 (pendiente) es: {b1}")
    print(f"El valor de b0 (intercepto) es: {b0}")
    print(f"El valor de R^2 es: {r2}, r es: {r}, scr es: {scr}, stc es: {stc}")
    print(f"rv es: {rv}, mcr es: {mcr}, sce es: {sce}, mce es: {mce}")
    print(f"El valor de t_calculado es: {t_calculado}, t_critico es: {t_critico}")
    print(f"F_calculado es: {F_calculado}, F_2calculado es: {F_2calculado}, F_critico es: {F_critico}")

def mostrar_grafica(x_values,y_values, b1, b0):
    line_x = np.array(x_values)
    line_y = b1*line_x+b0
    fig, ax = plt.subplots()
    ax.scatter(x_values,y_values, color='blue', label='Puntos de los datos')
    ax.plot(line_x, line_y, color='red', label='Línea de regresión')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend()
    for widget in frame_grafica.winfo_children():
        widget.destroy()

    # Crear el canvas de matplotlib dentro del frame de tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
    canvas.draw()
    canvas.get_tk_widget().pack()

ventana = tk.Tk()
ventana.title("Anális de regresión simple")

label_num_datos= tk.Label(ventana, text="Ingrese los datos:")
label_num_datos.pack()

#Numero de campos a completar
entry_num_datos= tk.Entry(ventana)
entry_num_datos.pack()

#botón para generarlos
button_generate_entry= tk.Button(ventana, text="Generar campos", command=generar_campos)
button_generate_entry.pack()

# Frame donde se generarán los campos 
frame_campos=tk.Frame(ventana)
frame_campos.pack()

# Frame de la grafica
frame_grafica = tk.Frame(ventana)
frame_grafica.pack()

ventana.mainloop()
