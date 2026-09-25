---
name: analisis-curricular
description: Extraer un currículo oficial a una ficha CUR-NNN. Úsalo al registrar competencias, criterios de evaluación o saberes de una etapa o materia.
version: "1.2"
license: CC-BY-4.0
---

# Análisis curricular

No se inventan competencias ni saberes. El estado de extracción refleja lo que se ha abierto, no lo que se pretende terminar.

## Qué abrir según la etapa

| Etapa o lente | Referencia |
| --- | --- |
| Infantil y Primaria | [references/primaria.md](references/primaria.md) |
| ESO | [references/eso.md](references/eso.md) |
| Bachillerato | [references/bachillerato.md](references/bachillerato.md) |
| Formación Profesional | [references/formacion-profesional.md](references/formacion-profesional.md) |
| Claridad para el profesorado | [references/perfil-docente.md](references/perfil-docente.md) |

La norma de la que cuelga el currículo se ficha con `analisis-normativo`, no aquí.

## Cierre

- ID `CUR-NNN`, etapa, materia, fuente y fecha de consulta.
- Plantillas: `10_plantillas/markdown/plantilla-curriculum.md` y `10_plantillas/yaml/plantilla-curriculum.yaml`.
- Entrada en `06_indices/curriculos.yaml`.
