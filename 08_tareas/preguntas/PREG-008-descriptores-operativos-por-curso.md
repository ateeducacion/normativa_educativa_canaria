---
id: PREG-008
titulo: "Los descriptores operativos varían por curso y el modelo de ficha curricular no lo representa"
estado: "Abierta"
fecha_registro: 2026-08-05
relacionadas: [CUR-001, DEC-0004, DEC-0007, TAREA-066, TAREA-067, TAREA-068, TAREA-069, TAREA-071]
---

# PREG-008 — Los descriptores operativos varían por curso

## Contexto

Al preparar la extracción de descriptores operativos (`TAREA-066` a `TAREA-069`) se comprobó
contra el texto oficial del Decreto 30/2023 (`NOR-005`) que **los descriptores operativos del
perfil de salida asociados a una competencia específica no son los mismos en todos los cursos**
en los que se imparte la materia.

Ejemplo verificado en Biología y Geología (`CUR-001`), competencia específica 2:

| Curso | Descriptores según el texto oficial |
| --- | --- |
| 1.º ESO | CCL3, CD1, CD2, CD4, CPSAA4 |
| 3.º ESO | CCL3, STEM4, CD1, CD2, CD3, CD4, CD5, CPSAA4 |
| 4.º ESO | CCL3, STEM4, CD1, CD2, CD3, CD4, CD5, CPSAA4 |

La competencia 6 de la misma materia varía en los tres cursos.

El modelo actual guarda una **lista plana por competencia**
(`elementos.competencias_especificas[].descriptores`), sin dimensión de curso. No puede
representar esta realidad.

## Consecuencia detectada en el corpus

De las 18 fichas en `estado_extraccion: completado` con descriptores volcados, **8 declaran
varios cursos**, así que su lista plana no puede ser correcta para todos ellos.

Y hay al menos un error que no es de agregación. En `CUR-001`, competencia 5, los tres cursos
coinciden en el texto oficial:

- Texto oficial (1.º, 3.º y 4.º ESO): `STEM2, STEM5, CD4, CPSAA1, CPSAA2, CC3, CC4, CE1`
- Ficha `CUR-001`: `STEM2, STEM5, CD4, CPSAA2, CC2, CC3, CC4, CE1`

La ficha pone `CC2`, que no aparece en la fuente, y omite `CPSAA1`, que sí. Comparando las seis
competencias de `CUR-001` con el texto oficial, solo la primera coincide exactamente.

Además, las 32 fichas en `parcial` **no declaran `cursos`**, así que ni siquiera se sabe a qué
curso habría que referir cada extracción.

## Qué falta decidir

1. ¿Los descriptores pasan a guardarse por curso —por ejemplo
   `descriptores: {1.º ESO: [...], 3.º ESO: [...]}`— o se separan las fichas por curso?
2. ¿Qué se hace con las 18 fichas ya marcadas `completado` cuyos descriptores no reproducen la
   fuente? ¿Se revisan todas o se degradan a `parcial` hasta revisarlas?
3. ¿Se rellena `cursos` en las 32 fichas parciales antes de extraer, dado que sin ese dato la
   extracción no es interpretable?
4. ¿Bachillerato tiene el mismo problema? Sus materias suelen impartirse en un solo curso, pero
   hay que confirmarlo antes de aplicar un criterio distinto por etapa.

## Fuente o evidencia necesaria

La evidencia está en el corpus: `07_corpus_ia/textos-completos/texto-oficial-NOR-005-decreto-30-2023.txt`
contiene los bloques competenciales por curso. No hace falta consultar fuente externa para
decidir el modelo; sí para corregir cada ficha.

## Bloqueo

`TAREA-066` a `TAREA-069` quedan bloqueadas hasta resolver esta pregunta: extraer ahora
consolidaría el mismo defecto en 32 fichas más.

Al resolverse debería registrarse como `DEC-NNNN`, previsiblemente como revisión de `DEC-0004`
y `DEC-0007`.
