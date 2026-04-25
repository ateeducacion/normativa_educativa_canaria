# Normativa Educativa Canarias

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
- Fuentes: [06_indices/fuentes.yaml](06_indices/fuentes.yaml)
- Normativa: [06_indices/normativa.yaml](06_indices/normativa.yaml)
- Currículos: [06_indices/curriculos.yaml](06_indices/curriculos.yaml)
- Relaciones: [06_indices/relaciones.yaml](06_indices/relaciones.yaml)
- Preguntas abiertas: [06_indices/preguntas.yaml](06_indices/preguntas.yaml)

## Estado del bootstrap

- Fuentes iniciales `FTE-001` a `FTE-008` creadas.
- Normas iniciales `NOR-001` a `NOR-004` creadas.
- Currículos ESO `CUR-001` a `CUR-023` registrados con estado `Pendiente`.
- `PREG-001` abierta por falta de confirmación externa de la fuente oficial final del decreto autonómico de currículo ESO/Bachillerato.
