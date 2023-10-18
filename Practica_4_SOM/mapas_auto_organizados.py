

import numpy as np
import matplotlib.pyplot as plt

# Datos de entrada (coordenadas 2D)
datos = np.array([[1.2, 0.8],
                 [0.4, 0.6],
                 [3.0, 2.9],
                 [2.9, 2.5]])

# Creación del mapa autoorganizativo
# Inicializamos las posiciones de las neuronas aleatoriamente
np.random.seed(0)  # Para reproducibilidad
mapa = np.random.rand(2, 2, 2)  # Mapa 2x2 con pesos 2D

# Hiperparámetros del algoritmo
tasa_aprendizaje = 0.4
num_epocas = 2

# Entrenamiento
for epoca in range(num_epocas):
    for punto in datos:
        # Calcular la neurona ganadora (la más cercana)
        diferencias = mapa - punto
        distancias = np.sum(diferencias**2, axis=2)
        neurona_ganadora = np.unravel_index(np.argmin(distancias), distancias.shape)
        print(neurona_ganadora)
        # Actualizar los pesos de la neurona ganadora
        mapa[neurona_ganadora] += tasa_aprendizaje * (punto - mapa[neurona_ganadora])
    print('-------')
# Resultado
print("Mapa autoorganizativo final:")
print(mapa)

