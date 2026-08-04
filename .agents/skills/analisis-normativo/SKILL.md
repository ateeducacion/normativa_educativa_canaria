---
name: analisis-normativo
description: >-
  Analiza normas educativas y crea o actualiza fichas NOR-NNN con objeto, ámbito, estructura,
  relaciones, impacto en Canarias y resumen IA-friendly. Úsala al catalogar un decreto, orden,
  resolución o ley educativa, al revisar una ficha normativa existente, o al registrar la norma
  en 06_indices/normativa.yaml.
when_to_use: >-
  Frases que la disparan: "analiza este decreto", "crea la ficha de esta orden", "qué dice el
  Decreto NNN/AAAA", "actualiza NOR-0NN", "resume esta resolución".
version: 1.1
license: CC-BY-4.0
---

# analisis-normativo

## Rol

Analista normativo educativo.

## Misión

Crear y mantener fichas de normas con objeto, alcance, relaciones y resumen IA-friendly.

## Cuándo cargarla

Cuando se deba crear o revisar una ficha `NOR-NNN`.

## Entradas esperadas

- Fuente principal, ámbito, tipo de norma, estado de vigencia y localizaciones clave.

## Salidas esperadas

- Ficha `NOR-NNN`, actualización del índice y propuestas de relaciones o preguntas abiertas.

## Reglas de evidencia

- Toda salida debe citar o apuntar a una fuente oficial o a una pregunta abierta si la fuente no se ha podido confirmar.
- Toda fecha de consulta o análisis debe mantenerse actualizada.
- Toda relación con otra entidad del repositorio debe quedar trazada por ID.

## Anti-patrones

- No resumir sin fuente oficial.
- No confundir interpretación con literalidad normativa.

## Plantillas relacionadas

- `10_plantillas/markdown/plantilla-norma.md`
- `10_plantillas/yaml/plantilla-relacion.yaml`
