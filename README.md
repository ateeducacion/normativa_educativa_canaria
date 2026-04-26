# Normativa Educativa Canaria

Repositorio IA-friendly para recopilar, analizar, resumir, indexar y relacionar normativa educativa y currículos aplicables a Canarias.

> Los resúmenes de este repositorio no sustituyen la consulta de las fuentes oficiales.

## Propósito

- centralizar fuentes oficiales y fichas normativas en formatos legibles;
- mantener metadatos estructurados en YAML;
- preparar contenido trazable para búsqueda semántica, RAG y asistentes internos;
- separar normativa, currículos, análisis, relaciones, preguntas y tareas.

## Principios del repositorio

1. **Sencillez primero.**
2. **IA-friendly.**
3. **Markdown para contenido narrativo.**
4. **YAML para metadatos estructurados.**
5. **Fuente oficial obligatoria.**
6. **Fecha de consulta obligatoria.**
7. **Fecha de análisis obligatoria cuando haya interpretación o resumen.**
8. **Estado de vigencia obligatorio.**
9. **Relaciones normativas explícitas.**
10. **No copiar normas completas si basta con resumen, cita y enlace oficial.**
11. **No mezclar normativa con recursos no normativos.**
12. **No borrar contenido histórico: marcar como derogado, obsoleto o sustituido.**
13. **Usar IDs estables y correlativos.**
14. **Todo resumen debe indicar que no sustituye la fuente oficial.**
15. **Todo índice debe ser legible por humanos y máquinas.**

## Estructura principal

- `00_gobierno-repositorio/`: metodología, criterios editoriales y glosario operativo.
- `01_fuentes/`: fichas de fuentes oficiales.
- `02_normativa/`: fichas Markdown de normas.
- `03_curriculos/`: currículos en Markdown y YAML.
- `04_analisis/`: notas, comparativas y síntesis.
- `05_relaciones/`: relaciones normativas y curriculares.
- `06_indices/`: índices YAML del corpus.
- `07_corpus_ia/`: resúmenes y chunks para IA.
- `08_tareas/`: backlog, diario y preguntas abiertas.
- `09_decisiones-editoriales/`: ADRs del repositorio.
- `10_plantillas/`: plantillas reutilizables.
- `11_calidad/`: validaciones e informes.
- `docs/`: guías metodológicas y esquema de datos.

## Arranque rápido

- Índice principal: [index.md](index.md)
- Gobierno del repositorio: [00_gobierno-repositorio/](00_gobierno-repositorio/)
- Fuentes: [06_indices/fuentes.yaml](06_indices/fuentes.yaml)
- Normativa: [06_indices/normativa.yaml](06_indices/normativa.yaml)
- Currículos: [06_indices/curriculos.yaml](06_indices/curriculos.yaml)
- Relaciones: [06_indices/relaciones.yaml](06_indices/relaciones.yaml)
- Preguntas abiertas: [06_indices/preguntas.yaml](06_indices/preguntas.yaml)

## Uso como contexto de IA

Vía rápida con un cliente compatible con MCP (VS Code 1.101+, Claude Code, Cursor):

```json
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/x/repos/readonly"
    }
  }
}
```

Después, en el prompt:

```text
Abre el repositorio ateeducacion/normativa_educativa_canaria. Lee primero llms.txt y responde usando los archivos del repositorio como contexto. Cita las normas por su denominación oficial.
```

Detalle completo, alternativas con Docker y guía de seguridad: [`MCP.md`](MCP.md).

## Estado actual del corpus

- Fuentes catalogadas hasta `FTE-055`.
- Normativa indexada hasta `NOR-059`.
- Currículos registrados hasta `CUR-058`: Infantil, Primaria, ESO, Bachillerato y primeros ciclos FP.
- Chunks IA registrados hasta `CHUNK-00022`.
- La extracción FP sigue abierta en `TAREA-042` a `TAREA-045` para correcciones de Sanidad, completar Integración Social y extraer criterios de evaluación completos en Administración e Informática.
