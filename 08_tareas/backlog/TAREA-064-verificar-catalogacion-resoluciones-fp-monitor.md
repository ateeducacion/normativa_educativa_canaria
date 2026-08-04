---
id: TAREA-064
titulo: "Verificar la catalogación de las tres resoluciones de FP detectadas por el monitor en TAREA-061"
estado: "Pendiente"
prioridad: "Media"
tipo: "catalogacion"
responsable: "@.agents/skills/catalogacion-fuentes"
fecha_creacion: 2026-08-05
fecha_actualizacion: 2026-08-05
relacionadas: [TAREA-061, TAREA-063]
siguiente_accion: "Identificar las tres resoluciones en el snapshot del monitor y comprobar si ya tienen ficha NOR."
---

# TAREA-064 — Verificar la catalogación de las tres resoluciones de FP del monitor

## Objetivo

`TAREA-061` dejó anotado como pendiente «completar la catalogación individual de las tres
resoluciones de FP detectadas originalmente por el monitor». Al cerrarla el 2026-08-05 no fue
posible confirmar si ese trabajo se completó por otra vía, así que se traslada aquí en lugar de
darlo por hecho.

## Contexto

- `TAREA-061` catalogó el Decreto 120/2026 (`FTE-075`, `NOR-068`, `REL-058`) y cerró el PR 29
  como duplicado del PR 28. Ese alcance sí está completo e indexado.
- `TAREA-062` catalogó la modificación de la FP semipresencial y virtual (`FTE-076`, `FTE-077`,
  `NOR-069`, `NOR-070`, `REL-059`, `REL-060`), que podría cubrir parte o la totalidad de esas
  tres resoluciones.
- El corpus tiene catalogadas resoluciones de FP de 2025 y 2026 en `NOR-061` a `NOR-070`.
- `11_calidad/monitor/portal-normativa-canaria.seen.json` solo guarda las URL ya vistas, sin
  distinguir cuáles se llegaron a catalogar, así que no sirve por sí solo para resolver la duda.

## Qué hacer

1. Localizar en el historial del PR 28 y en el diario `08_tareas/diario/2026-07-20-tarea-061-decreto-120-2026.md`
   qué tres resoluciones concretas detectó el monitor.
2. Comprobar para cada una si ya existe ficha `NOR` y entrada en `06_indices/normativa.yaml`.
3. Catalogar las que falten con la skill `catalogacion-fuentes` y `analisis-normativo`.
4. Si estaban todas catalogadas, cerrar esta tarea dejando constancia de la comprobación.

## Coordinación con trabajo paralelo

IDs consumidos: `TAREA-064`. No se reservan `FTE` ni `NOR` hasta saber cuántas fichas faltan
realmente.
