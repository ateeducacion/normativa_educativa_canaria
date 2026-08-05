---
id: TAREA-082
titulo: "Catalogar la fuente oficial del currículo de Religión en Primaria y cerrar CUR-033"
estado: "En progreso"
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

## Resultado parcial (2026-08-05)

**Fuente localizada con certeza:** Resolución de 21 de junio de 2022, de la Secretaría de Estado
de Educación, por la que se publican los currículos de las enseñanzas de religión católica
(BOE-A-2022-10452, BOE n.º 150 de 24-06-2022), dictada a propuesta de la Conferencia Episcopal
Española. Su Anexo II es el currículo de Primaria.

Catalogada como `FTE-079` y `NOR-072`. Sí procede ficha normativa: aunque el contenido lo
determina la jerarquía eclesiástica, quien la dicta y publica con eficacia jurídica es la
Secretaría de Estado, deroga expresamente los currículos anteriores y fija su entrada en vigor.

`CUR-033` se reapunta de `FTE-046` —que en realidad describe el Decreto 211/2022, no este
currículo— a `FTE-079`.

**El contenido de `CUR-033` no coincide con la fuente.** Verificado contra el Anexo II real:

- Sus seis «competencias» son paráfrasis o títulos, no el texto literal de las seis competencias
  específicas del BOE.
- Declara cuatro bloques de saberes —«El sentido de la vida», «La Biblia», «Jesús y la Iglesia»,
  «El compromiso»— frente a los **tres** reales, A, B y C, con títulos y estructura distintos.
- Registra dos criterios de evaluación por ciclo, cubriendo dos de las seis competencias, frente
  a los **doce** reales por ciclo.

No se ha corregido: es decisión editorial si se re-extrae todo desde `FTE-079` o si ese contenido
procede de otra fuente sin identificar. Queda documentado en la ficha y la tarea sigue abierta.

**Hallazgo colateral:** el RD 157/2022, de enseñanzas mínimas de Primaria, citado en el preámbulo
de esta resolución, no tiene ficha `NOR` propia en el corpus.
