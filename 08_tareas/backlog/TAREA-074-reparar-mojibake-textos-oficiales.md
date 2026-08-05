---
id: TAREA-074
titulo: "Reparar el doble encodeo de las copias locales de texto oficial"
estado: "Hecha"
prioridad: "Alta"
tipo: "corpus-ia"
responsable: "@.agents/skills/preparacion-corpus-ia"
fecha_creacion: 2026-08-05
fecha_actualizacion: 2026-08-05
fecha_cierre: 2026-08-05
relacionadas: [NOR-043, NOR-047, PREG-008, TAREA-072]
---

# TAREA-074 — Reparación del doble encodeo en `07_corpus_ia/textos-completos/`

## Hallazgo

Al intentar contrastar las fichas curriculares de Primaria e Infantil contra su decreto, ninguna
competencia aparecía en el texto local. La causa no eran las fichas: **33 de las 97 copias
locales de texto oficial estaban dobles-codificadas** (UTF-8 leído como latin-1 y vuelto a
guardar como UTF-8).

El daño hacía ilegible buena parte del contenido:

- `ANEXO 1` aparecía como `ANEXOÂ 1`.
- `Competencia específica` no aparecía **ni una vez** en los textos de Primaria e Infantil,
  porque estaba escrito `Competencia especÃ­fica`.
- `Crecimiento en Armonía` era irrecuperable por búsqueda.

Los ficheros son mixtos: la cabecera que añade el proceso de exportación —con la URL oficial,
la fecha de consulta y la advertencia de R16— estaba bien codificada, y solo el cuerpo llegó
dañado. Por eso revertir el fichero entero fallaba.

## Trabajo realizado

Se añade `11_calidad/reparar_mojibake.py`, que repara únicamente los tramos que contienen la
firma del daño (`Ã` o `Â`) y solo si decodifican limpio como UTF-8. El texto sano no se toca.
Dos pasadas adicionales cubren los restos que quedan pegados a caracteres ASCII y que por eso
caen fuera de los tramos: la `Â` huérfana de un espacio duro y los indicadores ordinales
`Âº` y `Âª`.

Resultado: 33 ficheros reparados y **cero mojibake** en los 97.

Comprobación posterior: `Competencia específica` pasa de 0 a 52 apariciones en el decreto de
Primaria y de 0 a 12 en el de Infantil.

## Impacto

Estas copias son el material que alimenta la búsqueda y el RAG del corpus. Un tercio de ellas
era parcialmente inservible para búsqueda por texto sin que nada lo detectara.

## Pendiente

El validador no comprueba la codificación de las copias locales. Convendría añadir esa
comprobación para que el daño no vuelva a pasar inadvertido, y revisar el proceso de exportación
que lo introdujo.

## Coordinación con trabajo paralelo

IDs consumidos: `TAREA-074`. No se ha modificado ninguna ficha; solo copias locales de texto.
