from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

PROJECT_TITLE = "Predicci\u00f3n de Precios de Viviendas con Regresi\u00f3n Lineal"
PROJECT_SHORT = "Housing Price ML"
PROJECT_SUBTITLE = "De los datos al despliegue: un caso pr\u00e1ctico de Machine Learning supervisado con California Housing"
AUTHOR = "Feibert Alirio Guzm\u00e1n P\u00e9rez"
COURSE = "Machine Learning I"
INSTITUTION = "UFHEC"
REPO_URL = "https://github.com/TU-USUARIO/TU-REPO"
PAGES_URL = "https://TU-USUARIO.github.io/TU-REPO/"
STREAMLIT_URL = ""
DATA_PATH = Path(__file__).resolve().parent / "housing.csv"
FIGURES_DIR = Path(__file__).resolve().parent / "assets" / "figures"
FEATURES = ["longitude", "latitude", "housing_median_age", "total_rooms", "total_bedrooms", "population", "households", "median_income"]
TARGET = "median_house_value"
DEFAULTS = [{"default": 3.5348, "label": "Ingreso mediano del bloque (decenas de miles de USD)", "max": 15.0001, "min": 0.4999, "name": "median_income", "step": 0.1}, {"default": 29.0, "label": "Edad mediana de las viviendas", "max": 52.0, "min": 1.0, "name": "housing_median_age", "step": 1.0}, {"default": 2127.0, "label": "Total de habitaciones del bloque", "max": 39320.0, "min": 2.0, "name": "total_rooms", "step": 10.0}, {"default": 435.0, "label": "Total de dormitorios del bloque", "max": 6445.0, "min": 1.0, "name": "total_bedrooms", "step": 1.0}, {"default": 1166.0, "label": "Poblaci\u00f3n del bloque", "max": 35682.0, "min": 3.0, "name": "population", "step": 10.0}, {"default": 409.0, "label": "Hogares del bloque", "max": 6082.0, "min": 1.0, "name": "households", "step": 1.0}]
DISCLAIMER = "Esta simulaci\u00f3n es una estimaci\u00f3n acad\u00e9mica basada en un modelo lineal entrenado con datos de 1990. No constituye un aval\u00fao ni una recomendaci\u00f3n financiera."
LIMITATIONS = ["La regresi\u00f3n lineal supone relaciones lineales que no siempre se cumplen.", "El dataset es agregado por bloque censal y corresponde a 1990; no refleja el mercado actual.", "El valor m\u00e1ximo est\u00e1 censurado en 500,001 d\u00f3lares.", "No se incluyen variables categ\u00f3ricas ni interacciones.", "Las predicciones son estimaciones acad\u00e9micas, no aval\u00faos profesionales."]
INSIGHTS = ["median_income es la variable con mayor correlaci\u00f3n positiva con median_house_value.", "La ubicaci\u00f3n geogr\u00e1fica explica parte importante del precio: la costa y las \u00e1reas metropolitanas concentran valores m\u00e1s altos.", "total_bedrooms tiene 207 valores nulos; se imputan con la mediana para no perder registros.", "La variable objetivo est\u00e1 acotada en 500,001 d\u00f3lares, lo que genera un efecto techo en las predicciones.", "Existen valores at\u00edpicos en total_rooms, population y households que deben interpretarse con cautela."]
TARGET_MIN = float(14999.0)
TARGET_MAX = float(500001.0)

st.set_page_config(
    page_title=PROJECT_TITLE,
    page_icon="assets/images/favicon.svg",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    f"""
<style>
    :root {{
        --ink: #0B1220;
        --ink-soft: #111C31;
        --surface: #F7F9FC;
        --cyan: #22D3EE;
        --teal: #14B8A6;
        --amber: #F59E0B;
        --slate: #64748B;
        --line: #DCE4EF;
    }}
    .stApp {{
        background:
            radial-gradient(circle at 92% 6%, rgba(34, 211, 238, 0.10), transparent 34%),
            radial-gradient(circle at 4% 92%, rgba(20, 184, 166, 0.08), transparent 30%),
            var(--surface);
    }}
    .block-container {{ padding-top: 2.2rem; max-width: 1180px; }}
    h1, h2, h3 {{ letter-spacing: -0.03em; }}
    .hero {{
        border: 1px solid var(--line);
        border-radius: 26px;
        padding: clamp(26px, 5vw, 54px);
        background: linear-gradient(135deg, var(--ink) 0%, var(--ink-soft) 58%, #12304a 100%);
        color: #f7f9fc;
        box-shadow: 0 28px 80px rgba(11, 18, 32, 0.18);
        margin-bottom: 22px;
    }}
    .hero .kicker {{
        color: var(--cyan);
        font-size: 0.76rem;
        font-weight: 800;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        margin-bottom: 14px;
    }}
    .hero h1 {{ font-size: clamp(2.1rem, 5vw, 4rem); margin: 0 0 14px; line-height: 1.05; }}
    .hero p {{ color: #c7d2e5; font-size: 1.08rem; max-width: 62ch; margin: 0 0 18px; }}
    .hero .meta {{ color: #8fa3bf; font-size: 0.9rem; }}
    .stat-grid {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px; margin: 18px 0 8px; }}
    .stat {{
        background: #ffffff;
        border: 1px solid var(--line);
        border-radius: 16px;
        padding: 18px;
    }}
    .stat strong {{ display: block; font-size: 1.8rem; letter-spacing: -0.04em; line-height: 1.1; color: var(--ink); }}
    .stat span {{ color: var(--slate); font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; }}
    .card {{
        background: #ffffff;
        border: 1px solid var(--line);
        border-radius: 18px;
        padding: 20px;
        margin-bottom: 12px;
    }}
    .card h3 {{ margin: 0 0 8px; font-size: 1.05rem; }}
    .card p {{ color: var(--slate); margin: 0; }}
    .pill {{
        display: inline-block;
        padding: 4px 10px;
        border-radius: 999px;
        background: rgba(20, 184, 166, 0.12);
        color: var(--teal);
        font-size: 0.72rem;
        font-weight: 800;
        letter-spacing: 0.04em;
        margin-bottom: 8px;
    }}
    .note {{ color: var(--slate); font-size: 0.85rem; }}
    .prediction {{
        background: linear-gradient(135deg, var(--ink), #12304a);
        color: #ffffff;
        border-radius: 20px;
        padding: 26px;
    }}
    .prediction small {{ color: #8fa3bf; display: block; margin-bottom: 6px; }}
    .prediction strong {{ display: block; font-size: clamp(2rem, 5vw, 3.4rem); letter-spacing: -0.05em; line-height: 1; }}
    .prediction span {{ display: block; color: #c7d2e5; margin-top: 10px; font-size: 0.86rem; }}
    .stButton > button {{
        border-radius: 999px;
        background: var(--ink);
        color: #ffffff;
        border: 0;
        padding: 0.55rem 1.2rem;
        font-weight: 700;
    }}
    .stButton > button:hover {{ background: #12304a; color: #ffffff; }}
    .stTabs [data-baseweb="tab-list"] {{ gap: 6px; }}
    .stTabs [data-baseweb="tab"] {{ border-radius: 999px; padding: 8px 18px; }}
    [data-testid="stSidebar"] {{ background: #ffffff; border-right: 1px solid var(--line); }}
    @media (max-width: 760px) {{
        .stat-grid {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
    }}
    </style>    """,
    unsafe_allow_html=True,
)


@st.cache_data(show_spinner=False)
def load_data(path: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    raw = pd.read_csv(path)
    clean = raw.copy()
    clean["total_bedrooms"] = clean["total_bedrooms"].fillna(clean["total_bedrooms"].median())
    return raw, clean


@st.cache_resource(show_spinner=False)
def train_models(path: str) -> dict:
    _, clean = load_data(path)
    data = clean[FEATURES + [TARGET]].dropna()
    y = data[TARGET]
    simple = LinearRegression().fit(data[["median_income"]], y)
    X_train, X_test, y_train, y_test = train_test_split(
        data[FEATURES], y, test_size=0.2, random_state=42
    )
    multiple = LinearRegression().fit(X_train, y_train)
    prediction = multiple.predict(X_test)
    return {
        "simple": simple,
        "multiple": multiple,
        "mse": float(mean_squared_error(y_test, prediction)),
        "rmse": float(np.sqrt(mean_squared_error(y_test, prediction))),
        "mae": float(mean_absolute_error(y_test, prediction)),
        "r2": float(r2_score(y_test, prediction)),
        "intercept": float(multiple.intercept_),
        "coefficients": dict(zip(FEATURES, multiple.coef_.tolist())),
        "train_rows": int(len(X_train)),
        "test_rows": int(len(X_test)),
        "y_test": y_test.reset_index(drop=True),
        "prediction": pd.Series(prediction),
    }


def money(value: float) -> str:
    return f"${value:,.0f}"


def metric_card(label: str, value: str, detail: str) -> str:
    return f'<div class="stat"><strong>{value}</strong><span>{label}</span><br><small class="note">{detail}</small></div>'


def hero() -> None:
    st.markdown(
        f"""
        <div class="hero">
            <div class="kicker">Machine Learning supervisado · CRISP-ML(Q)</div>
            <h1>{PROJECT_TITLE}</h1>
            <p>{PROJECT_SUBTITLE}</p>
            <div class="meta">{AUTHOR} · {COURSE} · {INSTITUTION}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def sidebar(models: dict) -> str:
    st.sidebar.markdown(f"### {PROJECT_SHORT}")
    st.sidebar.caption(f"{COURSE} · {INSTITUTION}")
    page = st.sidebar.radio(
        "Navegación",
        ["Inicio", "Datos", "Análisis exploratorio", "Modelo", "Simulador", "Documentación"],
        label_visibility="collapsed",
    )
    st.sidebar.divider()
    st.sidebar.metric("R² en prueba", f"{models['r2']:.3f}")
    st.sidebar.metric("RMSE", money(models["rmse"]))
    st.sidebar.caption(DISCLAIMER)
    return page


def page_home(models: dict) -> None:
    hero()
    st.markdown(
        f"""
        <div class="stat-grid">
            {metric_card("Registros", "20,640", "Bloques censales de California")}
            {metric_card("Variables", "8", "Predictores numéricos")}
            {metric_card("R²", f"{models['r2']:.3f}", "Variabilidad explicada")}
            {metric_card("RMSE", money(models['rmse']), "Error en dólares")}
        </div>
        """,
        unsafe_allow_html=True,
    )
    left, right = st.columns([1.15, 0.85])
    with left:
        st.markdown(
            """
            <div class="card">
                <span class="pill">Problema</span>
                <h3>Estimar el valor mediano de una vivienda</h3>
                <p>El precio depende de la ubicación, el tamaño, la antigüedad y el contexto socioeconómico.
                Este proyecto usa regresión lineal para aprender esa relación y comunicarla con transparencia.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="card">
                <span class="pill">Pregunta</span>
                <h3>¿Qué tan lejos puede llegar un modelo lineal?</h3>
                <p>Comparamos una regresión simple con el ingreso mediano frente a una regresión múltiple
                con ocho variables numéricas. El objetivo no es solo predecir: también interpretar.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with right:
        st.markdown("#### Ruta del proyecto")
        for number, name in [
            ("01", "Comprensión del problema"),
            ("02", "Preparación de datos"),
            ("03", "Análisis exploratorio"),
            ("04", "Modelado y evaluación"),
            ("05", "Despliegue y comunicación"),
        ]:
            st.markdown(
                f'<div class="card"><strong>{number}</strong> &nbsp; {name}</div>',
                unsafe_allow_html=True,
            )

    st.markdown("#### Hallazgos principales")
    for insight in INSIGHTS:
        st.markdown(f"- {insight}")

    st.info(
        "Esta aplicación es un recurso académico. Los datos corresponden a California en 1990 y el modelo "
        "no sustituye un avalúo profesional ni una decisión financiera."
    )


def page_data(raw: pd.DataFrame, clean: pd.DataFrame) -> None:
    st.title("Datos")
    st.caption("California Housing: 20,640 bloques censales, 10 columnas y una variable objetivo continua.")
    left, right, third = st.columns(3)
    left.metric("Filas", f"{len(raw):,}")
    right.metric("Columnas", str(raw.shape[1]))
    third.metric("Nulos en total_bedrooms", f"{int(raw['total_bedrooms'].isna().sum())}")
    st.markdown("#### Vista previa")
    st.dataframe(raw.head(12), width="stretch", hide_index=True)
    st.markdown("#### Calidad de datos")
    missing = raw.isna().sum().rename("nulos").to_frame()
    missing["porcentaje"] = (missing["nulos"] / len(raw) * 100).round(2)
    st.dataframe(missing, width="stretch")
    st.markdown("#### Estadísticas descriptivas")
    st.dataframe(raw.describe().T, width="stretch")
    st.caption(
        "La imputación de total_bedrooms se realiza con la mediana. "
        "ocean_proximity se excluye del modelo lineal por ser categórica."
    )


def page_eda() -> None:
    st.title("Análisis exploratorio")
    st.write(
        "Las figuras resumen la relación entre variables, el patrón geográfico y la distribución del precio. "
        "Son la base para decidir qué variables incluir y cómo interpretar el modelo."
    )
    figures = [
        ("correlation-heatmap.png", "Matriz de correlación", "Relaciones lineales entre variables numéricas."),
        ("geographic-map.png", "Distribución geográfica", "El color representa el valor mediano de la vivienda."),
        ("simple-regression.png", "Regresión simple", "Ingreso mediano frente a valor mediano."),
        ("target-distribution.png", "Distribución del precio", "Concentración y efecto techo en 500,001 dólares."),
    ]
    columns = st.columns(2)
    for index, (filename, title, caption) in enumerate(figures):
        path = FIGURES_DIR / filename
        with columns[index % 2]:
            if path.exists():
                st.image(str(path), caption=f"{title}. {caption}", width="stretch")
            else:
                st.warning(f"No se encontró la figura {filename}. Ejecuta los scripts de assets.")
    st.markdown("#### Lectura de los hallazgos")
    for insight in INSIGHTS:
        st.markdown(f"- {insight}")


def page_model(models: dict) -> None:
    st.title("Modelo y resultados")
    st.write(
        "La regresión múltiple se entrena con una división 80/20 y se evalúa sobre datos no vistos. "
        "Las métricas se reportan en dólares, excepto R²."
    )
    columns = st.columns(4)
    columns[0].metric("MSE", f"${models['mse']:,.0f}")
    columns[1].metric("RMSE", money(models["rmse"]))
    columns[2].metric("MAE", money(models["mae"]))
    columns[3].metric("R²", f"{models['r2']:.4f}")
    st.caption(
        f"Entrenamiento: {models['train_rows']:,} filas · Prueba: {models['test_rows']:,} filas · "
        f"Intercepto del modelo múltiple: {money(models['intercept'])}."
    )
    left, right = st.columns([1.1, 0.9])
    with left:
        st.markdown("#### Coeficientes del modelo múltiple")
        coefficients = pd.DataFrame(
            {
                "variable": FEATURES,
                "coeficiente": [models["coefficients"][name] for name in FEATURES],
            }
        )
        coefficients["coeficiente"] = coefficients["coeficiente"].map(lambda value: f"{value:,.2f}")
        st.dataframe(coefficients, width="stretch", hide_index=True)
        st.caption(
            "Los coeficientes describen asociaciones ajustadas por las demás variables. "
            "No deben interpretarse como relaciones causales."
        )
    with right:
        st.markdown("#### Regresión simple")
        simple = models["simple"]
        st.markdown(
            f'<div class="card"><span class="pill">median_income</span>'
            f"<h3>{money(simple.intercept_)} + {money(simple.coef_[0])} × ingreso</h3>"
            "<p>Por cada 10,000 dólares adicionales de ingreso mediano, el modelo estima un aumento "
            "promedio de 41,793.85 dólares en el valor de la vivienda.</p></div>",
            unsafe_allow_html=True,
        )
        st.markdown("#### Comparación")
        st.markdown(
            "El modelo múltiple mejora la capacidad explicativa frente a la regresión simple, "
            "pero sigue dejando fuera relaciones no lineales y la variable categórica ocean_proximity."
        )
    st.markdown("#### Límites del modelo")
    for limitation in LIMITATIONS:
        st.markdown(f"- {limitation}")
    with st.expander("Ver gráfico de valores reales frente a predicciones"):
        figure, axis = plt.subplots(figsize=(7, 5))
        axis.scatter(models["y_test"], models["prediction"], alpha=0.25, s=12, color="#14B8A6")
        axis.plot([TARGET_MIN, TARGET_MAX], [TARGET_MIN, TARGET_MAX], color="#FB7185", linewidth=2)
        axis.set_xlabel("Valor real")
        axis.set_ylabel("Predicción")
        axis.set_title("Predicción frente a valor real")
        axis.grid(alpha=0.2)
        st.pyplot(figure, width="stretch")
        plt.close(figure)


def page_simulator(models: dict) -> None:
    st.title("Simulador de predicción")
    st.write(
        "Ajusta las variables del bloque censal y obtén una estimación del valor mediano de la vivienda. "
        "La estimación usa el modelo múltiple entrenado con los datos del proyecto."
    )
    defaults = {item["name"]: item for item in DEFAULTS}
    with st.form("simulator"):
        left, right = st.columns(2)
        values = {}
        with left:
            for name in ["median_income", "housing_median_age", "total_rooms"]:
                item = defaults[name]
                values[name] = st.slider(
                    item["label"],
                    float(item["min"]),
                    float(item["max"]),
                    float(item["default"]),
                    float(item["step"]),
                )
        with right:
            for name in ["total_bedrooms", "population", "households"]:
                item = defaults[name]
                values[name] = st.slider(
                    item["label"],
                    float(item["min"]),
                    float(item["max"]),
                    float(item["default"]),
                    float(item["step"]),
                )
        with st.expander("Ubicación del bloque"):
            location_left, location_right = st.columns(2)
            with location_left:
                values["longitude"] = st.slider("Longitud", -124.35, -114.31, -118.49, 0.01)
            with location_right:
                values["latitude"] = st.slider("Latitud", 32.54, 41.95, 34.26, 0.01)
        submitted = st.form_submit_button("Estimar valor")

    if submitted:
        row = pd.DataFrame([{name: values[name] for name in FEATURES}], columns=FEATURES)
        prediction = float(models["multiple"].predict(row)[0])
        prediction = max(0.0, prediction)
        simple_row = pd.DataFrame([{"median_income": values["median_income"]}])
        simple_prediction = max(0.0, float(models["simple"].predict(simple_row)[0]))
        st.markdown(
            f"""
            <div class="prediction">
                <small>Valor mediano estimado</small>
                <strong>{money(prediction)}</strong>
                <span>Regresión simple de referencia: {money(simple_prediction)}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.caption(DISCLAIMER)
        st.caption(
            f"La predicción se limita al rango observado del target: {money(TARGET_MIN)} a {money(TARGET_MAX)}. "
            "Valores fuera de ese rango deben interpretarse con mucha cautela."
        )
    else:
        st.info("Ajusta los controles y presiona Estimar valor para ver la predicción.")
    st.markdown("#### Cómo leer el resultado")
    st.markdown(
        "- El valor es una estimación promedio para un bloque censal, no para una vivienda individual.\n"
        "- El modelo es lineal: no captura interacciones complejas ni cambios del mercado.\n"
        "- Un error de decenas de miles de dólares es esperable; revisa el RMSE y el MAE.\n"
        "- No uses esta salida como avalúo, oferta o decisión financiera."
    )


def page_docs() -> None:
    st.title("Documentación")
    st.write("Guías y recursos para reproducir, entender y desplegar el proyecto.")
    st.markdown(
        f"""
        <div class="card">
            <h3>Repositorio</h3>
            <p><a href="{REPO_URL}">{REPO_URL}</a></p>
        </div>
        <div class="card">
            <h3>Landing page</h3>
            <p><a href="{PAGES_URL}">{PAGES_URL}</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        #### Archivos recomendados
        - `README.md`: presentación, instalación y despliegue.
        - `documentation/GUIA_INSTALACION.md`: entorno local paso a paso.
        - `documentation/DESPLIEGUE.md`: GitHub Pages y Streamlit Cloud.
        - `documentation/DOCUMENTACION_TECNICA.md`: datos, pipeline y modelo.
        - `documentation/GUIA_DOCENTE.md`: uso en clase y criterios de evaluación.
        - `notebooks/Project_RL_clean.ipynb`: flujo reproducible sin salidas inconsistentes.
        """
    )
    st.markdown("#### Reproducir en local")
    st.code(
        "python -m venv .venv\n"
        ".venv\\Scripts\\activate\n"
        "pip install -r requirements.txt\n"
        "streamlit run app.py",
        language="powershell",
    )
    st.caption(
        "En macOS o Linux, activa el entorno con source .venv/bin/activate. "
        "El comando de instalación es el mismo."
    )


def main() -> None:
    if not DATA_PATH.exists():
        st.error(f"No se encontró el dataset en {DATA_PATH}. Coloca housing.csv junto a app.py.")
        st.stop()
    raw, clean = load_data(str(DATA_PATH))
    models = train_models(str(DATA_PATH))
    page = sidebar(models)
    if page == "Inicio":
        page_home(models)
    elif page == "Datos":
        page_data(raw, clean)
    elif page == "Análisis exploratorio":
        page_eda()
    elif page == "Modelo":
        page_model(models)
    elif page == "Simulador":
        page_simulator(models)
    else:
        page_docs()


if __name__ == "__main__":
    main()
