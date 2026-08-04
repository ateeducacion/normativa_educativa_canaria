---
name: preparacion-corpus-ia
description: >-
  Prepara material IA-friendly del corpus: chunks CHUNK-NNNNN autocontenidos, resúmenes breves y
  exports. Úsala al crear chunks para RAG o búsqueda semántica, al redactar resúmenes trazables,
  al mantener llms.txt y llms-full.txt, y al registrar chunks en 06_indices/chunks.yaml.
when_to_use: >-
  Frases que la disparan: "crea un chunk", "prepara esto para RAG", "resumen IA-friendly",
  "actualiza llms.txt", "material para el asistente".
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
