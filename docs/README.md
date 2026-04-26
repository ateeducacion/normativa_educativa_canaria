# GitHub Pages y documentos públicos

Este directorio contiene la versión estática y mantenible del panel público del repositorio.

## Contenido principal

- `index.html`: panel principal del corpus.
- `skill.html`: skill copiable para asistentes de IA.
- `assets/css/site.css`: estilos estáticos.
- `assets/js/site.js`: filtro cliente sin backend.
- `esquema-datos/`, `guias/`, `metodologia/`: documentación complementaria.

`llms.txt`, `llms-full.txt` y `skill.md` no se almacenan aquí. Tienen su única copia canónica en la raíz del repositorio o en `skills/`, y se publican como `https://ateeducacion.github.io/normativa_educativa_canaria/llms.txt`, `…/llms-full.txt` y `…/skill.md` mediante el flujo de trabajo `Publicar GitHub Pages`.

## Publicación con GitHub Actions

El sitio se construye y despliega con `.github/workflows/pages.yml`. El flujo:

1. Toma todo el contenido de `docs/`.
2. Copia al artefacto Pages los ficheros Markdown/YAML públicos del corpus (`README.md`, `index.md`, `status.yaml`, `AGENTS.md`, `00_gobierno-repositorio/`, `01_fuentes/`, `02_normativa/`, `03_curriculos/`, `05_relaciones/`, `06_indices/`, `07_corpus_ia/` y `09_decisiones-editoriales/`).
3. Copia `llms.txt`, `llms-full.txt` y la skill canónica al artefacto Pages.
4. Sube el artefacto y lo despliega en GitHub Pages.

Para activar la publicación una vez:

1. Abra la configuración del repositorio en GitHub.
2. Entre en **Pages**.
3. En **Build and deployment**, seleccione **GitHub Actions** como origen.
4. Guarde los cambios.
5. El primer push a `main` que toque `docs/`, `llms.txt`, `llms-full.txt`, `skills/experto-normativa-educativa-canaria/SKILL.md` o el propio workflow lanzará el despliegue. También se puede lanzar a mano desde la pestaña **Actions** con **Run workflow**.

## URLs públicas esperadas

- `https://ateeducacion.github.io/normativa_educativa_canaria/`
- `https://ateeducacion.github.io/normativa_educativa_canaria/llms.txt`
- `https://ateeducacion.github.io/normativa_educativa_canaria/llms-full.txt`
- `https://ateeducacion.github.io/normativa_educativa_canaria/skill.md`
- `https://ateeducacion.github.io/normativa_educativa_canaria/06_indices/curriculos.yaml`
- `https://ateeducacion.github.io/normativa_educativa_canaria/03_curriculos/eso/materias/CUR-001-biologia-y-geologia.md`
- `https://ateeducacion.github.io/normativa_educativa_canaria/03_curriculos/eso/materias/CUR-001-biologia-y-geologia.yaml`

## Notas de mantenimiento

- Edite `llms.txt` y `llms-full.txt` solo en la raíz del repositorio, y la skill solo en `skills/experto-normativa-educativa-canaria/SKILL.md`. No existe copia en `docs/`. El despliegue las añade automáticamente al sitio publicado junto con el corpus Markdown/YAML expuesto en GitHub Pages.
- Si necesita previsualizar el sitio en local, copie temporalmente esos dos archivos a `docs/` o use el mismo procedimiento que el workflow.
- Para añadir páginas nuevas al sitio, añada el archivo dentro de `docs/` y actualice la navegación de `index.html` si procede.
