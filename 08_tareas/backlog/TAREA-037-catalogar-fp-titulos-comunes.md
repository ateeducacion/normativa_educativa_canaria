---
id: TAREA-037
titulo: "Catalogar RD de títulos FP más comunes en Canarias (fase acotada)"
estado: "En progreso"
prioridad: "Media"
tipo: "curriculo"
responsable: "@.agents/skills/experto-formacion-profesional"
fecha_creacion: 2026-04-26
fecha_actualizacion: 2026-04-26
relacionadas: [NOR-007, FTE-015, FTE-016]
---

# TAREA-037 — Catalogar RD de títulos FP más comunes en Canarias (fase acotada)

## Objetivo

Catalogar los Reales Decretos de título de los ciclos formativos con mayor matrícula en Canarias, agrupados en cuatro familias profesionales prioritarias. No se extraen todavía los resultados de aprendizaje ni los criterios de evaluación completos (eso corresponde a una fase posterior). Esta tarea se limita a:

1. Crear la estructura de carpetas `03_curriculos/fp/` (subcarpeta por familia).
2. Registrar una fuente FTE-054 para el catálogo de títulos en BOE.
3. Crear fichas NOR para los Reales Decretos de cada título seleccionado.
4. Crear fichas CUR placeholder (`estado_extraccion: "pendiente"`) para cada ciclo.
5. Actualizar los índices afectados.

## Familias y ciclos seleccionados

### Sanidad
| Grado | Título | RD a localizar |
|-------|--------|----------------|
| GM | Cuidados Auxiliares de Enfermería | [PENDIENTE] |
| GS | Imagen para el Diagnóstico y Medicina Nuclear | [PENDIENTE] |

### Administración y Gestión
| Grado | Título | RD a localizar |
|-------|--------|----------------|
| GM | Gestión Administrativa | [PENDIENTE] |
| GS | Administración y Finanzas | [PENDIENTE] |

### Informática y Comunicaciones
| Grado | Título | RD a localizar |
|-------|--------|----------------|
| GS | Desarrollo de Aplicaciones Multiplataforma (DAM) | [PENDIENTE] |
| GS | Desarrollo de Aplicaciones Web (DAW) | [PENDIENTE] |

### Servicios Socioculturales y a la Comunidad
| Grado | Título | RD a localizar |
|-------|--------|----------------|
| GS | Educación Infantil | [PENDIENTE] |
| GS | Integración Social | [PENDIENTE] |

## IDs reservados

- **FTE**: FTE-054 (catálogo BOE FP títulos)
- **NOR**: NOR-051 a NOR-058 (uno por RD de título)
- **CUR**: CUR-046 a CUR-053 (uno por ciclo)
- **TAREA**: TAREA-037 (esta tarea)

## Criterios de cierre

- Carpeta `03_curriculos/fp/` creada con subcarpetas por familia.
- FTE-054 registrada en `06_indices/fuentes.yaml`.
- 8 fichas NOR (NOR-051 a NOR-058) con datos del RD oficial (número, fecha, BOE, título exacto).
- 8 fichas CUR (CUR-046 a CUR-053) con `estado_extraccion: "pendiente"` y referencia al NOR.
- Todos los índices YAML actualizados y validados.
- Sin [PENDIENTE] en campos de identificación (número RD, fecha, BOE).

## Coordinación con trabajo paralelo

- IDs utilizados: TAREA-037, FTE-054, NOR-051–NOR-058, CUR-046–CUR-053.
- Archivos tocados: `03_curriculos/fp/` (nuevo), fichas NOR y CUR (nuevas), índices.
- No se tocan CUR-001 a CUR-045 ni TAREA-001 a TAREA-036.
