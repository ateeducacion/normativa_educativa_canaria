---
id: TAREA-085
titulo: "Verificar o retirar las tres normas que no se han localizado en fuente oficial"
estado: "Pendiente"
prioridad: "Crítica"
tipo: "control-vigencia"
responsable: "@.agents/skills/control-vigencia"
fecha_creacion: 2026-08-05
fecha_actualizacion: 2026-08-05
relacionadas: [NOR-017, NOR-018, NOR-025, NOR-026, NOR-050, FTE-053, REL-047, REL-048, PREG-010, PREG-011, PREG-012, TAREA-084]
siguiente_accion: "Empezar por NOR-050: de ella depende una derogación declarada de NOR-025 que probablemente no se ha producido."
---

# TAREA-085 — Tres fichas describen normas que no se han localizado

## Hallazgo

Al re-exportar las copias locales de `TAREA-084`, tres de ellas resistieron todos los métodos
automáticos. La causa no era la exportación: **las normas no aparecen en el BOC**.

Para descartar un fallo de la herramienta, se recorrieron uno a uno los sumarios de **todos los
boletines de los tres años implicados** —253 de 2014, 257 de 2010 y 255 de 2023, 765 en total—
buscando cualquier disposición que encajase con cada título. El resultado:

| Ficha | Lo que declara | Lo que hay en el BOC |
| --- | --- | --- |
| `NOR-017` | Orden de 28-07-2014, organización y funcionamiento de las Escuelas Infantiles de titularidad pública | Nada equivalente. Sólo dos decretos que **crean** escuelas infantiles municipales |
| `NOR-018` | Orden de 01-09-2010, desarrollo del Reglamento Orgánico de centros respecto de los IES | La Orden de esa fecha desarrolla los **EOEP**; el ROC lo desarrolla la Orden de **9 de octubre de 2013** |
| `NOR-050` | Orden de 29-05-2023, procedimientos de respuesta educativa al alumnado NEAE | Nada sobre NEAE en todo 2023 salvo un extracto de convocatoria de ayudas |

Las tres estaban registradas con `nivel_evidencia: confirmado-fuente-primaria`.

## Por qué importa más que un fichero mal exportado

Una copia local equivocada se detecta al leerla. Una ficha que describe una norma inexistente
**no se detecta nunca** desde dentro del corpus: tiene título verosímil, fechas coherentes,
fuente asignada y estado de vigencia. Y arrastra consigo lo que se construya encima.

El caso de `NOR-050` lo muestra: sostiene `REL-048`, que declara que **deroga los procedimientos
de `NOR-025`**, la Orden de 13 de diciembre de 2010. Si la orden de 2023 no existe, `NOR-025`
sigue vigente y el corpus está afirmando lo contrario. Para un corpus normativo ese es el peor
error posible: no una laguna, sino una afirmación falsa sobre qué está en vigor.

`REL-047` y `REL-048` citan además localización concreta —«artículo 1 y preámbulo»,
«disposición derogatoria única»— de un texto que nadie ha podido encontrar.

## Mitigación ya aplicada

- Las tres fichas pasan a `estado_vigencia: Pendiente de verificación` y
  `nivel_evidencia: pendiente-verificacion`, con un bloque `[PENDIENTE]` al principio del cuerpo.
- `FTE-053`, que sólo existía para dar fuente a `NOR-050`, queda marcada como catalogación
  errónea, igual que se hizo con `FTE-051` en `DEC-0010`.
- `REL-047` y `REL-048` quedan degradadas y marcadas. **`NOR-025` no se toca**: mientras no se
  demuestre la derogación, se mantiene vigente.
- `CHUNK-00014` queda marcado como no utilizable.
- Las tres copias locales llevan advertencia corregida: el problema no es de exportación.
- Registradas `PREG-010`, `PREG-011` y `PREG-012`, una por norma.

## Qué hacer

1. **`NOR-050` primero**, por lo que arrastra. Confirmar con la Consejería o en Juriscan si
   existe alguna orden de 2023 sobre procedimientos NEAE. Si no existe, retirar la ficha, la
   fuente, las dos relaciones y el chunk, y dejar constancia de que el marco vigente sigue siendo
   el del Decreto 25/2018 con la Orden de 2010 y la Resolución de 2011.
2. **`NOR-018`**: decidir si se corrige para describir la Orden de 9 de octubre de 2013
   (`BOC-A-2013-200-5076`, ya verificada) o si se retira y se cataloga esa orden con
   identificador nuevo. Valorar de paso catalogar la Orden de 1 de septiembre de 2010 sobre los
   EOEP, que es real, vigente y hoy no está en el corpus.
3. **`NOR-017`**: comprobar si el título se tomó de la ORDEN 21/2019 de la Comunitat Valenciana,
   cuyo enunciado es casi idéntico, y buscar si existe norma canaria equivalente.
4. **Revisar el resto del corpus con el mismo criterio.** Estas tres se descubrieron por
   casualidad, al fallar su re-exportación. Conviene contrastar el título de cada ficha `NOR`
   contra el sumario del boletín que declara, que es una comprobación automatizable con la
   herramienta de `TAREA-084`.

## Coordinación con trabajo paralelo

IDs consumidos: `TAREA-085`, `PREG-010`, `PREG-011`, `PREG-012`. No se han creado ni retirado
fichas `NOR`; sólo se ha degradado su nivel de evidencia.
