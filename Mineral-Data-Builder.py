"""
Created on Thu Jun 15 12:41:41 2023
@author: Rsoriano
"""
import numpy as np
import matplotlib.colors
import matplotlib.pyplot as plt

seed = 50
rand_state = 100
color_map = plt.cm.get_cmap('viridis')
rand = np.random.RandomState(seed) 
dist_list = ['uniform','normal','exponential','lognormal','chisquare','beta']
param_list = ['-1,1','0,1','1','0,1','2','0.5,0.9']
colors_list = ['navy','red','blue','#0a9396','#ee9b00','green']

fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(12, 7))
plt_ind_list = np.arange(6) + 231

for dist, plt_ind, param, colors in zip(dist_list, plt_ind_list, param_list, colors_list):
    x = eval('rand.' + dist + '(' + param + ', 5000)')

    plt.subplot(plt_ind)
    plt.hist(x, bins=50, color=colors)
    plt.title(dist)     

fig.subplots_adjust(hspace=0.4, wspace=.3)
plt.suptitle('Ejemplos de algunas distribuciones', fontsize=20)
plt.show()

#%%%
def generar_datos(media, desviacion_estandar, tamaño_muestra):

    datos_minerales = np.random.normal(media, desviacion_estandar, tamaño_muestra)
    return datos_minerales

def simular_muestreo_y_analisis(ley_mineral_real, error_muestreo, error_analisis):

    muestras_muestreadas = ley_mineral_real + np.random.normal(0, error_muestreo, len(ley_mineral_real))
    resultados_analisis = muestras_muestreadas + np.random.normal(0, error_analisis, len(ley_mineral_real))
    return resultados_analisis

# Ejemplo de uso:
ley_mineral_real = generar_datos(2.5, 0.5, 1000)  # Datos reales de ley de mineral
error_muestreo = 0.1  # Error de muestreo
error_analisis = 0.05  # Error de análisis

resultados_simulados = simular_muestreo_y_analisis(ley_mineral_real, error_muestreo, error_analisis)

# Imprime algunos valores simulados después del muestreo y análisis.
print("Datos simulados después del muestreo y análisis:")
print(resultados_simulados[:10])  # Imprime los primeros 10 valores simulados.

# Datos simulados de coordenadas geoespaciales (latitud y longitud)
latitud = np.random.uniform(-90, 90, 100)  # Cambia el rango según tus datos reales
longitud = np.random.uniform(-180, 180, 100)  # Cambia el rango según tus datos reales

# Datos simulados de ley de mineral
ley_mineral = generar_datos(2.5, 0.5, 100)  # Utiliza tu función de generación de datos

# Visualización en un gráfico de dispersión geoespacial
plt.figure(figsize=(10, 6))
plt.scatter(longitud, latitud, c=ley_mineral, cmap='viridis', s=ley_mineral * 50, alpha=0.7)
plt.colorbar(label='Ley de Mineral')
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.title('Visualización de Ley de Mineral en un Yacimiento')
plt.grid(True)
plt.show()

#%%%
# Datos simulados de ley de mineral
ley_mineral = generar_datos(2.5, 0.5, 1000)  # Utiliza tu función de generación de datos

# Cálculo de estadísticas descriptivas
media = np.mean(ley_mineral)
desviacion_estandar = np.std(ley_mineral)

# Creación de histograma
plt.figure(figsize=(10, 6))
plt.hist(ley_mineral, bins=30, color='#00b4d8', alpha=0.7)
plt.xlabel('Ley de Mineral')
plt.ylabel('Frecuencia')
plt.title('Distribución de la Ley de Mineral en el Yacimiento')
plt.axvline(media, color='red', linestyle='dashed', linewidth=2, label=f'Media: {media:.2f}')
plt.axvline(media + desviacion_estandar, color='green', linestyle='dashed', linewidth=2, label=f'Desv. Estándar: {desviacion_estandar:.2f}')
plt.axvline(media - desviacion_estandar, color='green', linestyle='dashed', linewidth=2)
plt.legend()
plt.grid(True)
plt.show()

# Imprime estadísticas
print(f"Media: {media:.2f}")
print(f"Desviación Estándar: {desviacion_estandar:.2f}")





