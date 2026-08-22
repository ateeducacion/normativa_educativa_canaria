# Interoperabilidad jurídica

## Decisión de arquitectura

El formato editorial canónico del corpus continúa siendo Markdown/YAML. Es legible, versionable y ya está validado mediante esquemas e índices. Los estándares externos se incorporarán como capas de exportación generadas, sin duplicar manualmente la información ni sustituir la fuente jurídica oficial.

## Estándares aplicables

### ELI

El [Identificador Europeo de Legislación (ELI)](https://eur-lex.europa.eu/eli-register/about.html) es la referencia prioritaria para identificar legislación y publicar metadatos interoperables. La [especificación técnica española](https://www.elidata.es/documentacion_tecnica/especificacion_tecnica.php) contempla su aplicación gradual a la legislación estatal, autonómica y local.

ELI encaja con las fichas `NOR-NNN` como capa de identificación y metadatos. No sustituye por sí solo la estructura editorial interna ni autoriza a construir una URI oficial que el organismo publicador no haya confirmado.

### Akoma Ntoso

[Akoma Ntoso 1.0](https://docs.oasis-open.org/legaldocml/akn-core/v1.0/akn-core-v1.0.html) es un estándar XML para documentos jurídicos y parlamentarios. Sería adecuado como formato de exportación cuando se necesite representar con precisión la estructura completa del texto normativo, sus bloques y referencias.

No se adopta como formato de edición principal mientras el corpus mantenga fichas de análisis y copias de consulta, en vez de una edición XML estructural completa de cada disposición.

### llms.txt

[llms.txt](https://llmstxt.org/) facilita a modelos de lenguaje un mapa Markdown breve del contenido público. Es una capa de descubrimiento, no un estándar jurídico ni una fuente de verdad. La copia de la raíz debe apuntar a documentos canónicos y mantener su inventario generado desde `06_indices/`.

## Correspondencia prevista

| Campo interno | Destino interoperable | Regla |
|---|---|---|
| Identificador `NOR-NNN` | Identificador interno | Se conserva para trazabilidad; no se presenta como cita jurídica. |
| Denominación oficial | Metadato ELI de título | Se exporta literalmente desde la ficha validada. |
| Fechas de disposición y publicación | Metadatos ELI temporales | Se exportan solo cuando constan en la fuente oficial. |
| Tipo de norma y ámbito | Tipo de recurso y jurisdicción ELI | Requiere una tabla de correspondencias explícita y versionada. |
| URL oficial | URI de referencia | Se conserva; solo se marca como URI ELI si el publicador la ofrece como tal. |
| Texto completo estructurado | Akoma Ntoso | Se genera únicamente desde una extracción estructural verificada. |

## Implantación gradual

1. Añadir a las fichas normativas un campo opcional para una URI ELI oficial verificada.
2. Definir y validar la tabla de correspondencias entre los campos internos y la ontología ELI.
3. Generar JSON-LD/RDF desde YAML, con pruebas reproducibles y sin edición duplicada.
4. Evaluar una exportación Akoma Ntoso sobre un conjunto pequeño de normas antes de ampliar el alcance.

## Salvaguardas

- No inventar identificadores ELI ni inferir que una URL oficial cumple ELI por su apariencia.
- Mantener Markdown/YAML como única fuente editorial hasta que una migración tenga cobertura, validación y reversibilidad demostradas.
- Generar las capas interoperables automáticamente y comprobar en CI que no estén desactualizadas.
- Conservar siempre el enlace a BOE, BOC o al portal institucional como referencia jurídica verificable.
