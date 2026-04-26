---
name: analisis-curricular
description: Extraer y resumir currículos oficiales en formatos Markdown y YAML.
version: 1.0
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

- `10_plantillas/markdown/plantilla-fuente.md`
- `10_plantillas/markdown/plantilla-norma.md`
- `10_plantillas/markdown/plantilla-curriculum.md`
- `10_plantillas/yaml/plantilla-relacion.yaml`
- `10_plantillas/yaml/plantilla-chunk.yaml`
