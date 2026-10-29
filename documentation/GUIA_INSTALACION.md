# Guía de instalación y ejecución local

Esta guía permite reproducir el proyecto en Windows, macOS o Linux sin conocimientos avanzados de DevOps.

## 1. Requisitos

- Python 3.11 o superior.
- Git (recomendado para clonar y versionar).
- Un navegador moderno.
- 4 GB de RAM como mínimo recomendado.

Verifica la instalación:

```powershell
python --version
git --version
```

Si `python` no está disponible en Windows, usa `py --version` o instala Python desde [python.org](https://www.python.org/downloads/).

## 2. Obtener el proyecto

### Opción A: clonar el repositorio

```powershell
git clone https://github.com/TU-USUARIO/TU-REPO
cd TU-REPO
```

### Opción B: descargar el ZIP

Descarga el repositorio, descomprime la carpeta y abre una terminal dentro de ella.

## 3. Crear el entorno virtual

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

Si PowerShell bloquea la activación, ejecuta una vez:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### macOS o Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Sabrás que el entorno está activo porque la terminal muestra `(.venv)`.

## 4. Instalar dependencias

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Dependencias principales:

| Paquete | Uso |
|---|---|
| `streamlit` | Aplicación interactiva. |
| `pandas` | Carga y transformación de datos. |
| `numpy` | Operaciones numéricas. |
| `scikit-learn` | Regresión lineal y métricas. |
| `matplotlib` | Figuras del análisis. |
| `seaborn` | Visualizaciones estadísticas. |
| `joblib` | Serialización de modelos. |

Si necesitas regenerar la documentación o el Word, instala también:

```powershell
pip install python-docx PyYAML Jinja2 nbformat beautifulsoup4 Pillow nbconvert
```

## 5. Verificar el dataset

El archivo `housing.csv` debe estar en la raíz del proyecto:

```powershell
Get-ChildItem housing.csv
```

Debe contener 20,640 filas y 10 columnas. Si falta, descárgalo desde la fuente indicada en [`FUENTES_Y_DATOS.md`](FUENTES_Y_DATOS.md).

## 6. Ejecutar la aplicación

```powershell
streamlit run app.py
```

Streamlit abrirá `http://localhost:8501`. Si no lo hace, visita la URL manualmente.

Para detener la app, presiona `Ctrl+C` en la terminal.

## 7. Ejecutar la landing

La landing es estática. Puedes abrir `index.html` directamente en el navegador. Para una experiencia más cercana a producción:

```powershell
python -m http.server 8000
```

Visita `http://localhost:8000`.

## 8. Abrir el notebook

```powershell
jupyter notebook notebooks/Project_RL_clean.ipynb
```

Si no tienes Jupyter instalado:

```powershell
pip install notebook
```

También puedes abrir el archivo desde VS Code con la extensión de Jupyter.

## 9. Problemas frecuentes

| Síntoma | Causa probable | Solución |
|---|---|---|
| `python` abre otra instalación | Alias o venv previo | Usa `.\.venv\Scripts\python.exe` explícitamente. |
| `No module named streamlit` | Entorno virtual no activado | Activa `.venv` e instala de nuevo. |
| `FileNotFoundError: housing.csv` | Dataset fuera de la raíz | Coloca `housing.csv` junto a `app.py`. |
| La app no refleja cambios | Caché de Streamlit | Recarga o usa el menú de Streamlit. |
| El puerto 8501 está ocupado | Otra app en ejecución | `streamlit run app.py --server.port 8502`. |
| PowerShell bloquea scripts | Política de ejecución | Ajusta `ExecutionPolicy` como se indica arriba. |

## 10. Desinstalar el entorno

Solo elimina la carpeta `.venv`. El código y los datos no se modifican.
