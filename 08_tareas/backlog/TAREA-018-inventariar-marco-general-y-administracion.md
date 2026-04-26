---
id: TAREA-018
titulo: "Inventariar y catalogar normativa de Marco general, Administración y Servicios complementarios"
estado: "Pendiente"
prioridad: "Media"
tipo: "analisis"
responsable: "@.agents/skills/experto-normativa-canaria"
fecha_creacion: 2026-04-26
fecha_actualizacion: 2026-04-26
relacionadas: [FTE-013]
---

# TAREA-018 — Inventariar y catalogar normativa de Marco general, Administración y Servicios complementarios

## Objetivo

Cerrar el inventario inicial del corpus revisando los apartados restantes del portal de Inspección Educativa (`FTE-013`): marco general, administración educativa, orientaciones-programas-protocolos y servicios complementarios (transporte, comedor, residencias, etc.).

## Criterios de cierre

- Inventario y fichas `NOR-NNN` para las normas vigentes en cada uno de los apartados que aún no estén cubiertos por TAREA-014, TAREA-015, TAREA-016 o TAREA-017.
- Diferenciación clara entre normativa y orientaciones/protocolos no normativos según `DEC-0005`.
- `06_indices/normativa.yaml` y relaciones actualizados.

## Notas

- Fecha de creación: 2026-04-26
- Recurso: `FTE-013` apartados `/marco_general/`, `/administracion/`, `/orientaciones_programas_protocolos/`, `/servicios_complementarios/`.
- Las orientaciones, guías y protocolos no normativos se incorporarán solo como `tipo_fuente: orientacion-no-normativa` conforme a `DEC-0005`, no como `NOR-NNN`.
