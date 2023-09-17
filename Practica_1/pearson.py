import numpy as np

# Datos de ejemplo para dos variables (Tamaño de la casa y Precio de venta)
tamano_casa = np.array([1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700])
precio_venta = np.array([30, 10, 10, 8, 4, 40, 6, 1, 1, 6])

# Calcular la media de cada variable
media_tamano_casa = np.mean(tamano_casa)
media_precio_venta = np.mean(precio_venta)

# Calcular las desviaciones de cada variable con respecto a su media
desviaciones_tamano_casa = tamano_casa - media_tamano_casa
desviaciones_precio_venta = precio_venta - media_precio_venta

# Calcular el coeficiente de correlación de Pearson
correlacion = np.sum(desviaciones_tamano_casa * desviaciones_precio_venta) / \
    np.sqrt(np.sum(desviaciones_tamano_casa**2) * np.sum(desviaciones_precio_venta**2))

# Imprimir el coeficiente de correlación
print(f"Coeficiente de correlación de Pearson: {correlacion:.2f}")

# Interpretar la correlación
if correlacion > 0:
    print("Hay una correlación positiva: A medida que el tamaño de la casa aumenta, el precio tiende a aumentar.")
elif correlacion < 0:
    print("Hay una correlación negativa: A medida que el tamaño de la casa aumenta, el precio tiende a disminuir.")
else:
    print("No hay una correlación lineal significativa entre el tamaño de la casa y el precio de venta.")

