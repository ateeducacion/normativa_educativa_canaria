---
id: PREG-007
titulo: "Convergencia de las dos formas de ficha curricular y del valor de etapa para FP"
estado: "Abierta"
fecha_registro: 2026-08-05
relacionadas: [TAREA-063, CUR-046, CUR-048, CUR-052]
---

# PREG-007 — Convergencia de las dos formas de ficha curricular

## Contexto

Al ejecutar por primera vez `11_calidad/validar_corpus.py` contra `schemas/curriculum.schema.yaml`
(`TAREA-063`) se comprobó que las 58 fichas curriculares en YAML siguen hoy **dos estructuras
distintas**:

- **Forma A — currículo completo** (26 fichas). Agrupa el contenido bajo `elementos`, con
  `cursos`, `url_oficial`, `fecha_consulta`, `fecha_analisis`, `estado_extraccion`,
  `estado_vigencia`, `relaciones` y `resumen_ia`.
- **Forma B — extracción por bloques** (32 fichas). Coloca `competencias_especificas`,
  `bloques_saberes` y `criterios_evaluacion` directamente en la raíz, sin `elementos` ni los
  metadatos anteriores. Las 8 fichas de FP añaden además `familia_profesional` y `grado`, y
  organizan el contenido en `modulos_profesionales` en lugar de `saberes_basicos`.

Sólo son comunes a las 58 fichas: `id`, `titulo`, `etapa`, `materia`, `norma_base`, `fuente` y
`observaciones`.

Hay además una discrepancia de vocabulario: el campo `etapa` vale `fp` en las 8 fichas de
Formación Profesional, mientras que `etapas_afectadas` de las fichas `NOR` usa
`formacion-profesional` para la misma etapa.

El esquema se ha ajustado para admitir ambas formas y ambos valores, de modo que la validación
no quede bloqueada por una decisión editorial pendiente. Es una solución provisional: mantener
dos estructuras encarece cualquier consumo automático del corpus (RAG, exports, portal).

## Qué falta confirmar

1. ¿Convergen las dos formas en una sola, o se reconocen como tipos distintos de ficha
   curricular con esquemas separados (`curriculum` y, por ejemplo, `curriculum-fp`)?
2. Si convergen, ¿cuál es la forma de destino y quién asume la migración de las otras?
3. ¿Se unifica `etapa: fp` con `formacion-profesional`, o se documenta la diferencia como
   deliberada?
4. Los metadatos que hoy sólo tiene la forma A (`fecha_consulta`, `estado_vigencia`,
   `url_oficial`) ¿pasan a ser obligatorios para toda ficha curricular? Afecta a R3 y R4.

## Fuente o evidencia necesaria

No requiere fuente oficial externa: es una decisión editorial interna del repositorio. Al
resolverse debería registrarse como `DEC-NNNN` en `09_decisiones-editoriales/` y, si implica
migración, abrir la `TAREA-NNN` correspondiente.
