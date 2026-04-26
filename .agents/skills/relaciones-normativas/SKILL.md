---
name: relaciones-normativas
description: Crear relaciones REL entre normas y currículos con evidencia.
version: 1.0
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

- `10_plantillas/markdown/plantilla-fuente.md`
- `10_plantillas/markdown/plantilla-norma.md`
- `10_plantillas/markdown/plantilla-curriculum.md`
- `10_plantillas/yaml/plantilla-relacion.yaml`
- `10_plantillas/yaml/plantilla-chunk.yaml`
