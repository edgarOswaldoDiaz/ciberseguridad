# Python en ciencia de datos:

---

## Entorno y Gestión de Paquetes

| Comando                                 | Descripción                                        |
| --------------------------------------- | -------------------------------------------------- |
| `conda create -n nombre_env python=3.x` | Crea un entorno conda nuevo                        |
| `conda activate nombre_env`             | Activa el entorno conda                            |
| `conda deactivate`                      | Desactiva el entorno conda                         |
| `pip install paquete`                   | Instala un paquete desde PyPI                      |
| `conda install paquete`                 | Instala un paquete desde conda-forge/Canal oficial |
| `pip list`                              | Lista paquetes instalados                          |
| `pip freeze > requirements.txt`         | Exporta versiones de paquetes a requirements.txt   |
| `pip install -r requirements.txt`       | Instala paquetes desde un requirements.txt         |

---

## Jupyter Notebook / Lab

| Comando / Magic                           | Descripción                                       |
| ----------------------------------------- | ------------------------------------------------- |
| `jupyter notebook`                        | Arranca el servidor de notebooks                  |
| `jupyter lab`                             | Arranca JupyterLab                                |
| `%matplotlib inline`                      | Mostrar gráficos embebidos en el notebook         |
| `%load_ext autoreload`<br>`%autoreload 2` | Recarga código Python automáticamente             |
| `%time`                                   | Mide el tiempo de ejecución de la siguiente línea |
| `%timeit`                                 | Mide tiempo promedio de ejecución                 |
| `Shift + Enter`                           | Ejecuta la celda actual                           |
| `Esc + A/B`                               | Inserta una celda arriba/abajo                    |
| `M` / `Y`                                 | Cambia el tipo de celda a Markdown / Code         |

---

## Manipulación y Exploración de Datos (pandas)

| Comando                                  | Descripción                                     |
| ---------------------------------------- | ----------------------------------------------- |
| `import pandas as pd`                    | Importa pandas                                  |
| `df = pd.read_csv('archivo.csv')`        | Carga CSV en DataFrame                          |
| `df.head(n=5)`                           | Muestra primeras n filas                        |
| `df.tail(n=5)`                           | Muestra últimas n filas                         |
| `df.info()`                              | Información de tipos de datos y valores nulos   |
| `df.describe()`                          | Estadísticos descriptivos de columnas numéricas |
| `df.shape`                               | Tupla (n\_filas, n\_columnas)                   |
| `df.columns`                             | Lista nombres de columnas                       |
| `df['col']` / `df.col`                   | Selección de serie (columna)                    |
| `df[['col1','col2']]`                    | Selección de múltiples columnas                 |
| `df.loc[filas, columnas]`                | Indexación por etiquetas                        |
| `df.iloc[filas, columnas]`               | Indexación por posiciones                       |
| `df.drop(columns=['col'])`               | Elimina columna(s)                              |
| `df.dropna()`                            | Elimina filas con NA                            |
| `df.fillna(valor)`                       | Rellena NA con un valor                         |
| `df.sort_values('col')`                  | Ordena por columna                              |
| `df.groupby('col').agg({'otra':'mean'})` | Agrupación y agregación                         |

---

## Array Computing (NumPy)

| Comando                                       | Descripción                     |
| --------------------------------------------- | ------------------------------- |
| `import numpy as np`                          | Importa NumPy                   |
| `arr = np.array([1,2,3])`                     | Crea un array                   |
| `arr.shape`                                   | Dimensiones del array           |
| `arr.reshape((m,n))`                          | Cambia forma del array          |
| `arr.mean()`, `.std()`, `.sum()`              | Estadísticos básicos            |
| `np.zeros((m,n))`, `np.ones((m,n))`           | Arrays de ceros/unos            |
| `np.arange(start, stop, step)`                | Secuencia con paso              |
| `np.linspace(start, stop, num)`               | Secuencia de longitud fija      |
| `np.random.seed(0)`                           | Fija semilla de aleatoriedad    |
| `np.random.rand(m,n)`, `np.random.randn(m,n)` | Aleatorios uniformes / normales |

---

## Visualización

### Matplotlib

| Comando                              | Descripción           |
| ------------------------------------ | --------------------- |
| `import matplotlib.pyplot as plt`    | Importa Matplotlib    |
| `plt.figure(figsize=(w,h))`          | Tamaño de la figura   |
| `plt.plot(x, y, label='texto')`      | Gráfica de líneas     |
| `plt.scatter(x, y)`                  | Gráfica de dispersión |
| `plt.bar(x, height)`                 | Gráfica de barras     |
| `plt.hist(data, bins=10)`            | Histograma            |
| `plt.xlabel('x')`, `plt.ylabel('y')` | Etiquetas ejes        |
| `plt.title('Título')`                | Título                |
| `plt.legend()`                       | Muestra leyenda       |
| `plt.show()`                         | Renderiza gráfica     |

### Seaborn

| Comando                                        | Descripción                    |
| ---------------------------------------------- | ------------------------------ |
| `import seaborn as sns`                        | Importa Seaborn                |
| `sns.set(style='whitegrid')`                   | Estilo de fondo                |
| `sns.histplot(data, kde=True)`                 | Histograma con KDE             |
| `sns.scatterplot(x='col1', y='col2', data=df)` | Scatter con DataFrame          |
| `sns.boxplot(x='col', y='otra', data=df)`      | Boxplot                        |
| `sns.heatmap(df.corr(), annot=True)`           | Mapa de calor de correlaciones |

---

## Preprocesamiento y Modelado (scikit‑learn)

| Comando / Clase                                                                            | Descripción                      |
| ------------------------------------------------------------------------------------------ | -------------------------------- |
| `from sklearn.model_selection import train_test_split`                                     | División de datos                |
| `X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)` | Separar datos                    |
| `from sklearn.preprocessing import StandardScaler`                                         | Estandarización de variables     |
| `scaler = StandardScaler(); X_train_sc = scaler.fit_transform(X_train)`                    | Ajustar y transformar            |
| `from sklearn.linear_model import LinearRegression`                                        | Modelo de regresión lineal       |
| `model = LinearRegression(); model.fit(X_train, y_train)`                                  | Entrenar modelo                  |
| `y_pred = model.predict(X_test)`                                                           | Predicción                       |
| `from sklearn.metrics import mean_squared_error, accuracy_score`                           | Métricas de evaluación           |
| `mse = mean_squared_error(y_test, y_pred)`                                                 | Error cuadrático medio           |
| `accuracy = accuracy_score(y_test, y_pred)`                                                | Precisión (clasificación)        |
| `from sklearn.ensemble import RandomForestClassifier`                                      | Bosque aleatorio (clasificación) |
| `from sklearn.cluster import KMeans`                                                       | K‑means (clustering)             |

---

## Atajos y Buenas Prácticas

* **Entornos aislados**: usa siempre conda o venv para evitar conflictos de versiones.
* **Control de versiones**: mantén tu código en Git y registra cambios importantes.
* **Notebook limpio**: elimina celdas intermedias y agrega comentarios Markdown para explicación.
* **Estructura de proyectos**: separa scripts, notebooks, datos (`/data`), módulos (`/src`) y resultados (`/output`).
* **Documentación**: escribe docstrings en funciones y README con instrucciones de uso.

---

> By CISO oswaldo.diaz
