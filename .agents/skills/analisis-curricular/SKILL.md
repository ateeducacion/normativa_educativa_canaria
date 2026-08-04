---
name: analisis-curricular
description: >-
  Extrae currículos oficiales a fichas CUR-NNN en Markdown y YAML, manteniendo estado_extraccion
  y la relación con la norma base. Úsala al extraer competencias específicas, criterios de
  evaluación o saberes básicos de una etapa o materia, y al registrar el currículo en
  06_indices/curriculos.yaml.
when_to_use: >-
  Frases que la disparan: "extrae el currículo de", "competencias específicas de", "criterios de
  evaluación de", "saberes básicos", "añade la materia X de ESO o Bachillerato".
version: 1.1
license: CC-BY-4.0
---

# analisis-curricular

## Rol

Analista curricular LOMLOE.

## Misión

Crear fichas curriculares trazables con estado de extracción y relación con la norma base.

## Cuándo cargarla

Cuando se localice un currículo oficial o una actualización curricular.

## Entradas esperadas

- Fuente oficial, etapa, materia o ámbito, norma base y alcance de extracción.

## Salidas esperadas

- Fichas `CUR-NNN`, actualización del índice curricular y notas sobre pendientes.

## Reglas de evidencia

- Toda salida debe citar o apuntar a una fuente oficial o a una pregunta abierta si la fuente no se ha podido confirmar.
- Toda fecha de consulta o análisis debe mantenerse actualizada.
- Toda relación con otra entidad del repositorio debe quedar trazada por ID.

## Anti-patrones

- No inventar competencias o saberes.
- No cerrar la extracción sin reflejar su estado real.

## Plantillas relacionadas

- `10_plantillas/markdown/plantilla-curriculum.md`
- `10_plantillas/yaml/plantilla-curriculum.yaml`
