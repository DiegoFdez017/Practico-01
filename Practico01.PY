# Importar las librerías que necesitamos
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Establecemos una semilla para que los resultados sean los mismos cada vez que ejecutemos el código
np.random.seed(42)

# Creamos 100 estaturas aleatorias entre 1.45m y 2.15m
estaturas = np.random.uniform(1.45, 2.15, 100)

# Lista para guardar los pesos que vamos a generar
pesos = []

# Creamos pesos aleatorios basados en cada estatura
for estatura in estaturas:
    # Definimos el peso mínimo y máximo para cada estatura
    peso_min = 50 + (estatura - 1.45) * 35  # Peso mínimo aumenta con la estatura
    peso_max = 80 + (estatura - 1.45) * 45  # Peso máximo aumenta con la estatura
    # Generamos un peso aleatorio entre el peso mínimo y máximo
    peso = np.random.uniform(peso_min, peso_max)
    pesos.append(peso)  # Agregamos el peso a la lista

# Creamos una tabla con las estaturas y los pesos
datos = pd.DataFrame({
    'Estatura (m)': estaturas,
    'Peso (kg)': pesos
})

# Calculamos la pendiente y la intersección para la línea de mejor ajuste
x = datos['Estatura (m)']
y = datos['Peso (kg)']
pendiente = np.sum((x - np.mean(x)) * (y - np.mean(y))) / np.sum((x - np.mean(x)) ** 2)
interseccion = np.mean(y) - pendiente * np.mean(x)

# Calculamos los valores de la línea ajustada
y_recta = pendiente * x + interseccion

# Mostramos los datos y la línea ajustada en un gráfico
plt.scatter(datos['Estatura (m)'], datos['Peso (kg)'], color='blue', label='Datos')
plt.plot(x, y_recta, color='red', label='Línea ajustada')
plt.title('Estatura vs Peso con Línea Ajustada')
plt.xlabel('Estatura (m)')
plt.ylabel('Peso (kg)')
plt.legend()
plt.show()
