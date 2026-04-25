# AGENTS.md

## 1. Propósito del repositorio

Este repositorio mantiene un corpus Markdown/YAML de normativa educativa y currículos aplicables a Canarias, preparado para consulta humana y uso por IA, sin sustituir nunca la fuente oficial.

## 2. Qué debe hacer un agente antes de modificar el repositorio

1. Leer `README.md`, `index.md`, `status.yaml` y las plantillas de `10_plantillas/`.
2. Localizar la fuente oficial y registrar la fecha de consulta.
3. Revisar los índices YAML afectados para no duplicar IDs.
4. Confirmar si la tarea requiere análisis, currículo, relación, chunk o actualización de vigencia.
5. Registrar dudas abiertas como `PREG-NNN` antes de inferir datos no confirmados.

## 3. Regla de evidencia

Todo dato normativo debe poder rastrearse hasta una fuente oficial con nombre de la norma o fuente, localización, fecha de consulta y ficha interna asociada.

### Reglas obligatorias

- R1. No se crea contenido normativo sin fuente oficial.
- R2. Todo resumen indica que no sustituye la fuente oficial.
- R3. Toda norma tiene estado de vigencia.
- R4. Toda ficha tiene fecha de consulta.
- R5. Todo análisis tiene fecha de análisis.
- R6. Toda relación normativa se registra en YAML.
- R7. Todo contenido IA-friendly debe ser breve, trazable y fiel.
- R8. No se mezclan normas con orientaciones no normativas.
- R9. No se borran normas derogadas; se marcan.
- R10. Los IDs son estables, correlativos y no se reutilizan.
- R11. Los índices YAML se actualizan con cada nueva fuente, norma, currículo o chunk.
- R12. Las dudas se registran como PREG-NNN.
- R13. Las interpretaciones se marcan con [INTERPRETACIÓN].
- R14. Las hipótesis se marcan con [HIPÓTESIS].
- R15. Los datos pendientes se marcan con [PENDIENTE].

## 4. Estructura de carpetas

- `01_fuentes/`: fichas de portales, BOE, BOC, Juriscan y otras fuentes oficiales.
- `02_normativa/`: una ficha Markdown por norma.
- `03_curriculos/`: fichas curriculares Markdown/YAML.
- `04_analisis/`: notas de análisis, comparativas y síntesis.
- `05_relaciones/`: relaciones entre normas y currículos.
- `06_indices/`: índices YAML con claves por ID.
- `07_corpus_ia/`: resúmenes, chunks y materiales para IA.
- `08_tareas/`: tareas, diario y preguntas abiertas.
- `09_decisiones-editoriales/`: decisiones editoriales del corpus.
- `10_plantillas/`: plantillas reutilizables.
- `11_calidad/`: validaciones, enlaces, vigencia e informes.

## 5. Formato Markdown

Usa frontmatter YAML, títulos con ID estable, secciones breves y trazables, y la advertencia de que el contenido no sustituye la fuente oficial.

## 6. Formato YAML

Usa claves explícitas, estados controlados, arrays para relaciones múltiples y `additionalProperties: false` en schemas. Los índices se guardan como mapas por ID, no listas anónimas.

## 7. Cómo crear una ficha de fuente

1. Asignar ID `FTE-NNN` correlativo.
2. Completar autoridad, URL oficial, tipo de fuente y fecha de consulta.
3. Describir qué contiene y su relevancia.
4. Enlazar normas o currículos relacionados.
5. Registrar la fuente en `06_indices/fuentes.yaml`.

## 8. Cómo crear una ficha normativa

1. Asignar ID `NOR-NNN` correlativo.
2. Registrar fuente principal, ámbito, tipo de norma y estado de vigencia.
3. Redactar objeto, ámbito, estructura, relaciones e impacto en Canarias.
4. Añadir resumen IA-friendly, dudas abiertas y fuentes.
5. Actualizar `06_indices/normativa.yaml` y relaciones asociadas.

## 9. Cómo crear una ficha curricular

1. Asignar ID `CUR-NNN` correlativo.
2. Registrar etapa, materia o ámbito, fuente y fecha de consulta.
3. Mantener `estado_extraccion` actualizado.
4. Separar YAML estructurado y Markdown narrativo.
5. Reflejar cualquier duda normativa en `PREG-NNN`.

## 10. Cómo crear chunks para IA

1. Crear `CHUNK-NNNNN` autocontenido y breve.
2. Indicar siempre fuente, localización y fechas.
3. No mezclar hechos con interpretación; si la hay, marcar `[INTERPRETACIÓN]`.
4. Relacionar el chunk con normas, currículos o chunks conectados.
5. Registrar el chunk en `06_indices/chunks.yaml`.

## 11. Cómo registrar relaciones

Crea un `REL-NNN` en YAML indicando tipo de relación, origen, destino, evidencia, fecha de registro y nivel de evidencia. Después actualiza `06_indices/relaciones.yaml`.

## 12. Cómo actualizar índices

Cada nueva entidad debe reflejarse inmediatamente en su índice YAML correspondiente. Los índices son la puerta de entrada del repositorio para personas y máquinas.

## 13. Cómo comprobar vigencia

Verifica siempre en fuente oficial. Si no se puede confirmar, usa `Pendiente de verificación`, documenta la limitación y abre una pregunta o tarea de seguimiento.

## 14. Cuándo cargar cada skill

- `catalogacion-fuentes`: alta o revisión de fuentes oficiales.
- `analisis-normativo`: creación y actualización de fichas `NOR`.
- `control-vigencia`: revisión de estado de vigencia.
- `relaciones-normativas`: creación y mantenimiento de `REL`.
- `analisis-curricular`: extracción curricular.
- `preparacion-corpus-ia`: resúmenes, chunks y exports.
- `control-calidad-documental`: validación de estructura y trazabilidad.
- `experto-lomloe-loe`: normativa básica estatal.
- `experto-normativa-canaria`: normativa autonómica canaria.
- `experto-eso`: currículo y ordenación de ESO.
- `experto-primaria`: Infantil y Primaria.
- `experto-bachillerato`: Bachillerato.
- `experto-formacion-profesional`: Formación Profesional.
- `perfil-docente`: revisión de claridad para profesorado.

## 15. Criterios de cierre de tarea

Una tarea solo pasa a `Hecha` si tiene fuente oficial, fecha de consulta, formato válido, entrada en índice, ID correcto, relaciones si aplica, estado de vigencia si es norma, resumen IA si corresponde, preguntas abiertas si hay dudas y registro en el diario.
