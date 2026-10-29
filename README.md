# Predicción de Precios de Viviendas con Regresión Lineal

De los datos al despliegue: un caso práctico de Machine Learning supervisado con California Housing

![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![pandas 3.x](https://img.shields.io/badge/pandas-3.x-150458?logo=pandas&logoColor=white)
![NumPy 2.x](https://img.shields.io/badge/NumPy-2.x-013243?logo=numpy&logoColor=white)
![scikit-learn 1.9](https://img.shields.io/badge/scikit-learn-1.9-F7931E?logo=scikitlearn&logoColor=white)
![Streamlit 1.66](https://img.shields.io/badge/Streamlit-1.66-FF4B4B?logo=streamlit&logoColor=white)
![HTML5 5](https://img.shields.io/badge/HTML5-5-E34F26?logo=html5&logoColor=white)
![CSS3 3](https://img.shields.io/badge/CSS3-3-1572B6?logo=css3&logoColor=white)
![JavaScript ES6+](https://img.shields.io/badge/JavaScript-ES6%2B-F7DF1E?logo=javascript&logoColor=white)
![GitHub Pages live](https://img.shields.io/badge/GitHub%20Pages-live-222222?logo=githubpages&logoColor=white)
![Licencia MIT](https://img.shields.io/badge/Licencia-MIT-22C55E?logo=opensourceinitiative&logoColor=white)

> Proyecto académico de **Machine Learning I** en **UFHEC**. Recorre el ciclo completo de un modelo supervisado: exploración, limpieza, entrenamiento, evaluación, landing documental y simulador interactivo.

## Demo

| Recurso | Enlace |
|---|---|
| Landing page | https://TU-USUARIO.github.io/TU-REPO/ |
| Aplicación Streamlit | Pendiente de publicar |
| Notebook limpio | [`notebooks/Project_RL_clean.ipynb`](notebooks/Project_RL_clean.ipynb) |
| Documento Word | [`documentation/Material_1_Proyecto_ML_UFHEC.docx`](documentation/Material_1_Proyecto_ML_UFHEC.docx) |

Los enlaces de GitHub Pages y Streamlit usan marcadores (`TU-USUARIO`, `TU-REPO`) hasta que se realice el despliegue. Reemplázalos en `work/content.yaml` y vuelve a ejecutar la skill.

## Qué incluye

- Landing estática responsive con narrativa del problema, teoría, datos, pipeline, EDA, código, resultados y simulador.
- Aplicación Streamlit con navegación, visualizaciones, métricas y simulador de predicción.
- Notebook limpio y reproducible, sin salidas inconsistentes.
- Documento Word reescrito a partir de la plantilla institucional.
- Documentación para instalar, desplegar, enseñar y auditar el proyecto.
- Figuras e ilustraciones SVG/PNG generadas desde el dataset.

## Dataset

**California Housing** · 20,640 registros · 10 columnas · variable objetivo `median_house_value`.

Los datos son agregados por bloque censal, no por vivienda individual. El valor máximo está censurado en 500,001 dólares, lo que limita las predicciones en la zona alta del mercado.

| Variable | Tipo | Rol |
|---|---|---|
| `longitude` | Numérica continua | Feature |
| `latitude` | Numérica continua | Feature |
| `housing_median_age` | Numérica discreta | Feature |
| `total_rooms` | Numérica discreta | Feature |
| `total_bedrooms` | Numérica discreta | Feature |
| `population` | Numérica discreta | Feature |
| `households` | Numérica discreta | Feature |
| `median_income` | Numérica continua | Feature principal |
| `median_house_value` | Numérica continua | Target |
| `ocean_proximity` | Categórica | Excluida |

Fuente: U.S. Census Bureau (1990), distribuido por StatLib y disponible en scikit-learn. Licencia: Uso académico y educativo; datos públicos agregados.

## Resultados

| Métrica | Valor | Lectura |
|---|---|---|
| MSE | $5.06 B | Penaliza con fuerza los errores grandes. |
| RMSE | $71,133 | Error típico en dólares. |
| MAE | $51,810 | Desviación absoluta promedio. |
| R² | 0.614 | 61.39% de la variabilidad explicada. |

Modelo simple: `median_house_value = 45,085.58 + 41,793.85 × median_income`.

El modelo múltiple explica aproximadamente el 61.39% de la variabilidad del precio en el conjunto de prueba. El error promedio absoluto es de 51,810.48 dólares y el RMSE de 71,133.17 dólares.

## Estructura del proyecto

```text
.
├── index.html                  Landing para GitHub Pages
├── app.py                      Aplicación Streamlit
├── requirements.txt            Dependencias de la app
├── housing.csv                 Dataset fuente
├── css/                        Estilos de la landing
├── js/                         Interacciones de la landing
├── assets/
│   ├── images/                 Ilustraciones SVG y OG image
│   └── figures/                Figuras del EDA
├── data/                       Espacio para datos derivados
├── documentation/              Guías y documento Word
├── notebooks/                  Notebook limpio
├── work/                       Contenido y métricas de la skill
└── .opencode/skills/           Skill reutilizable de despliegue
```

## Instalación rápida

Requisitos: Python 3.11 o superior, Git y un navegador moderno.

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

En macOS o Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecutar en local

```powershell
streamlit run app.py
```

Abre `http://localhost:8501`. Para ver la landing, abre `index.html` o ejecuta un servidor estático:

```powershell
python -m http.server 8000
```

Luego visita `http://localhost:8000`.

## Despliegue

### GitHub Pages

1. Crea el repositorio y sube el proyecto.
2. En **Settings → Pages**, selecciona **Deploy from a branch**.
3. Elige la rama `main` y la carpeta `/ (root)`.
4. Espera la publicación y actualiza `pages_url` en `work/content.yaml`.

### Streamlit Community Cloud

1. Entra a [share.streamlit.io](https://share.streamlit.io) y conecta el repositorio.
2. Selecciona `app.py` como archivo principal.
3. Verifica que `housing.csv` esté en la raíz del repositorio.
4. Publica y copia la URL en `streamlit_url`.

Las instrucciones completas están en [`documentation/DESPLIEGUE.md`](documentation/DESPLIEGUE.md).

## Documentación

- [Guía de instalación](documentation/GUIA_INSTALACION.md)
- [Guía de despliegue](documentation/DESPLIEGUE.md)
- [Documentación técnica](documentation/DOCUMENTACION_TECNICA.md)
- [Guía docente](documentation/GUIA_DOCENTE.md)
- [Fuentes y datos](documentation/FUENTES_Y_DATOS.md)

## Ética y límites

El proyecto es académico y exploratorio. No sustituye un avalúo profesional ni una decisión financiera. El dataset es agregado por bloque censal, corresponde a California en 1990 y tiene un valor máximo censurado en 500,001 dólares. Las predicciones son estimaciones académicas: no constituyen avalúos ni recomendaciones financieras.

## Autoría

**Feibert Alirio Guzmán Pérez** · Docente e investigador · UFHEC · 2026-10-28.

Licencia [MIT](LICENSE).
