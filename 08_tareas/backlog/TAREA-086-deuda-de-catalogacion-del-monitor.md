---
id: TAREA-086
titulo: "Catalogar las disposiciones que el monitor detectó y nunca se ficharon"
estado: "En progreso"
prioridad: "Alta"
tipo: "catalogacion"
responsable: "@.agents/skills/catalogacion-fuentes"
fecha_creacion: 2026-08-05
fecha_actualizacion: 2026-08-05
relacionadas: [NOR-079, NOR-080, NOR-081, NOR-082, NOR-083, NOR-084, NOR-085, NOR-086, FTE-086, FTE-087, FTE-088, FTE-089, FTE-090, FTE-091, FTE-092, FTE-093, TAREA-064, TAREA-084, PREG-006]
siguiente_accion: "Catalogar las siete resoluciones de 25 de febrero de 2026 sobre distribución horaria de los Grados C y B, que forman un conjunto coherente por familia profesional."
---

# TAREA-086 — La deuda silenciosa del monitor

## El problema de diseño

El monitor del portal de normativa guarda un snapshot de URL vistas para no repetir avisos. Es lo
que se quiere, pero tiene un efecto secundario que nadie había mirado: **una disposición
detectada y nunca catalogada desaparece del radar para siempre**. No vuelve a aparecer en ningún
informe.

Al cruzar el snapshot contra el corpus aparecieron **58 URL sin rastro**, vistas desde mayo de
2026. Entre ellas, el Real Decreto 659/2023, que cuatro fichas del corpus citaban sin poder
enlazar.

Había además un fallo de comparación: el monitor contrastaba **URL contra URL**, y la misma
disposición se publica como PDF de la sede, como HTML del boletín y como texto consolidado. Una
norma ya catalogada bajo una de esas formas se contaba como pendiente bajo otra.

## Qué se ha corregido en la herramienta

- El escaneo compara ahora por **identificador oficial** —`BOC-A-AAAA-NNN-NNNN`,
  `BOE-A-AAAA-NNNNN`— además de por URL.
- Nuevo modo `python3 11_calidad/monitor/scan_normativa.py --pendientes`: lista las URL del
  snapshot que siguen sin rastro, clasificadas en disposiciones del BOC, del BOE, PDF de la
  Consejería y páginas de portal. Devuelve código 1 si queda alguna disposición sin catalogar.

De las 58, **23 son páginas de portal** —índices de navegación de la normativa clasificada—, que
no son normas y no requieren ficha. La deuda real eran 35.

## Lo catalogado

Ocho normas, elegidas por ser las que otras fichas del corpus citaban sin poder enlazar:

| Ficha | Norma | Por qué |
| --- | --- | --- |
| `NOR-079` | RD 157/2022, enseñanzas mínimas de Primaria | La desarrolla `NOR-043`; apareció como pendiente en `TAREA-082` |
| `NOR-080` | RD 659/2023, ordenación del Sistema de FP | La citaban `NOR-073`, `NOR-074`, `NOR-078` y las resoluciones canarias |
| `NOR-081` | Resolución 30-10-2024, Grados D y E | Resolución base del marco de FP canario, citada por tres fichas |
| `NOR-082` | Resolución 29-11-2024 | Modifica la anterior; sin ella `NOR-081` quedaba desactualizada |
| `NOR-083` | Resolución 26-03-2026 | Amplía `NOR-081` con un ciclo y seis cursos de especialización |
| `NOR-084` | Resolución 17-04-2026 | Corrige la omisión del Anexo III en la anterior |
| `NOR-085` | Resolución 26-11-2025, dobles titulaciones | Es la que modifica `NOR-075`, que no podía enlazarla |
| `NOR-086` | Resolución 02-05-2025, primer curso en común | Antecedente citado por `NOR-085` |

Con sus fuentes `FTE-086` a `FTE-093` y copia local de cada una extraída del PDF firmado.

Y once relaciones, `REL-064` a `REL-074`, que cierran la cadena: qué desarrolla qué, qué modifica
qué y qué corrige qué. Antes había fichas que **declaraban en su texto** una modificación cuyo
destino no existía en el corpus.

## Lo que queda

### Disposiciones identificadas, pendientes de catalogar

Las siete resoluciones de **25 de febrero de 2026** sobre distribución horaria y estructura
modular de los **Grados C (Certificados Profesionales) y sus Grados B (Certificados de
Competencia)**, repartidas por familia profesional entre dos boletines:

| CVE | Familias profesionales |
| --- | --- |
| `BOC-A-2026-045-733` | Actividades Físicas y Deportivas; Comercio y Marketing; Marítimo-Pesquera |
| `BOC-A-2026-045-734` | Administración y Gestión; Agraria; Informática y Comunicaciones |
| `BOC-A-2026-045-735` | Artes Gráficas; Fabricación Mecánica; Servicios Socioculturales |
| `BOC-A-2026-045-736` | Edificación y Obra Civil; Electricidad y Electrónica; Energía |
| `BOC-A-2026-046-748` | Hostelería y Turismo |
| `BOC-A-2026-046-749` | Imagen Personal; Imagen y Sonido; Instalación y Mantenimiento |
| `BOC-A-2026-046-750` | Industrias Alimentarias; Seguridad y Medio Ambiente; Textil |

Forman un conjunto coherente y conviene catalogarlas juntas. Cubren los Grados C y B, que el
corpus no tiene representados: hoy sólo están los Grados D y E.

Además, `BOC-A-2022-087-1481`, Resolución de 21 de abril de 2022 sobre organización del Curso
Específico de acceso a ciclos de grado medio, y `BOC-A-2024-230-3794`, Resolución de 5 de
noviembre de 2024 sobre formación dual.

### Disposiciones del BOE identificadas

- `BOE-A-2024-14079` — RD 658/2024, que **modifica el RD 659/2023** ya catalogado como `NOR-080`.
  Es la más prioritaria: sin ella, `NOR-080` no refleja su redacción vigente.
- `BOE-A-2025-2039` — RD 69/2025, elementos e instrumentos de gestión del Sistema Nacional de FP.
- `BOE-A-2020-17274` y su corrección `BOE-A-2021-979` — RD 1085/2020, convalidaciones de módulos.
- `BOE-A-2022-1274` — RD 62/2022, flexibilización de requisitos para certificados de
  profesionalidad.
- `BOE-A-2021-18189` — Orden EFP/1210/2021, equivalencias de estudios para acceso a FP.

### PDF de la Consejería

Nueve documentos de normativa interna —instrucciones de coordinación de familias profesionales,
estructura modular y horaria de los Grados D y E, admisión a cursos de especialización, oferta
bilingüe—. Requieren decidir antes si son normativa o instrucciones internas: `R8` prohíbe
mezclar normas con orientaciones no normativas.

### Resoluciones citadas por fichas del corpus y aún sin catalogar

- Resolución de **27 de enero de 2026**, que modifica `NOR-085` y otra resolución. La citan
  `NOR-074` y `NOR-075`.
- Resolución de **25 de abril de 2025** y de **21 de febrero de 2025**, sobre FP Adaptada. Las
  citan `NOR-074` y `NOR-083`.
- Resolución de **9 de julio de 2025**, cursos de acceso directo del curso 2025-2026, antecedente
  de `NOR-073`.

## Coordinación con trabajo paralelo

IDs consumidos: `TAREA-086`, `FTE-086` a `FTE-093`, `NOR-079` a `NOR-086`, `REL-064` a `REL-074`.
