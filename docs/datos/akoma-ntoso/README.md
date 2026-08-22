# Pilotos Akoma Ntoso

Los XML de este directorio son exportaciones técnicas y reproducibles de artículos delimitados de normas educativas. Su finalidad es probar la estructura, los identificadores FRBR y, cuando existe, la trazabilidad ELI.

El catálogo revisado vive en `11_calidad/akoma_ntoso_pilotos.yaml`. El generador `11_calidad/generar_interoperabilidad.py` es la única vía de edición de estos XML.

## Alcance y garantías

- Cada fichero incluye un artículo concreto; no representa el texto completo ni una consolidación jurídica.
- El contenido se contrasta con la copia local de consulta o con la publicación oficial citada en el catálogo de pilotos.
- Se ha validado localmente contra el XSD oficial de [Akoma Ntoso 3.0 / OASIS LegalDocML 1.0](https://docs.oasis-open.org/legaldocml/akn-core/v1.0/os/part2-specs/schemas/akomantoso30.xsd).
- No sustituyen al BOE ni al BOC, no son publicación oficial y no deben utilizarse como fuente jurídica autónoma.
- La URI ELI solo aparece como `FRBRalias` cuando la ficha normativa tiene `uri_eli` confirmada por el publicador.

## Cobertura actual

| Fichero | Norma | Artículos | Publicador |
|---|---|---|---|
| `NOR-003-articulo-1.xml`, `NOR-003-articulo-2.xml` | RD 217/2022 (ESO) | 1 y 2 | BOE |
| `NOR-004-articulo-1.xml`, `NOR-004-articulo-2.xml` | Ley 6/2014 | 1 y 2 | BOE |
| `NOR-005-articulo-1.xml`, `NOR-005-articulo-2.xml` | Decreto 30/2023 | 1 y 2 | BOC |
| `NOR-006-articulo-1.xml`, `NOR-006-articulo-2.xml` | RD 243/2022 (Bachillerato) | 1 y 2 | BOE |
| `NOR-007-articulo-1.xml` | Ley Orgánica 3/2022 (FP) | 1 | BOE |
| `NOR-043-articulo-1.xml`, `NOR-043-articulo-2.xml` | Decreto 211/2022 (Primaria) | 1 y 2 | BOC |
| `NOR-047-articulo-1.xml`, `NOR-047-articulo-2.xml` | Decreto 196/2022 (Infantil) | 1 y 2 | BOC |
| `NOR-079-articulo-1.xml`, `NOR-079-articulo-2.xml` | RD 157/2022 (Primaria) | 1 y 2 | BOE |
| `NOR-080-articulo-1.xml`, `NOR-080-articulo-2.xml` | RD 659/2023 (ordenación FP) | 1 y 2 | BOE |

La ampliación a más artículos requiere segmentación estructural, revisión humana de cada bloque y validación XSD; no debe inferirse automáticamente a partir de saltos de línea del texto plano.
