---
name: preparacion-corpus-ia
description: Crear un resumen, un chunk o un texto rápido. Úsalo al preparar material en 07_corpus_ia.
version: 1.1
license: CC-BY-4.0
---

# preparacion-corpus-ia

## Rol

Diseñador de corpus para IA.

## Misión

Transformar fichas documentales en resúmenes y chunks breves, fieles y trazables.

## Cuándo cargarla

Cuando se necesite soporte para RAG, búsqueda semántica o FAQ.

## Entradas esperadas

- Ficha origen, objetivo del chunk y uso previsto.

## Salidas esperadas

- Resúmenes IA, `CHUNK-NNNNN`, índices y vínculos con entidades fuente.

## Reglas de evidencia

- Toda salida debe citar o apuntar a una fuente oficial o a una pregunta abierta si la fuente no se ha podido confirmar.
- Toda fecha de consulta o análisis debe mantenerse actualizada.
- Toda relación con otra entidad del repositorio debe quedar trazada por ID.

## Anti-patrones

- No crear chunks largos ni ambiguos.
- No mezclar hechos con interpretación sin marcarla.

## Plantillas relacionadas

- `10_plantillas/yaml/plantilla-chunk.yaml`
