# Guía de despliegue

El proyecto tiene dos superficies independientes:

1. **Landing documental** en GitHub Pages.
2. **Simulador interactivo** en Streamlit Community Cloud.

Ambas se publican desde el mismo repositorio. Ningún script de este proyecto ejecuta el despliegue de forma automática: las credenciales, la creación del repositorio y la publicación quedan como puertas manuales.

## 1. Antes de desplegar

Completa estos datos en `work/content.yaml`:

```yaml
project:
  repo_url: "https://github.com/TU-USUARIO/TU-REPO"
  pages_url: "https://TU-USUARIO.github.io/TU-REPO/"
  streamlit_url: "https://TU-APP.streamlit.app"
```

Luego regenera la landing y el README:

```powershell
.\.venv\Scripts\python.exe .opencode\skills\despliegue-streamlit\scripts\run_pipeline.py
```

Verifica que `housing.csv` esté en la raíz y que el repositorio no incluya `.venv`, `work/` ni credenciales.

## 2. Publicar el repositorio

```powershell
git init
git add .
git commit -m "feat: publica proyecto de regresion lineal con landing y Streamlit"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/TU-REPO.git
git push -u origin main
```

No ejecutes estos comandos si el repositorio ya existe. En ese caso, revisa primero `git status` y `git remote -v`.

## 3. GitHub Pages

1. Abre el repositorio en GitHub.
2. Ve a **Settings → Pages**.
3. En **Build and deployment**, selecciona **Deploy from a branch**.
4. Elige la rama `main`.
5. Selecciona la carpeta `/ (root)`.
6. Guarda y espera la publicación.

La landing queda en:

```text
https://TU-USUARIO.github.io/TU-REPO/
```

El archivo `.nojekyll` ya está incluido para evitar que GitHub omita carpetas que empiezan con guion bajo.

### Verificación

- Abre la URL en una ventana privada.
- Revisa que carguen `css/styles.css`, `js/main.js` y las figuras.
- Comprueba los enlaces a documentación y al notebook.
- Valida que los badges y la imagen Open Graph respondan.

### Dominio personalizado

1. En **Settings → Pages → Custom domain**, escribe el dominio.
2. Crea un registro `CNAME` que apunte a `TU-USUARIO.github.io`.
3. Activa **Enforce HTTPS** cuando GitHub lo permita.
4. No agregues un archivo `CNAME` hasta tener el dominio listo.

## 4. Streamlit Community Cloud

1. Entra a [share.streamlit.io](https://share.streamlit.io).
2. Inicia sesión con GitHub.
3. Selecciona **New app**.
4. Elige el repositorio, la rama `main` y el archivo `app.py`.
5. Revisa la configuración de Python y confirma que `requirements.txt` está en la raíz.
6. Publica la app.

Streamlit instala las dependencias de `requirements.txt` y ejecuta `app.py`. La app carga `housing.csv` desde la raíz y entrena los modelos al iniciar.

### Verificación

- La app abre sin errores.
- El simulador responde a los controles.
- Las figuras del EDA cargan desde `assets/figures`.
- El aviso académico es visible.

### Actualizaciones

Cada `push` a `main` puede reconstruir la app. Si cambias dependencias, usa **Reboot app** en el panel de Streamlit.

## 5. Checklist de publicación

- [ ] `repo_url`, `pages_url` y `streamlit_url` actualizados.
- [ ] `index.html`, `README.md` y documentación regenerados.
- [ ] `housing.csv` presente y sin rutas absolutas.
- [ ] `.venv/`, `work/` y temporales fuera del repositorio.
- [ ] GitHub Pages publicada y verificada en ventana privada.
- [ ] Streamlit publicado y probado con varios valores.
- [ ] Enlaces de la landing sin errores 404.
- [ ] Aviso de uso académico visible en landing y app.
- [ ] Licencia y autoría correctas.

## 6. Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| GitHub Pages no publica | Revisa rama, carpeta y estado en Actions. |
| Streamlit no encuentra el CSV | Confirma que `housing.csv` esté en la raíz. |
| Dependencias incompatibles | Usa las versiones de `requirements.txt` y Python 3.11. |
| URLs con placeholders | Actualiza `content.yaml` antes de publicar. |
| Datos desactualizados | Mantén visible la fecha y las limitaciones. |
| Uso indebido del simulador | Aviso académico y enlace a la documentación técnica. |
