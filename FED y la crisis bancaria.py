#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import librerías

import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
import warnings


warnings.simplefilter(action='ignore', category=FutureWarning)


ruta_json = "C:\\Users\\....json"

# Leer el archivo JSON con pandas
df = pd.read_json(ruta_json)

# Ordenar la tabla por la columna Assets (adj.) de mayor a menor
df = df.sort_values(by="Assets (adj.)", ascending=False)

# Seleccionar las cuatro primeras filas de la tabla
top4 = df.head(4)


top4["Nombre y fecha"] = top4["Bank Name"] + "\n" + top4["Date"].dt.strftime("%d/%m/%Y")


total = df["Assets (adj.)"].sum()


def porcentaje(row):
  return "{:.1f}%".format(row["Assets (adj.)"] / total * 100)


top4["% Assets (adj.)"] = top4.apply(porcentaje, axis=1)


resto = df.tail(len(df) - 4)
porcentaje_resto = "{:.1f}%".format(resto["Assets (adj.)"].sum() / total * 100)


top4 = top4.append({"Nombre y fecha": "Resto de bancos", "% Assets (adj.)": porcentaje_resto}, ignore_index=True)


top4["% Assets (adj.)"] = top4["% Assets (adj.)"].str.replace("%", "").astype(float)

# Seleccionar las columnas Nombre y fecha y % Assets (adj.)
df_prolijo = top4.loc[:, ["Nombre y fecha", "% Assets (adj.)"]]


df_prolijo = df_prolijo.style.set_properties(**{'text-align': 'left'})


# Imprimir el dataframe prolijo con display o render
display(df_prolijo)
#print(df_prolijo.render())

# Crear una figura y un eje con matplotlib
fig, ax = plt.subplots()

# Hacer un gráfico de torta con los porcentajes de los bancos (ajustados) y sus nombres y fechas como etiquetas
ax.pie(top4["% Assets (adj.)"], labels=top4["Nombre y fecha"], autopct="%1.1f%%")


ax.set_title("Porcentaje de activos (ajustados) de los bancos")

# Ajustar el espacio entre los subplots
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

# Agregar la fuente debajo del gráfico
plt.figtext(0.5, 0.01, "Fuente: Elaboración propia en base datos FDIC", ha="center", fontsize=12)

# Mostrar el gráfico
plt.show()


# In[ ]:




