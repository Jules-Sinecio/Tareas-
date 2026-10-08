import numpy as np


# ================================================================
#  NIVEL 1 — Crear y manipular arrays
# ================================================================
#  Lo más básico: cómo crear arrays y hacer operaciones con ellos.
#  Un array de NumPy es como una lista de Python pero más rápido
#  y con operaciones matemáticas elemento a elemento.
# ================================================================

print("=" * 60)
print("NIVEL 1 — Crear y manipular arrays")
print("=" * 60)

# ---------------------------------------------------------------
#  1.1) Crea un array con las temperaturas de una semana:
#       [22, 25, 19, 30, 28, 21, 24]
#       Calcula la media, el máximo y el mínimo.
# ---------------------------------------------------------------

temps_sem = np.array([22, 25, 19, 30, 28, 21, 24])[cite: 1]
print("Media:", round(temps_sem.mean(), 2))
print("Máximo:", temps_sem.max())
print("Mínimo:", temps_sem.min())

# ---------------------------------------------------------------
#  1.2) Crea un array de alturas de 0 a 5000 metros, cada 500 m.
#       Usa np.arange.
#       ¿Cuántos elementos tiene?
# ---------------------------------------------------------------

# np.arange(inicio, fin, paso) — OJO: el fin NO se incluye,
# por eso ponemos 5500 si queremos que llegue a 5000.

alturas = np.arange(0, 5500, 500)[cite: 1]
print("Array de alturas:", alturas)
print("Cantidad de elementos:", alturas.size)

# ---------------------------------------------------------------
#  1.3) Crea un array de 10 valores equidistantes entre 0 y 100.
#       Usa np.linspace.
# ---------------------------------------------------------------

# np.linspace(inicio, fin, cantidad) — aquí sí INCLUYE el fin.
# Es diferente de arange: le dices cuántos puntos quieres,
# no el paso.

linea_puntos = np.linspace(0, 100, 10)[cite: 1]
print("Valores equidistantes:", linea_puntos)

# ---------------------------------------------------------------
#  1.4) Operaciones elemento a elemento.
#       Tienes temperaturas en Celsius: [0, 20, 37, 100]
#       Conviértelas a Fahrenheit:  F = C * 9/5 + 32
#       y a Kelvin:  K = C + 273.15
# ---------------------------------------------------------------

# En NumPy las operaciones se aplican a TODOS los elementos
# automáticamente. No necesitas un for loop.

celsius = np.array([0, 20, 37, 100])
fahrenheit = (celsius * 1.8) + 32
kelvin = celsius + 273.15[cite: 1]

print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)
print("Kelvin:", kelvin)

# ---------------------------------------------------------------
#  1.5) Crea un array de 8 ceros y otro de 5 unos.
#       Usa np.zeros y np.ones.
# ---------------------------------------------------------------

arr_ceros = np.zeros(8)
arr_unos = np.ones(5)

print("Array de ceros:", arr_ceros)
print("Array de unos:", arr_unos)

# ================================================================
#  NIVEL 2 — Indexing y slicing
# ================================================================
#  Cómo seleccionar partes de un array.
#  Es igual que listas de Python pero con más poderes.
# ================================================================

print("\n\n" + "=" * 60)
print("NIVEL 2 — Indexing y slicing")
print("=" * 60)

# ---------------------------------------------------------------
#  2.1) Dado este array de presiones (hPa):
#       [1013, 950, 850, 700, 500, 300, 200, 100]
#       Obtén: el primer elemento, el último, los 3 primeros,
#       y los 3 últimos.
# ---------------------------------------------------------------

presion = np.array([1013, 950, 850, 700, 500, 300, 200, 100])[cite: 1]

print("Primer valor:", presion[0])
print("Último valor:", presion[-1])
print("Primeros 3:", presion[:3])
print("Últimos 3:", presion[-3:])

# ---------------------------------------------------------------
#  2.2) Del mismo array, obtén los elementos en posiciones pares
#       (0, 2, 4, 6) usando slicing con paso.
# ---------------------------------------------------------------

# array[inicio:fin:paso]

pos_pares = presion[::2]
print("Posiciones pares:", pos_pares)

# ---------------------------------------------------------------
#  2.3) Modifica el array: cambia el valor en la posición 3
#       de 700 a 750. Luego cambia los dos últimos a 999.
# ---------------------------------------------------------------

presion_copia = presion.copy()   # hacemos copia para no perder el original[cite: 1]
presion_copia[3] = 750[cite: 1]
presion_copia[-2:] = 999[cite: 1]
print("Copia modificada:", presion_copia)

# ---------------------------------------------------------------
#  2.4) Tienes un array de 12 meses de lluvia (mm):
#       Obtén solo los meses de verano (junio=5, julio=6, agosto=7)
#       usando una lista de índices.
# ---------------------------------------------------------------

# "Fancy indexing": pasas una lista de índices y te devuelve
# los elementos en esas posiciones.

lluvia = np.array([30, 25, 40, 60, 80, 120, 150, 140, 90, 50, 35, 28])[cite: 1]

idx_verano = [5, 6, 7]
lluvia_verano = lluvia[idx_verano]
print("Lluvia en verano:", lluvia_verano)

# ================================================================
#  NIVEL 3 — Máscaras booleanas
# ================================================================
#  ESTE ES EL CONCEPTO MÁS IMPORTANTE para los ejercicios
#  de atmósfera. Una máscara es un array de True/False que
#  usas para filtrar datos.
# ================================================================

print("\n\n" + "=" * 60)
print("NIVEL 3 — Máscaras booleanas")
print("=" * 60)

# ---------------------------------------------------------------
#  3.1) Tienes temperaturas de 10 días:
#       Crea una máscara que sea True donde T > 25.
#       Úsala para obtener solo las temperaturas calientes.
# ---------------------------------------------------------------

t_dias = np.array([22, 25, 19, 30, 28, 21, 24, 26, 27, 23])
filtro_calor = t_dias > 25
t_calientes = t_dias[filtro_calor]

print("Temperaturas > 25:", t_calientes)

# ---------------------------------------------------------------
#  3.2) Combina condiciones: selecciona temperaturas entre 20 y 28
#       (inclusive). Usa & (and) con paréntesis.
# ---------------------------------------------------------------

# IMPORTANTE: cada condición va entre paréntesis cuando usas & o |
# & : and (ambas deben ser True)
# | : or  (al menos una debe ser True)
# ~ : not (invierte True/False)

filtro_rango = (t_dias >= 20) & (t_dias <= 28)
t_intermedias = t_dias[filtro_rango]

print("Temperaturas entre 20 y 28:", t_intermedias)

# ---------------------------------------------------------------
#  3.3) ¿Cuántos días fueron calientes (T > 25)?
#       Usa np.sum sobre la máscara.
# ---------------------------------------------------------------

# True se cuenta como 1, False como 0.
# Entonces np.sum de una máscara = cantidad de True.

total_calientes = np.sum(filtro_calor)
print("Total de días calientes:", total_calientes)

# ---------------------------------------------------------------
#  3.4) Reemplaza valores: pon 0 donde la temperatura sea menor
#       a 22 (simular que no hubo evento significativo).
# ---------------------------------------------------------------

t_umbral = t_dias.copy()
t_umbral[t_umbral < 22] = 0
print("Temperaturas con umbral aplicado:", t_umbral)

# ---------------------------------------------------------------
#  3.5) Clasificación con máscaras: clasifica cada temperatura
#       como "fría" (<22), "templada" (22-28), o "caliente" (>28).
#       Cuenta cuántas hay de cada clase.
# ---------------------------------------------------------------

dias_frios = np.sum(t_dias < 22)
dias_templados = np.sum((t_dias >= 22) & (t_dias <= 28))
dias_muy_calientes = np.sum(t_dias > 28)

print("Frías (<22):", dias_frios)
print("Templadas (22-28):", dias_templados)
print("Calientes (>28):", dias_muy_calientes)

# ---------------------------------------------------------------
#  3.6) np.where: encuentra los ÍNDICES donde se cumple una
#       condición. ¿En qué días (posiciones) llovió más de 80 mm?
# ---------------------------------------------------------------

lluvia = np.array([30, 25, 40, 60, 80, 120, 150, 140, 90, 50, 35, 28])[cite: 1]

# np.where devuelve una TUPLA. El [0] saca el array de índices.
# ¿Por qué tupla? Porque en 2D devolvería (filas, columnas).
# En 1D solo hay un eje, pero la tupla siempre está.

pos_lluvia_fuerte = np.where(lluvia > 80)[0]
print("Posiciones donde llovió > 80 mm:", pos_lluvia_fuerte)

# ================================================================
#  NIVEL 4 — Funciones útiles: diff, cumsum, nan
# ================================================================

print("\n\n" + "=" * 60)
print("NIVEL 4 — diff, cumsum y NaN")
print("=" * 60)

# ---------------------------------------------------------------
#  4.1) np.diff: diferencias consecutivas.
#       Tienes alturas de un globo cada minuto:
#       [100, 250, 430, 600, 590, 610, 800]
#       Calcula cuánto subió (o bajó) entre cada minuto.
# ---------------------------------------------------------------

# np.diff calcula elemento[i+1] - elemento[i].
# Si hay N elementos, el resultado tiene N-1 elementos.

h_globo = np.array([100, 250, 430, 600, 590, 610, 800])
cambio_minuto = np.diff(h_globo)
print("Diferencias consecutivas del globo:", cambio_minuto)

# ---------------------------------------------------------------
#  4.2) np.cumsum: suma acumulada.
#       Tienes lluvia horaria (mm): [2, 5, 0, 1, 8, 3, 0]
#       Calcula la lluvia acumulada a cada hora.
# ---------------------------------------------------------------

# cumsum: [2, 2+5, 2+5+0, 2+5+0+1, ...] = [2, 7, 7, 8, 16, 19, 19]

precip_hora = np.array([2, 5, 0, 1, 8, 3, 0])
precip_acumulada = np.cumsum(precip_hora)
print("Lluvia acumulada:", precip_acumulada)

# ---------------------------------------------------------------
#  4.3) NaN: datos faltantes.
#       Tienes mediciones con huecos (sensor falló):
#       [22.5, nan, 23.1, 24.0, nan, nan, 22.8]
#       Calcula la media ignorando los NaN.
# ---------------------------------------------------------------

# np.nan es un valor especial = "no hay dato".
# np.mean falla con NaN (da NaN). Usa np.nanmean.

datos_sensor = np.array([22.5, np.nan, 23.1, 24.0, np.nan, np.nan, 22.8])
promedio_valido = np.nanmean(datos_sensor)
print("Media omitiendo NaN:", round(promedio_valido, 2))

# ---------------------------------------------------------------
#  4.4) Detectar y contar NaN.
# ---------------------------------------------------------------

es_nan = np.isnan(datos_sensor)
indices_nulos = np.where(es_nan)[0]
total_nulos = np.sum(es_nan)

print("Índices donde hay NaN:", indices_nulos)
print("Total de NaN:", total_nulos)

# ---------------------------------------------------------------
#  4.5) Reemplazar valores malos con NaN.
#       Un sensor marca -999 cuando falla. Límpialo.
# ---------------------------------------------------------------

mediciones_raw = np.array([22.5, -999, 23.1, 24.0, -999, -999, 22.8])
mediciones_nan = np.where(mediciones_raw == -999, np.nan, mediciones_raw)
print("Array limpio (-999 cambiados a NaN):", mediciones_nan)

# ---------------------------------------------------------------
#  4.6) Limpieza combinada: reemplaza valores negativos Y
#       mayores a 100 con NaN (outliers de un sensor de humedad).
# ---------------------------------------------------------------

humedad = np.array([55, 72, -5, 88, 150, 63, -10, 91, 200, 45])[cite: 1]

humedad_limpia = humedad.astype(float)  # necesario para poder poner NaN[cite: 1]
humedad_limpia = np.where((humedad_limpia < 0) | (humedad_limpia > 100), np.nan, humedad_limpia)
print("Humedad sin valores inválidos:", humedad_limpia)

# ================================================================
#  NIVEL 5 — Arrays 2D y operaciones por eje
# ================================================================
#  En meteorología casi siempre trabajas con datos 2D o más:
#  (estaciones × tiempo), (latitud × longitud), etc.
#  Entender los ejes es CLAVE.
# ================================================================

print("\n\n" + "=" * 60)
print("NIVEL 5 — Arrays 2D y ejes")
print("=" * 60)

# ---------------------------------------------------------------
#  5.1) Crea una matriz de temperaturas: 3 estaciones × 5 días.
#       Cada fila es una estación, cada columna es un día.
# ---------------------------------------------------------------

red_estaciones = np.array([
    [20, 22, 24, 26, 28],
    [18, 20, 22, 24, 26],
    [16, 18, 20, 22, 24]
])
print("Matriz de temperaturas:\n", red_estaciones)

# ---------------------------------------------------------------
#  5.2) Promedios por eje.
#       axis=0: promedia "hacia abajo" (sobre las estaciones)
#               → te da un promedio por día
#       axis=1: promedia "hacia la derecha" (sobre los días)
#               → te da un promedio por estación
# ---------------------------------------------------------------

# TRUCO para recordar: axis=X elimina esa dimensión.
#   axis=0 → elimina filas → queda un valor por columna
#   axis=1 → elimina columnas → queda un valor por fila

media_diaria = np.mean(red_estaciones, axis=0)
media_estacion = np.mean(red_estaciones, axis=1)

print("Promedio por día (eje 0):", media_diaria)
print("Promedio por estación (eje 1):", media_estacion)

# ---------------------------------------------------------------
#  5.3) Máximo y mínimo por eje.
# ---------------------------------------------------------------

maximo_diario = np.max(red_estaciones, axis=0)
minimo_estacion = np.min(red_estaciones, axis=1)

print("Máximo por día:", maximo_diario)
print("Mínimo por estación:", minimo_estacion)

# ---------------------------------------------------------------
#  5.4) Máscaras en 2D.
#       Encuentra todas las celdas donde T > 25.
# ---------------------------------------------------------------

mask_t25 = red_estaciones > 25
print("Máscara booleana T > 25:\n", mask_t25)

# ---------------------------------------------------------------
#  5.5) np.where en 2D.
#       Devuelve DOS arrays: filas y columnas.
# ---------------------------------------------------------------

filas, columnas = np.where(red_estaciones > 25)
print("Filas (estaciones) > 25:", filas)
print("Columnas (días) > 25:", columnas)

# ---------------------------------------------------------------
#  5.6) Seleccionar filas y columnas específicas.
# ---------------------------------------------------------------

# Una fila completa (estación B):
estacion_b = red_estaciones[1, :]

# Una columna completa (día 3):
dia_3 = red_estaciones[:, 2]

# Un bloque (estaciones A y B, días 1 a 3):
bloque_ab_1a3 = red_estaciones[0:2, 0:3]

print("Estación B:", estacion_b)
print("Día 3:", dia_3)
print("Submatriz estaciones A-B (días 1 a 3):\n", bloque_ab_1a3)

# ================================================================
#  NIVEL 6 — Reshape y broadcasting
# ================================================================
#  Reshape cambia la forma de un array sin cambiar los datos.
#  Broadcasting permite operar arrays de distinto tamaño.
#  Ambos se usan MUCHO en datos atmosféricos.
# ================================================================

print("\n\n" + "=" * 60)
print("NIVEL 6 — Reshape y broadcasting")
print("=" * 60)

# ---------------------------------------------------------------
#  6.1) Reshape básico.
#       Tienes 24 mediciones horarias en un array 1D.
#       Reorganízalas en una matriz de 4 periodos × 6 horas.
# ---------------------------------------------------------------

# reshape no cambia los datos, solo la forma del array.
# El total de elementos debe coincidir: 24 = 4 × 6

horas_24 = np.arange(24)
bloques_4x6 = horas_24.reshape(4, 6)
print("Matriz reorganizada (4x6):\n", bloques_4x6)

# ---------------------------------------------------------------
#  6.2) Reshape para promedios por periodo.
#       Tienes 30 días × 24 horas = 720 datos de temperatura.
#       Calcula el promedio diario.
# ---------------------------------------------------------------

# Simulamos 720 horas de datos
np.random.seed(42)[cite: 1]
temp_horaria = 20 + 5 * np.sin(2 * np.pi * np.tile(np.arange(24), 30) / 24) \
               + np.random.normal(0, 1, 720)[cite: 1]

# Reshape a (30 días, 24 horas) y promediamos sobre las horas
temp_grid = temp_horaria.reshape(30, 24)
media_por_dia = np.mean(temp_grid, axis=1)

print("Primeros 5 promedios diarios:", np.round(media_por_dia[:5], 2))

# ---------------------------------------------------------------
#  6.3) Broadcasting: operaciones entre arrays de distinto tamaño.
#       NumPy "estira" el array más chico para que coincida.
# ---------------------------------------------------------------

# Ejemplo simple: restar la media de cada columna a una matriz.
# La matriz es (3, 5) y la media por columna es (5,).
# NumPy automáticamente resta cada media a su columna.

matriz_datos = np.array([[1, 2, 3, 4, 5],
                         [6, 7, 8, 9, 10],
                         [11, 12, 13, 14, 15]])

media_cols = np.mean(matriz_datos, axis=0)
matriz_centrada_cols = matriz_datos - media_cols

print("Matriz original:\n", matriz_datos)
print("Media por columna:", media_cols)
print("Restando media de columnas:\n", matriz_centrada_cols)

# ---------------------------------------------------------------
#  6.4) Broadcasting con None (np.newaxis).
#       A veces necesitas agregar un eje para que el broadcasting
#       funcione en la dirección correcta.
# ---------------------------------------------------------------

# Si quieres restar la media por FILA (no columna):

# Esto falla: datos(3,3) - media_fila(3,) resta por columna, no fila.
# Necesitas convertir media_fila de shape (3,) a shape (3, 1):

media_filas = np.mean(matriz_datos, axis=1)
media_filas_columna = media_filas[:, np.newaxis]
matriz_centrada_filas = matriz_datos - media_filas_columna

print("Media por fila:", media_filas)
print("Restando media de filas:\n", matriz_centrada_filas)

# ---------------------------------------------------------------
#  6.5) Ejemplo atmosférico: calcular anomalías mensuales.
#       Tienes 3 años × 12 meses de temperatura.
#       Calcula la climatología (promedio de cada mes) y resta.
# ---------------------------------------------------------------

# Simulamos datos: 3 años × 12 meses
datos_meses = 15 + 10 * np.random.rand(3, 12)

# Climatología: promedio de cada mes sobre los 3 años
climatologia = np.mean(datos_meses, axis=0)

# Anomalías: cada año menos la climatología
# Broadcasting funciona directo: (3, 12) - (12,)
anomalias_mes = datos_meses - climatologia

print("Climatología (media de cada mes):\n", np.round(climatologia, 2))
print("Anomalías resultantes:\n", np.round(anomalias_mes, 2))

