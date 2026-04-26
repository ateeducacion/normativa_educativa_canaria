# GitHub Pages y documentos públicos

Este directorio contiene la versión estática y mantenible del panel público del repositorio.

## Contenido principal

- `index.html`: panel principal del corpus.
- `skill.html`: skill copiable para asistentes de IA.
- `assets/css/site.css`: estilos estáticos.
- `assets/js/site.js`: filtro cliente sin backend.
- `esquema-datos/`, `guias/`, `metodologia/`: documentación complementaria.

`llms.txt` y `llms-full.txt` no se almacenan aquí. Tienen su única copia en la raíz del repositorio y se publican como `https://ateeducacion.github.io/normativa_educativa_canaria/llms.txt` y `…/llms-full.txt` mediante el flujo de trabajo `Publicar GitHub Pages`.

## Publicación con GitHub Actions

El sitio se construye y despliega con `.github/workflows/pages.yml`. El flujo:

1. Toma todo el contenido de `docs/`.
2. Copia `llms.txt` y `llms-full.txt` desde la raíz del repositorio al artefacto Pages.
3. Sube el artefacto y lo despliega en GitHub Pages.

Para activar la publicación una vez:

1. Abra la configuración del repositorio en GitHub.
2. Entre en **Pages**.
3. En **Build and deployment**, seleccione **GitHub Actions** como origen.
4. Guarde los cambios.
5. El primer push a `main` que toque `docs/`, `llms.txt`, `llms-full.txt` o el propio workflow lanzará el despliegue. También se puede lanzar a mano desde la pestaña **Actions** con **Run workflow**.

## URLs públicas esperadas

- `https://ateeducacion.github.io/normativa_educativa_canaria/`
- `https://ateeducacion.github.io/normativa_educativa_canaria/llms.txt`
- `https://ateeducacion.github.io/normativa_educativa_canaria/llms-full.txt`

## Notas de mantenimiento

- Edite `llms.txt` y `llms-full.txt` solo en la raíz del repositorio. No existe copia en `docs/`. El despliegue las añade automáticamente al sitio publicado.
- Si necesita previsualizar el sitio en local, copie temporalmente esos dos archivos a `docs/` o use el mismo procedimiento que el workflow.
- Para añadir páginas nuevas al sitio, añada el archivo dentro de `docs/` y actualice la navegación de `index.html` si procede.
