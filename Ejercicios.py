import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df2 = pd.DataFrame({
    'Nombre': ['Ana','Luis','Marta','Juan','Sofía','Pedro','Lucía','Diego','Carla','Tomás'],
    'Altura': [1.65,1.75,1.60,1.80,1.68,1.77,1.62,1.82,1.70,1.78],
    'Peso': [60,75,55,85,63,78,58,90,65,80]
})

sns.set(style="darkgrid")
sns.scatterplot(df2, x='Peso', y='Altura')
plt.show()