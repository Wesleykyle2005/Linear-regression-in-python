import math as ma
import scipy.stats as stats

# Función para calcular sumatorias
def calcular_sumatorias(variable_independiente, variable_dependiente, registros):
    suma_x = sum(variable_independiente)
    suma_y = sum(variable_dependiente)
    suma_x2 = sum([x**2 for x in variable_independiente])
    suma_y2 = sum([y**2 for y in variable_dependiente])
    suma_xy = sum([variable_independiente[i] * variable_dependiente[i] for i in range(registros)])

    return suma_x, suma_y, suma_x2, suma_xy, suma_y2

# Función para calcular b1 (pendiente)
def calcular_b1(suma_x, suma_y, suma_x2, suma_xy, registros):
    b1 = (suma_xy - ((suma_x * suma_y) / registros)) / (suma_x2 - (suma_x**2) / registros)
    return b1

# Función para calcular b0 (intercepto)
def calcular_b0(suma_x, suma_y, b1, registros):
    b0 = (1/registros) * (suma_y - (b1 * suma_x))
    return b0

# Función para calcular el coeficiente de determinación R^2
def calcular_r2(b1, suma_xy, suma_x, suma_y, suma_y2, registros):
    scr = b1 * (suma_xy - ((suma_x * suma_y) / registros))
    stc = suma_y2 - (suma_y**2 / registros)
    r2 = scr / stc
    return r2, ma.sqrt(r2), scr, stc

# Función para calcular el valor de F
def calcular_rv(scr, stc, registros):
    mcr = scr / 1
    sce = stc - scr
    mce = sce / (registros - 2)
    rv = mcr / mce
    return rv, mcr, sce, mce

# Función para calcular t
def calcular_t(b1, suma_x2, suma_x, registros, mce):
    t_calculado = b1 / (ma.sqrt(mce / (suma_x2 - (suma_x**2 / registros))))
    alpha = 0.05
    t_critico = stats.t.ppf(1 - alpha / 2, registros - 2)
    return t_calculado, t_critico

# Función para calcular F (análisis de varianza)
def calcular_F(rv, t_calculado, registros):
    F_calculado = rv
    F_2calculado = t_calculado**2
    alpha = 0.05
    F_critico = stats.f.ppf(1 - alpha, 1, registros - 2)
    return F_calculado, F_2calculado, F_critico
