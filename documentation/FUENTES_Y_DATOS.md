# Fuentes y datos

## 1. Dataset principal

**California Housing**

Los datos son agregados por bloque censal, no por vivienda individual. El valor máximo está censurado en 500,001 dólares, lo que limita las predicciones en la zona alta del mercado.

| Campo | Detalle |
|---|---|
| Fuente | U.S. Census Bureau (1990), distribuido por StatLib y disponible en scikit-learn |
| URL | https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset |
| Licencia | Uso académico y educativo; datos públicos agregados |
| Registros | 20640 |
| Columnas | 10 |
| Variable objetivo | `median_house_value` |
| Nulos | 207 en `total_bedrooms` |

## 2. Diccionario de variables

| Variable | Tipo | Descripción | Rol |
|---|---|---|---|
| `longitude` | Numérica continua | Longitud geográfica del bloque de viviendas. | Feature |
| `latitude` | Numérica continua | Latitud geográfica del bloque de viviendas. | Feature |
| `housing_median_age` | Numérica discreta | Edad mediana de las viviendas del bloque. | Feature |
| `total_rooms` | Numérica discreta | Total de habitaciones en el bloque. | Feature |
| `total_bedrooms` | Numérica discreta | Total de dormitorios en el bloque. Presenta 207 valores nulos. | Feature |
| `population` | Numérica discreta | Población del bloque. | Feature |
| `households` | Numérica discreta | Número de hogares en el bloque. | Feature |
| `median_income` | Numérica continua | Ingreso mediano de los hogares, expresado en decenas de miles de dólares. | Feature principal |
| `median_house_value` | Numérica continua | Valor mediano de la vivienda. Es la variable objetivo. Está acotada en 500,001 dólares. | Target |
| `ocean_proximity` | Categórica | Proximidad al océano. Se excluye del modelo lineal para trabajar solo con variables numéricas. | Excluida |

## 3. Origen y contexto

El dataset fue construido a partir del censo de Estados Unidos de 1990. Cada fila representa un bloque censal, no una vivienda individual. Las variables geográficas permiten reconstruir patrones regionales, pero también introducen dependencia espacial.

La versión tabular usada en este proyecto proviene de `housing.csv`, ampliamente distribuida para fines educativos. La versión de scikit-learn ofrece la misma información con una API alternativa.

## 4. Decisiones de limpieza

| Decisión | Justificación | Efecto |
|---|---|---|
| Imputar `total_bedrooms` con la mediana | Evita perder 207 registros y reduce el sesgo de la media. | Se conserva el 100% de las filas. |
| Excluir `ocean_proximity` | Es categórica y el modelo base es numérico. | Se pierde información de cercanía al mar. |
| Mantener valores atípicos | Representan bloques reales y el objetivo es interpretar, no limpiar en exceso. | El modelo puede verse afectado por extremos. |
| No eliminar el techo de 500,001 | Es un límite del dataset, no un error de captura. | Se documenta como limitación. |

## 5. Consideraciones éticas

- **Privacidad:** los datos son agregados y no contienen identificadores personales.
- **Representatividad:** corresponden a California en 1990; no representan el mercado actual ni otras regiones.
- **Sesgo:** las variables socioeconómicas pueden reflejar desigualdades históricas. No se usan para clasificar personas.
- **Transparencia:** se publican métricas, coeficientes y limitaciones.
- **Supervisión humana:** la salida es una estimación académica y requiere validación profesional.

## 6. Fuentes complementarias

- **California Housing (scikit-learn).** Dataset de bloques censales de California, 1990. 8 variables numéricas y valor mediano de vivienda. [Enlace](https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset).
- **California Housing (StatLib).** Distribución original del dataset utilizada en la literatura. Variables geográficas, demográficas y socioeconómicas. [Enlace](https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.html).
- **Kaggle: California Housing Prices.** Versión tabular del dataset con exploraciones de la comunidad. Mismas variables del dataset California Housing. [Enlace](https://www.kaggle.com/datasets/camnugent/california-housing-prices).

## 7. Referencias bibliográficas

- Pace, R. K., & Barry, R. (1997). Sparse spatial autoregressions. Statistics & Probability Letters, 33(3), 291-297.
- Pedregosa, F. et al. (2011). Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research, 12, 2825-2830.
- scikit-learn Developers. California housing dataset. https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset
- Streamlit. Streamlit documentation. https://docs.streamlit.io
- Studer, S. et al. (2021). Towards CRISP-ML(Q): A Machine Learning Process Model with Quality Assurance Methodology. Machine Learning and Knowledge Extraction, 3(2), 392-413.
- McKinney, W. (2010). Data Structures for Statistical Computing in Python. Proceedings of the 9th Python in Science Conference.

## 8. Cómo citar este proyecto

Feibert Alirio Guzmán Pérez. (2026). *Predicción de Precios de Viviendas con Regresión Lineal*. UFHEC, Machine Learning I. https://github.com/TU-USUARIO/TU-REPO
