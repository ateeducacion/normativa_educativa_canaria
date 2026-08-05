---
id: PREG-009
titulo: "FTE-051 declara una resolución que no existe como norma diferenciada"
estado: "Abierta"
fecha_registro: 2026-08-05
relacionadas: [FTE-049, FTE-051, NOR-046, NOR-049, TAREA-070, TAREA-076]
---

# PREG-009 — Identidad de FTE-051

## Contexto

`FTE-051` declara una «Resolución de 20 de junio de 2025, IOF Escuelas Infantiles». `TAREA-070`
la buscó en el portal oficial y concluye, con evidencia primaria, que **ese documento no existe
como norma diferenciada**.

La única resolución de 20 de junio de 2025 es la **Resolución conjunta n.º 73/2025** de
instrucciones de organización y funcionamiento para el curso 2025-2026, ya catalogada como
`FTE-049`. Su sello de registro electrónico dice literalmente «RESOLUCION - Nº: 73 / 2025 -
Tomo: 1 - Libro: 613 - Fecha: 20/06/2025 08:40:38», y la cadena «escuelas infantiles» no aparece
ni una vez en sus más de 2.800 líneas.

Esa resolución remite expresamente fuera de sí misma para el primer ciclo de Infantil: su Anexo
II punto 2 dice que los centros autorizados «deberán atender a las instrucciones específicas que
se dicten al efecto». Esas instrucciones son la **Resolución Conjunta n.º 24/2024, de 16 de
julio** (sello verificado: «RESOLUCION - Nº: 24 / 2024 - Tomo: 1 - Libro: 2739 - Fecha:
16/07/2024»), que sigue vigente y **no** es equivalente a lo que declara `FTE-051`: otra fecha,
otro número y otro órgano —Direcciones Generales, no Viceconsejería—.

## Comprobado sin resultado

1. Página de instrucciones de organización y funcionamiento de la Inspección: solo aparecen la
   73/2025 (25-26), la de 26-27, su modificatoria de 17/07/2026 y la 24/2024 de Infantil.
2. Página de normativa clasificada de Educación Infantil: la más reciente es la 24/2024, sin
   sustituta de 2025 ni 2026.
3. Portal «Centros de Educación Infantil».
4. «Instrucciones y procedimientos para Infantil, Primaria, ESO y Bachillerato».
5. Buscador de normativa de la Consejería filtrado por 2025 e «infantil»: solo devuelve una orden
   de subvenciones a escuelas infantiles municipales, ajena al objeto.
6. Búsquedas en el BOC, incluida la comprobación del cambio de numeración anual.

## Hipótesis

`FTE-051` parece un **desdoblamiento por etapas** de la única resolución 73/2025. Es el mismo
patrón que se observa en `NOR-046` («IOF Primaria 25-26») y `NOR-049` («IOF Infantil 25-26»), que
comparten `fecha_disposicion: 2025-06-20` y cuyo cuerpo, en el caso de `NOR-049`, ya dice
«Resolución conjunta n.º 73/2025, de 20 de junio». [HIPÓTESIS]

## Qué falta decidir

Las tres salidas razonables, ninguna aplicada porque todas cambian la identidad de una fuente y
afectan a fichas de otras tareas:

1. **Fusionar `FTE-051` en `FTE-049`** y reapuntar `NOR-049` a `FTE-049`, ajustando el título a
   la realidad. Consecuencia: hay que decidir qué se hace con el ID `FTE-051`, que por R10 no se
   reutiliza.
2. **Reidentificar `FTE-051`** como la Resolución Conjunta n.º 24/2024, de 16 de julio,
   corrigiendo título, fecha y autoridad. Deja de ser «de 20 de junio de 2025».
3. **Mantenerla en `Pendiente de verificación`** con esta pregunta abierta como constancia.

Conviene revisar de paso si `NOR-046` y `NOR-049` sufren el mismo desdoblamiento.

## Fuente o evidencia necesaria

Ninguna adicional: la evidencia primaria ya está recogida. Es decisión editorial.
