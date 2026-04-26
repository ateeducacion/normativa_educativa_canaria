---
id: TAREA-017
titulo: "Inventariar y catalogar normativa de Formación Profesional en Canarias"
estado: "En progreso"
prioridad: "Alta"
tipo: "analisis"
responsable: "@.agents/skills/experto-formacion-profesional"
fecha_creacion: 2026-04-26
fecha_actualizacion: 2026-04-26
relacionadas: [FTE-014, FTE-015, FTE-016, NOR-002, NOR-007, NOR-008, REL-008, TAREA-020]
---

# TAREA-017 — Inventariar y catalogar normativa de Formación Profesional en Canarias

## Objetivo

Construir el bloque del corpus dedicado a Formación Profesional (FP) catalogando primero la **Ley Orgánica 3/2022, de 31 de marzo, de ordenación e integración de la FP** y los reales decretos de los títulos vigentes; y a continuación los decretos autonómicos y resoluciones canarias asociadas.

## Criterios de cierre

- Ficha `NOR-NNN` para la Ley Orgánica 3/2022 de FP creada y enlazada a `FTE-XXX` BOE.
- Lista de reales decretos de títulos de FP relevantes para Canarias inventariada.
- Decretos y órdenes autonómicas de desarrollo de FP en Canarias catalogados como `NOR-NNN`.
- `06_indices/normativa.yaml` y relaciones actualizados.

## Notas

- Fecha de creación: 2026-04-26
- Recurso: `FTE-014` (Enseñanzas) y `FTE-015` (FP).
- La FP combina norma básica estatal (Ley Orgánica 3/2022) con desarrollos autonómicos: la trazabilidad debe mantener la cita doble (estatal + autonómica) cuando proceda.

## Avance — 2026-04-26

- Catalogada la fuente oficial estatal: `FTE-016` (BOE-A-2022-5139, texto consolidado de la LO 3/2022).
- Creada la ficha estatal `NOR-007` (LOFP) con datos verificados (BOE n.º 78, 1-04-2022; entrada en vigor 21-04-2022; deroga LO 5/2002).
- Creada la ficha autonómica `NOR-008` (Decreto 156/1996 de FP Específica en Canarias) con `estado_vigencia: Pendiente de verificación` conforme a `DEC-0003`, dado que es pre-LOMLOE/LOFP.
- Registrada la relación `REL-008` (NOR-007 relaciona NOR-002 / LOMLOE).
- Pendiente de cerrar: órdenes y resoluciones canarias de FP listadas en `FTE-015` y verificación de vigencia del Decreto 156/1996. Continuación en `TAREA-020`.
