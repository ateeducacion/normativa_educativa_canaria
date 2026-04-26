---
name: preparacion-corpus-ia
description: Preparar resúmenes, chunks y materiales IA-friendly.
version: 1.0
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

- `10_plantillas/markdown/plantilla-fuente.md`
- `10_plantillas/markdown/plantilla-norma.md`
- `10_plantillas/markdown/plantilla-curriculum.md`
- `10_plantillas/yaml/plantilla-relacion.yaml`
- `10_plantillas/yaml/plantilla-chunk.yaml`
