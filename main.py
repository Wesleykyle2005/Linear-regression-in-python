import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox

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

        if num_datos < 5:
            messagebox.showwarning("Advertencia", "El número mínimo de datos es 5.")
            num_datos = 5
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

    if mce == 0:
        # Regresión perfecta: omitir cálculos adicionales
        imprimir_resultados(b1, b0, r2, r, scr, stc, rv, mcr, sce, mce, None, None, None, None, None)
        mostrar_grafica(x_values, y_values, b1, b0)
        print("Regresión perfecta: no se requieren más cálculos.")
        return

    # Calcular t y F si no hay regresión perfecta
    t_calculado, t_critico = calcular_t(b1, suma_x2, suma_x, registros, mce)
    F_calculado, F_2calculado, F_critico = calcular_F(rv, t_calculado, registros)

    # Imprimir resultados
    imprimir_resultados(b1, b0, r2, r, scr, stc, rv, mcr, sce, mce, t_calculado, t_critico, F_calculado, F_2calculado, F_critico)
    mostrar_grafica(x_values, y_values, b1, b0)
    resultado = analizar_regresion(b1, b0, r2, r, scr, stc, rv, mcr, sce, mce, t_calculado, t_critico, F_calculado, F_critico)
    print(resultado)


def imprimir_resultados(b1, b0, r2, r, scr, stc, rv, mcr, sce, mce, t_calculado, t_critico, F_calculado, F_2calculado, F_critico):
    print(f"El valor de b1 (pendiente) es: {b1}")
    print(f"El valor de b0 (intercepto) es: {b0}")
    print(f"El valor de R^2 es: {r2}, r es: {r}, scr es: {scr}, stc es: {stc}")
    print(f"rv es: {rv}, mcr es: {mcr}, sce es: {sce}, mce es: {mce}")
    print(f"El valor de t_calculado es: {t_calculado}, t_critico es: {t_critico}")
    print(f"F_calculado es: {F_calculado}, F_2calculado es: {F_2calculado}, F_critico es: {F_critico}")

def mostrar_grafica(x_values,y_values, b1, b0):
    print(f"Valores de x: {x_values}")
    print(f"Valores de Y: {y_values}")
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

def analizar_regresion(b1, b0, r2, r, scr, stc, rv, mcr, sce, mce, t_calculado, t_critico, f_calculado, f_critico):
    mensajes = []

    # Evaluación de la pendiente b1
    if b1 > 0:
        mensajes.append("La pendiente es positiva, lo que indica que hay una relación positiva entre las variables.")
    elif b1 < 0:
        mensajes.append("La pendiente es negativa, lo que sugiere que la variable dependiente disminuye conforme aumenta la variable independiente.")
    else:
        mensajes.append("La pendiente es cero, lo que significa que no hay relación entre las variables.")

    # Evaluación de R^2 (Coeficiente de determinación)
    if r2 > 0.8:
        mensajes.append(f"El valor de R^2 es {r2:.2f}, lo que indica que el modelo explica una gran parte de la variabilidad de la variable dependiente.")
    elif 0.5 < r2 <= 0.8:
        mensajes.append(f"El valor de R^2 es {r2:.2f}, lo que significa que el modelo explica una cantidad moderada de la variabilidad.")
    else:
        mensajes.append(f"El valor de R^2 es {r2:.2f}, lo que indica que el modelo no explica mucha variabilidad.")

    # Evaluación del coeficiente de correlación r
    if r > 0.9:
        mensajes.append(f"El coeficiente de correlación es {r:.2f}, lo que sugiere una relación lineal fuerte entre las variables.")
    elif 0.7 < r <= 0.9:
        mensajes.append(f"El coeficiente de correlación es {r:.2f}, lo que indica una correlación moderada.")
    else:
        mensajes.append(f"El coeficiente de correlación es {r:.2f}, lo que sugiere una relación débil entre las variables.")

    # Evaluación del RV (F calculado) y comparación con F crítico
    if f_calculado > f_critico:
        mensajes.append(f"El valor de F calculado es {f_calculado:.2f}, mayor que el valor crítico de F ({f_critico:.2f}), lo que indica que el modelo es estadísticamente significativo.")
    else:
        mensajes.append(f"El valor de F calculado es {f_calculado:.2f}, menor que el valor crítico de F ({f_critico:.2f}), lo que indica que el modelo no es significativo.")

    # Evaluación del t-calculado y comparación con t-crítico
    if t_calculado > t_critico:
        mensajes.append(f"El valor de t calculado es {t_calculado:.2f}, mayor que el valor crítico de t ({t_critico:.2f}), lo que indica que la pendiente es significativa.")
    else:
        mensajes.append(f"El valor de t calculado es {t_calculado:.2f}, menor que el valor crítico de t ({t_critico:.2f}), lo que sugiere que la pendiente no es significativa.")

    # Evaluación de la suma de cuadrados de la regresión (SCR) y del error (SCE)
    if scr > sce:
        mensajes.append(f"El modelo explica más variabilidad ({scr:.2f}) que el error residual ({sce:.2f}), lo que sugiere un buen ajuste.")
    else:
        mensajes.append(f"El error residual ({sce:.2f}) es mayor que la variabilidad explicada por el modelo ({scr:.2f}), lo que indica un ajuste deficiente.")

    # Unir todos los mensajes de manera coherente
    mensaje_final = " ".join(mensajes)
    
    return mensaje_final



# Función para cerrar el programa correctamente
def on_closing():
    if messagebox.askokcancel("Salir", "¿Deseas cerrar la aplicación?"):
        ventana.quit()  # Detener el loop de Tkinter
        ventana.destroy()  # Cerrar la ventana de forma segura

# Función para centrar la ventana
def centrar_ventana(ventana):
    ventana.update_idletasks()  # Actualiza la ventana para obtener el tamaño
    width = ventana.winfo_width()  # Ancho de la ventana
    height = ventana.winfo_height()  # Altura de la ventana
    x = (ventana.winfo_screenwidth() // 2) - (width // 2)  # Calcular posición X
    y = (ventana.winfo_screenheight() // 2) - (height // 2)  # Calcular posición Y
    ventana.geometry(f'{width+100}x{height+100}+{x}+{y}')  # Aplicar la geometría

# Configurar la ventana principal
ventana = tk.Tk()
ventana.title("Análisis de regresión simple")

# Llamar a la función para centrar la ventana después de que esté construida
ventana.update()  # Actualiza la ventana para que obtenga su tamaño
centrar_ventana(ventana)

# Configurar el cierre del programa cuando se presiona la "X"
ventana.protocol("WM_DELETE_WINDOW", on_closing)




# Etiqueta de entrada
label_num_datos = tk.Label(ventana, text="Ingrese el número de datos:")
label_num_datos.pack()


# Entrada de datos
entry_num_datos = tk.Entry(ventana)
entry_num_datos.pack()

button_generate_entry= tk.Button(ventana, text="Generar campos", command=generar_campos)
button_generate_entry.pack()

# Frame donde se generarán los campos
frame_campos = tk.Frame(ventana)
frame_campos.pack()

# Frame de la gráfica
frame_grafica = tk.Frame(ventana)
frame_grafica.pack()

# Mantener la ventana abierta
ventana.mainloop()










