#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Crear un dataframe con los nuevos datos
data = {
    'Country': ['India', 'China', 'Singapore', 'Japan', 'Korea', 'Philippines', 'Taipei', 'Thailand', 'Indonesia', 'Pakistan', 'Bangladesh', 'Other countries'],
    'Variation': [26.14, 13.38, 5.65, -5.19, 5.99, 9.05, 11.52, 9.05, 20.86, 8.96, 30.82, -9.72]
}

df = pd.DataFrame(data)

# Cargar el archivo de shapefile con los límites de los países de Asia
asia = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
asia = asia[asia['continent'] == 'Asia']

# Unir los datos con los límites de los países
merged = asia.merge(df, left_on='name', right_on='Country')

# Crear el mapa
fig, ax = plt.subplots(figsize=(12, 8))
merged.plot(column='Variation', cmap='Reds', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# Agregar etiquetas de país y porcentaje
for x, y, label, value in zip(merged.geometry.centroid.x, merged.geometry.centroid.y, merged['Country'], merged['Variation']):
    ax.text(x, y-0.3, f'{label}\n{value}%', fontsize=8, ha='center', va='top')

# Personalizar el mapa
ax.set_title('Variación acumulada de servicios basados en el conocimiento en Asia (9 meses)')
ax.axis('off')

# Agregar fuente
plt.text(0.5, -0.1, 'Fuente: Elaboración propia en base a datos de Argencon', ha='center', va='center', transform=ax.transAxes, fontsize=8)

# Guardar el gráfico como un archivo JPEG
filename = r'.jpg'
plt.savefig(filename, dpi=300)

# Mostrar mensaje de confirmación
print(f'El gráfico se ha guardado correctamente en: {filename}')


# In[ ]:




