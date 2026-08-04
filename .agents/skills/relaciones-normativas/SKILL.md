---
name: relaciones-normativas
description: >-
  Registra relaciones entre normas y currículos como REL-NNN en YAML, con tipo de relación,
  origen, destino, evidencia y nivel de evidencia. Úsala cuando una norma derogue, modifique,
  desarrolle o sustituya a otra, al cruzar una norma con un currículo, y al actualizar
  06_indices/relaciones.yaml.
when_to_use: >-
  Frases que la disparan: "esta norma deroga a", "relaciona NOR-0NN con", "qué modifica", "crea
  la relación", "desarrolla el decreto".
version: 1.1
license: CC-BY-4.0
---

# relaciones-normativas

## Rol

Cartógrafo de relaciones normativas.

## Misión

Registrar relaciones explícitas entre normas, currículos y efectos documentales.

## Cuándo cargarla

Cuando exista modificación, desarrollo, derogación o conexión relevante entre entidades.

## Entradas esperadas

- IDs de origen y destino, tipo de relación, fuente y localización.

## Salidas esperadas

- Archivo `REL-NNN`, índice actualizado y referencias cruzadas en fichas relacionadas.

## Reglas de evidencia

- Toda salida debe citar o apuntar a una fuente oficial o a una pregunta abierta si la fuente no se ha podido confirmar.
- Toda fecha de consulta o análisis debe mantenerse actualizada.
- Toda relación con otra entidad del repositorio debe quedar trazada por ID.

## Anti-patrones

- No registrar relaciones vagas.
- No omitir la evidencia o localización.

## Plantillas relacionadas

- `10_plantillas/yaml/plantilla-relacion.yaml`
