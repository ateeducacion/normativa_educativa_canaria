---
id: TAREA-079
titulo: "Sustituir por el enunciado literal las competencias de las fichas curriculares de Infantil"
estado: "Pendiente"
prioridad: "Media"
tipo: "curriculo"
responsable: "@.agents/skills/analisis-curricular"
fecha_creacion: 2026-08-05
fecha_actualizacion: 2026-08-05
relacionadas: [DEC-0008, DEC-0009, CUR-034, CUR-035, CUR-036, NOR-047, TAREA-069]
siguiente_accion: "Localizar en el Decreto 196/2022 el enunciado literal de las 11 competencias y sustituir descripcion por enunciado_oficial."
---

# TAREA-079 — Literalidad de los enunciados de Infantil

## Contexto

`DEC-0009` estableció que los descriptores operativos no aplican a Educación Infantil, así que
`TAREA-069` se cerró por no proceder. Pero las tres fichas siguen en `estado_extraccion: parcial`
por un motivo distinto: **sus enunciados no son literales**.

Comprobado: 0 de las 11 competencias de `CUR-034`, `CUR-035` y `CUR-036` reproducen el texto del
Decreto 196/2022. Sus competencias siguen usando las claves `id` y `descripcion`, con un resumen,
en lugar de `codigo` y `enunciado_oficial` con la redacción oficial, como fija `DEC-0008`.

El decreto sí contiene las competencias: 12 apariciones de «Competencia específica» tras reparar
la codificación del fichero en `TAREA-074`.

## Qué hacer

1. Localizar en `07_corpus_ia/textos-completos/texto-oficial-NOR-047-decreto-196-2022-infantil.txt`
   el enunciado de cada competencia específica por área.
2. Sustituir `descripcion` por `enunciado_oficial` con el texto literal, y renombrar `id` a
   `codigo`.
3. Comprobar que los criterios de evaluación y los saberes básicos son también literales.
4. Con los tres elementos aplicables completos y literales, pasar las fichas a
   `estado_extraccion: "completado"` conforme a `DEC-0009`, y realinear
   `06_indices/curriculos.yaml`.

## Advertencia

El decreto describe cada competencia en prosa explicativa —«En esta competencia específica, el
conocimiento…»— antes de enunciarla. Hay que copiar **el enunciado**, no la explicación.

## Coordinación con trabajo paralelo

IDs consumidos: `TAREA-079`. Solo se modifican `CUR-034`, `CUR-035` y `CUR-036`.
