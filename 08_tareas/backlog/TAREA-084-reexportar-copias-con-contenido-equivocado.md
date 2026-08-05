---
id: TAREA-084
titulo: "Re-exportar las trece copias locales que contienen una norma distinta de la que declaran"
estado: "Pendiente"
prioridad: "Crítica"
tipo: "corpus-ia"
responsable: "@.agents/skills/preparacion-corpus-ia"
fecha_creacion: 2026-08-05
fecha_actualizacion: 2026-08-05
relacionadas: [NOR-044, NOR-028, NOR-050, NOR-060, TAREA-074, TAREA-077, TAREA-081]
siguiente_accion: "Re-exportar NOR-044 desde su PDF oficial: es la norma de evaluación más citada del corpus."
---

# TAREA-084 — Copias locales con contenido equivocado

## Hallazgo

Al revisar los 96 textos locales buscando anexos ausentes apareció un problema **más grave que
el que se buscaba**: trece copias no contienen la norma que declaran. Su cabecera R16 es
correcta —título y URL— pero el cuerpo es **otra disposición por completo**.

El patrón apunta a que la exportación original tomó el ítem equivocado del sumario del boletín,
probablemente `001.html` en vez del anuncio concreto.

Nada lo detectaba: los ficheros están bien codificados, tienen su cabecera y su tamaño es
plausible. Quien los usara para citar o para RAG estaría citando otra norma.

## Los trece

| Ficha | Debería contener | Contiene realmente |
| --- | --- | --- |
| `NOR-044` | Orden 31-05-2023, evaluación y promoción | Resolución del Hospital Ntra. Sra. de Candelaria sobre carrera profesional sanitaria |
| `NOR-050` | Orden 29-05-2023, procedimientos NEAE | Orden de subvenciones por las erupciones volcánicas de La Palma |
| `NOR-012` | Decreto 112/2011, ROC de los CIFP | Decreto 97/2011, Plan Insular de Ordenación de La Gomera |
| `NOR-013` | Orden 22-05-2011, Inspección | Decreto 131/2011 sobre intensidades de protección de la dependencia |
| `NOR-011` | Decreto 52/2009, Reglamento de la Inspección | Corrección de errores del Decreto 35/2009 sobre la RPT de Economía |
| `NOR-017` | Orden 28-07-2014, escuelas infantiles | Resolución de subvenciones a Cofradías de Pescadores |
| `NOR-018` | Orden 1-09-2010, desarrollo del ROC en IES | Resolución de la Academia Canaria de Seguridad |
| `NOR-034` | Orden 24-04-2009, comedores escolares | Ley 3/2009 de la Agencia Canaria de Desarrollo Sostenible |
| `NOR-035` | Orden 2-08-2006, transporte escolar | Resolución de 1-08-2006 sobre período vacacional y permisos |
| `NOR-023` | Resolución 16-06-2020, permisos y licencias | Resolución de convalidación del Decreto ley 9/2020 (COVID-19) |
| `NOR-019` | Ley 2/1987, Función Pública Canaria | Resolución de 1987 de la Diputación Provincial de Almería |
| `NOR-060` | RD 1074/2012, Técnico Superior en Integración Social | Resolución de la Universidad Carlos III sobre un máster |
| `NOR-028` | Orden 10-02-2016, aulas enclave | Cáscara del BOC: faltan íntegros los anexos, que **son** la norma (116 páginas) |

**`NOR-044` es prioridad máxima**: es la norma de evaluación más citada del corpus.

## Mitigación aplicada

Las trece copias llevan ya una línea `ADVERTENCIA DE CONTENIDO` en su cabecera que dice qué
contienen realmente y que no deben usarse para cita ni búsqueda. El validador las reporta como
aviso mientras esa marca esté presente, y como **error** si falta: así una contaminación nueva no
pasaría inadvertida.

## Qué hacer

Para cada una, el procedimiento probado de `TAREA-077` y `TAREA-081`:

1. Localizar el PDF del anuncio concreto en el BOC o el BOE, **no** el sumario del día.
2. Extraer con `pdftotext -layout` y comprobar que el cuerpo corresponde al título.
3. Sustituir la copia conservando la cabecera R16, actualizando URL y fechas, y **retirando la
   línea de advertencia de contenido**.
4. Registrar la nueva procedencia en `06_indices/textos-oficiales.yaml`.
5. Validar: el fichero debe desaparecer de los avisos de `CORRESPONDENCIA`.

## Anexos accesorios ausentes

Seis copias más tienen ausente un anexo de carácter accesorio —formularios, modelos de acta— con
el articulado completo: `NOR-025`, `NOR-015`, `NOR-014`, `NOR-026`, `NOR-016` y `NOR-037`. No
comprometen la cita del articulado y quedan como trabajo de menor prioridad dentro de esta tarea.

## Coordinación con trabajo paralelo

IDs consumidos: `TAREA-084`. Solo se modifican copias locales de texto y su índice.
