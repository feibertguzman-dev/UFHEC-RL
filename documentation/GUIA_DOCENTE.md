# Guía docente

## 1. Propósito

Este proyecto es un caso completo de Machine Learning supervisado para enseñar regresión lineal con datos reales. Conecta teoría, código, evaluación y despliegue en una sola entrega.

## 2. Resultados de aprendizaje

Al finalizar el recorrido, el estudiante debería poder:

- Formular un problema de regresión y definir la variable objetivo.
- Explorar un dataset, detectar nulos y valores atípicos.
- Entrenar regresión lineal simple y múltiple con scikit-learn.
- Interpretar MSE, RMSE, MAE y R².
- Explicar coeficientes sin confundir asociación con causalidad.
- Publicar una landing y una app interactiva con advertencias de uso.

## 3. Duración sugerida

| Sesión | Tema | Tiempo |
|---|---|---|
| 1 | Problema, dataset y EDA | 2 horas |
| 2 | Regresión simple y múltiple | 2 horas |
| 3 | Evaluación e interpretación | 2 horas |
| 4 | Landing, Streamlit y ética | 2 horas |

## 4. Secuencia didáctica

### Sesión 1: contexto y datos

1. Presenta la pregunta de investigación y el alcance.
2. Abre `notebooks/Project_RL_clean.ipynb` y ejecuta la carga.
3. Pide al grupo identificar nulos, tipos y rangos.
4. Discute por qué `ocean_proximity` se excluye del modelo lineal.

### Sesión 2: modelado

1. Explica la ecuación de regresión simple.
2. Entrena el modelo con `median_income`.
3. Compara con la regresión múltiple.
4. Pide interpretar dos coeficientes y detectar señales de multicolinealidad.

### Sesión 3: evaluación

1. Revisa MSE, RMSE, MAE y R².
2. Discute por qué un R² alto no implica un modelo útil.
3. Analiza el efecto techo en 500,001 dólares.
4. Pide proponer una mejora: variables categóricas, interacciones o modelo no lineal.

### Sesión 4: comunicación y ética

1. Abre la landing y la app.
2. Prueba el simulador con valores extremos.
3. Discute el riesgo de usar la predicción como avalúo.
4. Revisa la documentación y la licencia.

## 5. Actividades de evaluación

| Actividad | Evidencia | Peso sugerido |
|---|---|---|
| Análisis exploratorio | Notebook con hallazgos y figuras | 20% |
| Modelado | Regresión simple y múltiple funcionando | 25% |
| Evaluación | Métricas y lectura crítica | 25% |
| Comunicación | Landing clara y sin errores | 15% |
| Ética | Limitaciones y advertencias visibles | 15% |

## 6. Preguntas para discusión

- ¿Qué significa que el modelo explique el 61.39% de la varianza?
- ¿Por qué la longitud y la latitud tienen coeficientes negativos?
- ¿Qué pasaría si incluyéramos `ocean_proximity` sin codificarla?
- ¿Cómo cambia la interpretación si usamos logaritmos?
- ¿Qué riesgo tiene desplegar un modelo entrenado con datos de 1990?
- ¿Qué información falta para tomar una decisión inmobiliaria real?

## 7. Errores frecuentes

| Error | Corrección |
|---|---|
| Confundir correlación con causalidad | Interpretar coeficientes como asociaciones ajustadas. |
| Usar el conjunto de prueba para entrenar | Mantener la división 80/20 y evaluar solo al final. |
| Ocultar el error del modelo | Publicar RMSE, MAE y limitaciones. |
| Presentar el simulador como avalúo | Aviso académico visible y lenguaje cuidadoso. |
| Ignorar el efecto techo | Explicar el límite de 500,001 dólares. |

## 8. Adaptaciones

- **Curso introductorio:** usa solo la regresión simple y la landing.
- **Curso intermedio:** agrega codificación de `ocean_proximity` y validación cruzada.
- **Curso avanzado:** compara con Random Forest o Gradient Boosting y analiza residuos.
- **Evaluación en línea:** pide un video de 5 minutos explicando el simulador y sus límites.

## 9. Recursos

- [Documentación técnica](DOCUMENTACION_TECNICA.md)
- [Guía de instalación](GUIA_INSTALACION.md)
- [Guía de despliegue](DESPLIEGUE.md)
- [Fuentes y datos](FUENTES_Y_DATOS.md)
