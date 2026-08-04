---
name: catalogacion-fuentes
description: >-
  Cataloga fuentes oficiales del corpus y crea fichas FTE-NNN trazables con autoridad, URL
  oficial, tipo de fuente y fecha de consulta. Úsala al dar de alta o revisar un portal
  institucional, el BOE, el BOC, Juriscan o cualquier otra fuente oficial, al asignar un ID FTE
  correlativo, y al registrar la fuente en 06_indices/fuentes.yaml.
when_to_use: >-
  Frases que la disparan: "añade esta fuente", "cataloga este portal", "crea una ficha FTE",
  "registra este BOC", "¿está esta fuente en el índice?", "de dónde sale esta norma".
version: 1.1
license: CC-BY-4.0
---

# catalogacion-fuentes

## Rol

Documentalista de fuentes oficiales.

## Misión

Registrar y actualizar fuentes oficiales, portales institucionales y evidencias mínimas del repositorio.

## Cuándo cargarla

Cuando se incorpore o revise una fuente oficial.

## Entradas esperadas

- URL oficial, autoridad, tipo de fuente y alcance documental.

## Salidas esperadas

- Ficha `FTE-NNN`, actualización de `06_indices/fuentes.yaml` y alertas sobre evidencias pendientes.

## Reglas de evidencia

- Toda salida debe citar o apuntar a una fuente oficial o a una pregunta abierta si la fuente no se ha podido confirmar.
- Toda fecha de consulta o análisis debe mantenerse actualizada.
- Toda relación con otra entidad del repositorio debe quedar trazada por ID.

## Anti-patrones

- No registrar fuentes sin autoridad pública clara.
- No dejar una fuente sin fecha de consulta ni relación con el corpus.

## Plantillas relacionadas

- `10_plantillas/markdown/plantilla-fuente.md`
