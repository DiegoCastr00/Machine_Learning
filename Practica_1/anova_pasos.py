# Datos de ejemplo para tres grupos (Group1, Group2 y Group3)
group1 = [15, 20, 25, 30, 35]
group2 = [10, 15, 20, 25, 30]
group3 = [150,250 ,3, 500, 115]

# Calcular las medias de cada grupo
mean_group1 = sum(group1) / len(group1)
mean_group2 = sum(group2) / len(group2)
mean_group3 = sum(group3) / len(group3)

# Calcular la media general de todos los datos
all_data = group1 + group2 + group3
mean_total = sum(all_data) / len(all_data)

# Calcular la suma de los cuadrados de las diferencias entre las medias de los grupos
ss_between = (
    len(group1) * (mean_group1 - mean_total)**2 +
    len(group2) * (mean_group2 - mean_total)**2 +
    len(group3) * (mean_group3 - mean_total)**2
)

# Calcular la suma de los cuadrados de las diferencias dentro de los grupos
ss_within = sum((x - mean_group1)**2 for x in group1) + \
           sum((x - mean_group2)**2 for x in group2) + \
           sum((x - mean_group3)**2 for x in group3)

# Calcular el estadístico F
#La estadística F es simplemente un cociente de dos varianzas. Las varianzas son una medida
# de dispersión, es decir, qué tan dispersos están los datos con respecto a la media.
df_between = 2  # Grados de libertad entre grupos (3 grupos - 1)
df_within = len(all_data) - 3  # Grados de libertad dentro de los grupos (N - k)
f_statistic = (ss_between / df_between) / (ss_within / df_within)

# Calcular el valor p utilizando la distribución F
import scipy.stats as stats
p_value = 1 - stats.f.cdf(f_statistic, df_between, df_within)

# Imprimir resultados
print(f"Estadístico F: {f_statistic}")
print(f"Valor p: {p_value}")

# Evaluar si rechazamos o no la hipótesis nula
alpha = 0.05  # Nivel de significancia
if p_value < alpha:
    print("Rechazamos la hipótesis nula: Hay diferencias significativas entre los grupos.")
else:
    print("No rechazamos la hipótesis nula: No hay diferencias significativas entre los grupos.")

