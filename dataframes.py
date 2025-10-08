import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Crear un DataFrame de ejemplo
"""
np.random.seed(42)  # para reproducibilidad

df = pd.DataFrame({
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
    'Ventas': np.random.randint(2000, 5000, 6),
    'Gastos': np.random.randint(1000, 4000, 6),
    'Clientes': np.random.randint(50, 150, 6)
})
"""
#df = pd.read_csv("https://raw.githubusercontent.com/llshao/data_scientist/master/Cartwheeldata.csv")


#print(df.head(1))

#print(df[df["Ventas"] >= 4000])

#sns.set(style="whitegrid")

#plt.figure(figsize=(14,5))


#matplotlib
#plt.subplot(1,2,1)  # 1 fila, 2 columnas, gráfico 1
#plt.bar(df['Mes'], df['Ventas'])
#plt.title('Ventas por Mes (Matplotlib)')



#seaborn
#plt.subplot(1,2,2)  # 1 fila, 2 columnas, gráfico 2
#sns.barplot(data=df, x='Mes', y='Ventas', edgecolor='black', palette='viridis')
#plt.title('Ventas por Mes (Seaborn)')


#plt.show()



#construya un dataframe a aprtir de un diccionario de tres claves y un solo valor, cuyo indice sea un string


#df2 = {
#    'clave1': "hola",
#    'clave2': "chau",
#    'clave3': "xd"
#}


#print(pd.DataFrame(df2, index=['clave']))

"""
df3 = {
    'columna1': ['a', 'b', 'c'],
    'columna2': ['d', 'e', 'f'],
    'columna3': ['g', 'h', 'i'],
}


#print(pd.DataFrame(df3, index=['Enero', 'Febrero', 'Marzo']))



miDataframe = {
    'Nombre' : ['Bruno', 'Agustín'],
    'Edad' : [24, 23]
}
"""
#print(pd.DataFrame(miDataframe))

#plt.bar(miDataframe['Nombre'], miDataframe['Edad'])
#plt.show()

#sns.barplot(miDataframe, x='Nombre', y='Edad')
#plt.show()


#a = np.array([(1,2,3),(4,5,6)])
#b = np.ones((3, 2))


#print(b @ a)



#Ejercicio 2
"""
javi = {
    'columna1' : ['a', 'b', 'c'],
    'columna2' : [10, 100, 1000]
}


dfjavi = pd.DataFrame(javi)

datos_agrupados = dfjavi.groupby('columna1')['columna2'].sum()

print(dfjavi)

print(datos_agrupados)
"""

#Ejercicio 3
"""
df = pd.DataFrame({
    'Estudiante' : ['Merino', 'Javier', 'Viru'],
    'Edad' : [24, 25, 26]
})

print(df)
"""

#Ejercicio 4
"""
df = pd.DataFrame({
    'Producto' : ['Control', 'Monitor', 'Teclado'],
    'Precio' : [180000, 400000, 50000],
    'Stock' : [6, 15, 10]
})

print(df[df['Stock']>10])
"""

#Ejercicio 5
"""
df = pd.DataFrame({
    'Mes' : ['Enero', 'Febrero', 'Marzo'],
    'Ventas' : [800, 1200, 1100]
})

plt.title('Ventas/Mes')
plt.bar(df['Mes'], df['Ventas'])
plt.show()
"""


#Ejercicio 12
"""
df = pd.DataFrame({
    'A' : [800, 1200, 1100, 800, 1200],
    'B' : [800, 1200, 1100, 800, 1204],
    'C' : [800, 1200, 1100, 800, 1230]
})
jio
print(df.mean())
"""

"""
Arquitectura MVT
La arquitectura MVT se divide en 3 partes, por sus siglas MVT:
View: Es la parte lógica y decide que se envía y que no
Model: Es el modelo que dice como está hecho cierto objeto y se comunica directamente con la BD
Template: Es la vista que se le presenta al usuario, recibe datos del View
"""

"""
Una API Rest es una interfaz de comunicacion entre sistemas a través de métodos HTTP, por ejemplo:
GET: Pide datos
POST: Envía datos
PUT: Actualiza datos
DELETE: Elimina datos

"""


"""
Una librería es un conjunto de funciones o clases que podemos implementar en nuestro código si consideramos necesario
Ejemplos de estas librerías:
Numpy: Librería escrita en C++ para que python pueda delegar trabajos relacionados a números para una compilación más rápida y eficiente
matplotlib: Librería básica para crear gráficos a partir de datasets
seaborn: Librería basada en matplotlib que ofrece más funciones sobre matplotlib

"""


"""
asdasd
asd
"""