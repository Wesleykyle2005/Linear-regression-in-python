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
registros = 18
variable_dependiente = [12, 22, 30, 18, 32, 36, 30, 34, 46, 40, 44, 50, 44, 60, 64, 64, 68, 76]
variable_independiente = [0.5, 0.5, 0.5, 1, 1, 1, 1.5, 1.5, 1.5, 2, 2, 2, 2.5, 2.5, 2.5, 3, 3, 3]

# Calcular sumatorias
suma_x, suma_y, suma_x2, suma_xy, suma_y2 = calcular_sumatorias(variable_independiente, variable_dependiente, registros)

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

def imprimir_datos():
    print(f"El valor de b1 (pendiente) es: {b1}")
    print(f"El valor de b0 (intercepto) es: {b0}")
    print(f"El valor de R^2 es: {r2}, r es: {r}, scr es: {scr}, stc es: {stc}")
    print(f"rv es: {rv}, mcr es: {mcr}, sce es: {sce}, mce es: {mce}")
    print(f"El valor de t_calculado es: {t_calculado}, t_critico es: {t_critico}")
    print(f"F_calculado es: {F_calculado}, F_2calculado es: {F_2calculado}, F_critico es: {F_critico}")

imprimir_datos()
