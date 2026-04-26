# GitHub Pages y documentos públicos

Este directorio contiene la versión estática y mantenible del panel público del repositorio.

## Contenido principal

- `index.html`: panel principal del corpus.
- `llms.txt`: punto de entrada corto para LLM.
- `llms-full.txt`: contexto ampliado para LLM.
- `mcp.html`: guía pública de uso con GitHub MCP Server.
- `assets/css/site.css`: estilos estáticos.
- `assets/js/site.js`: filtro cliente sin backend.

## Publicación recomendada con GitHub Pages

1. Abra la configuración del repositorio en GitHub.
2. Entre en **Pages**.
3. Seleccione **Deploy from a branch**.
4. Elija la rama `main`.
5. Seleccione la carpeta `/docs` como origen.
6. Guarde los cambios.
7. Compruebe el sitio publicado.

## URLs públicas esperadas

- `https://ateeducacion.github.io/normativa_educativa/`
- `https://ateeducacion.github.io/normativa_educativa/llms.txt`
- `https://ateeducacion.github.io/normativa_educativa/llms-full.txt`
- `https://ateeducacion.github.io/normativa_educativa/mcp.html`

## Notas de mantenimiento

- Se prefiere la publicación directa desde `/docs` porque no requiere build ni GitHub Actions.
- Si en el futuro hiciera falta un proceso de generación, entonces podría añadirse un workflow de Pages.
- `docs/llms.txt` y `docs/llms-full.txt` deben mantenerse consistentes con sus equivalentes en la raíz del repositorio.
