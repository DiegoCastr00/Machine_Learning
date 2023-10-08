import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data

# Estandarizar los datos (recomendado para PCA)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Calcular la matriz de covarianza
cov_matrix = np.cov(X_scaled, rowvar=False)

# Calcular los valores propios (eigenvalues) y vectores propios (eigenvectors)
eigenvalues, _ = np.linalg.eig(cov_matrix)

# Ordenar los valores propios en orden descendente
eigenvalues_sorted = np.sort(eigenvalues)[::-1]

# Calcular la varianza acumulada
total_variance = np.sum(eigenvalues_sorted)
variance_explained = np.cumsum(eigenvalues_sorted) / total_variance

# Imprimir la varianza acumulada para cada número de componentes principales
for i, explained_variance in enumerate(variance_explained):
    print(f"Componente Principal {i+1}: {explained_variance:.4f}")

# Visualizar la varianza acumulada en un gráfico
import matplotlib.pyplot as plt

plt.plot(range(1, len(variance_explained) + 1), variance_explained, marker='o', linestyle='--')
plt.xlabel('Número de Componentes Principales')
plt.ylabel('Varianza Acumulada Explicada')
plt.title('Varianza Acumulada en PCA del conjunto de datos Iris')
plt.grid(True)
plt.show()