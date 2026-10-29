# Documentación técnica

## 1. Resumen ejecutivo

El proyecto estima el valor mediano de una vivienda en California con regresión lineal. Usa 20,640 bloques censales y ocho variables numéricas. La regresión múltiple alcanza un **R² de 0.614** en el conjunto de prueba, con un **RMSE de $71,133** y un **MAE de $51,810**.

El resultado es interpretable y reproducible, pero no es un avalúo profesional: los datos son de 1990, están agregados por bloque y la variable objetivo tiene un techo en 500,001 dólares.

## 2. Problema y alcance

**Pregunta:** ¿Cómo predecir el valor mediano de una vivienda en California a partir de variables geográficas, demográficas y socioeconómicas, usando regresión lineal simple y múltiple?

**Objetivo general:** Desarrollar y desplegar un modelo de regresión lineal que estime el valor mediano de una vivienda y lo ponga a disposición mediante una landing page y un simulador interactivo en Streamlit.

**Alcance:** El proyecto es académico y exploratorio. No sustituye un avalúo profesional ni una decisión financiera.

### Objetivos específicos

- Comprender el problema y el diccionario de variables del dataset California Housing.
- Realizar análisis exploratorio, limpieza e imputación de valores faltantes.
- Entrenar un modelo de regresión lineal simple usando median_income.
- Entrenar un modelo de regresión lineal múltiple con las variables numéricas disponibles.
- Evaluar los modelos con MSE, RMSE, MAE y R².
- Publicar una landing page documental y una aplicación Streamlit para simular predicciones.

## 3. Dataset

| Atributo | Valor |
|---|---|
| Nombre | California Housing |
| Archivo | `housing.csv` |
| Registros | 20,640 |
| Columnas | 10 |
| Variable objetivo | `median_house_value` |
| Nulos | 207 en `total_bedrooms` |
| Entrenamiento | 16,512 filas |
| Prueba | 4,128 filas |

### Diccionario de variables

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

### Calidad de datos

- `total_bedrooms` presenta 207 valores nulos. Se imputan con la mediana para conservar todos los registros.
- `ocean_proximity` es categórica y se excluye del modelo lineal. Incluirla requeriría codificación y cambiaría la interpretación.
- El valor máximo de `median_house_value` es 500,001 dólares, un límite artificial del dataset.
- Existen valores atípicos en `total_rooms`, `population` y `households`.

## 4. Metodología CRISP-ML(Q)

01. **Comprensión del problema.** Se define el objetivo, la variable objetivo, las métricas y el alcance académico.
02. **Comprensión y preparación de datos.** Se carga el CSV, se revisan tipos y nulos, se imputa total_bedrooms y se excluye ocean_proximity.
03. **Análisis exploratorio.** Se estudian distribuciones, correlaciones, valores atípicos y patrones geográficos.
04. **Modelado.** Se entrenan regresión simple y múltiple con scikit-learn y una división 80/20.
05. **Evaluación.** Se comparan MSE, RMSE, MAE y R² sobre el conjunto de prueba.
06. **Despliegue y monitoreo.** Se publica la landing page y la app Streamlit, dejando documentados los límites y la reproducibilidad.

## 5. Análisis exploratorio

El análisis exploratorio permite entender la calidad de los datos, la relación entre variables y los patrones geográficos antes de entrenar el modelo.

### Hallazgos

- median_income es la variable con mayor correlación positiva con median_house_value.
- La ubicación geográfica explica parte importante del precio: la costa y las áreas metropolitanas concentran valores más altos.
- total_bedrooms tiene 207 valores nulos; se imputan con la mediana para no perder registros.
- La variable objetivo está acotada en 500,001 dólares, lo que genera un efecto techo en las predicciones.
- Existen valores atípicos en total_rooms, population y households que deben interpretarse con cautela.

### Figuras generadas

| Archivo | Contenido |
|---|---|
| `correlation-heatmap.png` | Matriz de correlación numérica. |
| `geographic-map.png` | Dispersión geográfica coloreada por precio. |
| `simple-regression.png` | Relación ingreso mediano vs. precio. |
| `target-distribution.png` | Distribución del valor de la vivienda. |

## 6. Modelos

### 6.1 Regresión lineal simple

Ecuación estimada:

```text
median_house_value = 45,085.58 + 41,793.85 × median_income
```

Por cada aumento de una unidad en median_income (10,000 dólares de ingreso mediano), el modelo estima un incremento promedio de 41,793.85 dólares en el valor de la vivienda.

### 6.2 Regresión lineal múltiple

Variables: `longitude`, `latitude`, `housing_median_age`, `total_rooms`, `total_bedrooms`, `population`, `households`, `median_income`.

Intercepto: `$-3,578,224`.

| Variable | Coeficiente |
|---|---|
| `median_income` | 40538.4 |
| `longitude` | -42632.39 |
| `latitude` | -42450.07 |
| `housing_median_age` | 1182.81 |
| `total_rooms` | -8.19 |
| `total_bedrooms` | 116.26 |
| `population` | -38.49 |
| `households` | 46.34 |

Los coeficientes son asociaciones ajustadas, no efectos causales. La longitud y la latitud tienen signos negativos porque resumen patrones geográficos complejos y están correlacionadas entre sí.

## 7. Evaluación

| Métrica | Valor | Interpretación |
|---|---|---|
| MSE | $5.06 B | Error cuadrático medio; penaliza errores grandes. |
| RMSE | $71,133 | Error típico en dólares. |
| MAE | $51,810 | Desviación absoluta promedio. |
| R² | 0.614 | 61.39% de la varianza explicada. |

El modelo múltiple mejora la capacidad explicativa frente a la regresión simple, pero sigue dejando fuera relaciones no lineales y variables categóricas como ocean_proximity.

### Lectura crítica

Un R² de 0.614 indica que el modelo captura una parte relevante de la variabilidad, pero el error absoluto sigue siendo alto para decisiones reales. El modelo es útil para explorar relaciones y comunicar conceptos, no para tasar una vivienda concreta.

## 8. Arquitectura

```text
housing.csv
   │
   ├── pandas: carga, limpieza e imputación
   │
   ├── EDA: matplotlib y seaborn
   │       └── assets/figures/*.png
   │
   ├── scikit-learn: regresión simple y múltiple
   │       └── métricas: MSE, RMSE, MAE, R²
   │
   ├── Streamlit: app.py
   │       └── simulador interactivo
   │
   └── GitHub Pages: index.html + css + js
           └── landing documental
```

### Componentes

| Componente | Archivo | Responsabilidad |
|---|---|---|
| Landing | `index.html` | Narrativa, resultados y enlaces. |
| Estilos | `css/styles.css` | Diseño responsive y modo oscuro. |
| Interacciones | `js/main.js` | Navegación, tema, calculadora y lightbox. |
| App | `app.py` | Simulador y exploración interactiva. |
| Notebook | `notebooks/Project_RL_clean.ipynb` | Flujo reproducible. |
| Documento | `documentation/Material_1_Proyecto_ML_UFHEC.docx` | Entrega académica. |
| Pipeline | `.opencode/skills/despliegue-streamlit/scripts/` | Generación y validación. |

## 9. Reproducibilidad

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Para regenerar todos los entregables:

```powershell
.\.venv\Scripts\python.exe .opencode\skills\despliegue-streamlit\scripts\run_pipeline.py
```

El pipeline analiza las fuentes, calcula métricas, genera figuras, renderiza la landing y la app, reescribe el Word y valida los enlaces.

## 10. Limitaciones

- La regresión lineal supone relaciones lineales que no siempre se cumplen.
- El dataset es agregado por bloque censal y corresponde a 1990; no refleja el mercado actual.
- El valor máximo está censurado en 500,001 dólares.
- No se incluyen variables categóricas ni interacciones.
- Las predicciones son estimaciones académicas, no avalúos profesionales.

## 11. Ética y uso responsable

- **Privacidad y protección de datos:** Se utilizan datos públicos agregados por bloque censal. No se incorporan datos personales ni identificadores individuales. Cualquier uso futuro con datos institucionales requeriría anonimización y cumplimiento normativo.
- **Sesgo y representatividad:** Se reconoce que el dataset corresponde a California en 1990 y puede no representar otros territorios o periodos. Se documentan las limitaciones y se evita presentar el modelo como predictor universal.
- **Transparencia y explicabilidad:** Se publican coeficientes, métricas y limitaciones. La app muestra el resultado y advierte que es una estimación académica. No se oculta el error del modelo.
- **Riesgo de estigmatización:** No se clasifican personas ni comunidades como buenas o malas. Las variables geográficas se interpretan como contexto agregado, no como juicio sobre sus habitantes.
- **Supervisión humana:** Las predicciones son de apoyo. Cualquier decisión inmobiliaria o financiera debe ser validada por profesionales y por la persona usuaria.

## 12. Referencias

- Pace, R. K., & Barry, R. (1997). Sparse spatial autoregressions. Statistics & Probability Letters, 33(3), 291-297.
- Pedregosa, F. et al. (2011). Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research, 12, 2825-2830.
- scikit-learn Developers. California housing dataset. https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset
- Streamlit. Streamlit documentation. https://docs.streamlit.io
- Studer, S. et al. (2021). Towards CRISP-ML(Q): A Machine Learning Process Model with Quality Assurance Methodology. Machine Learning and Knowledge Extraction, 3(2), 392-413.
- McKinney, W. (2010). Data Structures for Statistical Computing in Python. Proceedings of the 9th Python in Science Conference.
