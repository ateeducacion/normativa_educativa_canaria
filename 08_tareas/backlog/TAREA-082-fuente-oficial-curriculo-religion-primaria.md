---
id: TAREA-082
titulo: "Catalogar la fuente oficial del currículo de Religión en Primaria y cerrar CUR-033"
estado: "Pendiente"
prioridad: "Media"
tipo: "catalogacion"
responsable: "@.agents/skills/catalogacion-fuentes"
fecha_creacion: 2026-08-05
fecha_actualizacion: 2026-08-05
relacionadas: [CUR-033, NOR-043, FTE-046, TAREA-067]
siguiente_accion: "Localizar en el BOE la resolución que publica el currículo de Religión Católica en Educación Primaria y catalogarla como FTE."
---

# TAREA-082 — Fuente oficial del currículo de Religión en Primaria

## Problema

`CUR-033` (Religión) es la única ficha de Primaria que no se pudo completar en `TAREA-067`, y por
una razón de fondo: **el Decreto 211/2022 no contiene su currículo**. Su disposición adicional
primera, punto 6, delega esa competencia en la jerarquía eclesiástica, y el currículo se publica
por el Ministerio en el BOE.

Hay además un incumplimiento de R1 que conviene resolver: el contenido que la ficha ya tiene
—competencias, criterios y saberes— **no está trazado a ninguna `FTE-NNN`**. Solo hay una nota
suelta, «BOE 24-06-2022», sin ficha de fuente asociada. Es decir, hay contenido normativo en el
corpus sin fuente oficial registrada.

## Qué hacer

1. Localizar en el BOE la resolución que publica el currículo del área de Religión Católica en
   Educación Primaria, previsiblemente de junio de 2022 según la nota existente.
2. Catalogarla como `FTE-NNN` conforme a `AGENTS.md` §7, y valorar si procede también una ficha
   `NOR`, dado que es una resolución de la Conferencia Episcopal publicada por el Ministerio y no
   una norma autonómica.
3. Reapuntar `CUR-033` a esa fuente y verificar contra ella el contenido que ya tiene, que hasta
   ahora nadie ha podido contrastar.
4. Decidir el `estado_extraccion` que corresponda: el marco de `DEC-0004` está pensado para el
   currículo LOMLOE autonómico y puede no encajar tal cual.

## Advertencia

Hasta que esto se resuelva, `CUR-033` debe permanecer en `parcial`. No es una ficha incompleta
por falta de trabajo, sino por falta de fuente registrada.

## Coordinación con trabajo paralelo

IDs consumidos: `TAREA-082`. Consumirá un `FTE` y posiblemente un `NOR` al ejecutarse.
