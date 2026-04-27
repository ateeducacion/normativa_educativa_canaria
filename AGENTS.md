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
- R16. Toda copia local de texto completo debe indicar URL oficial, fecha de consulta, fecha de exportación y advertencia de que no sustituye la fuente oficial.

## 4. Estructura de carpetas

- `01_fuentes/`: fichas de portales, BOE, BOC, Juriscan y otras fuentes oficiales.
- `02_normativa/`: una ficha Markdown por norma.
- `03_curriculos/`: fichas curriculares Markdown/YAML.
- `04_analisis/`: notas de análisis, comparativas y síntesis.
- `05_relaciones/`: relaciones entre normas y currículos.
- `06_indices/`: índices YAML con claves por ID.
- `07_corpus_ia/`: resúmenes, chunks, textos completos rápidos y materiales para IA.
- `08_tareas/`: tareas, diario y preguntas abiertas.
- `09_decisiones-editoriales/`: decisiones editoriales del corpus.
- `10_plantillas/`: plantillas reutilizables.
- `11_calidad/`: validaciones, enlaces, vigencia e informes.

## 5. Formato Markdown

Usa frontmatter YAML, títulos con ID estable, secciones breves y trazables, y la advertencia de que el contenido no sustituye la fuente oficial.

### 5.1 Frontmatter YAML — formato obligatorio

- Las claves de primer nivel del frontmatter empiezan **en la columna 0**, sin sangría inicial. No uses 4 espacios ni tabuladores delante de `id:`, `titulo:`, etc.
- Los bloques anidados (por ejemplo `relaciones:` en una ficha normativa) usan **dos espacios** de indentación para sus claves hijas, y todas comparten el mismo nivel.
- Los delimitadores `---` van también en la columna 0, sin sangría. El delimitador de cierre debe coincidir con el de apertura.
- El cuerpo Markdown que sigue al frontmatter **no debe llevar sangría inicial**: encabezados, párrafos y tablas comienzan en la columna 0.
- Antes de subir cambios, valida que `yaml.safe_load` parsea el frontmatter sin errores.
- Cuando crees nuevas fichas, parte siempre de la plantilla correspondiente en `10_plantillas/markdown/` o `10_plantillas/yaml/`. Si encuentras una ficha existente que no cumpla esta regla (por ejemplo con sangría heredada), normalízala junto con tu cambio o abre una `TAREA-NNN` específica.

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

## 10 bis. Cómo registrar un texto oficial rápido

1. Crear la copia local solo cuando aporte valor real para lectura rápida, RAG o extracción.
2. Mantener siempre la URL oficial, la fecha de consulta y la fecha de exportación.
3. Añadir advertencia expresa de que la copia local no sustituye la fuente oficial.
4. Registrar la ruta local y su acceso oficial en `06_indices/textos-oficiales.yaml`.
5. No usar la copia local como prueba única si la fuente oficial ofrece una versión más reciente o consolidada.

## 11. Cómo registrar relaciones

Crea un `REL-NNN` en YAML indicando tipo de relación, origen, destino, evidencia, fecha de registro y nivel de evidencia. Después actualiza `06_indices/relaciones.yaml`.

## 12. Cómo actualizar índices

Cada nueva entidad debe reflejarse inmediatamente en su índice YAML correspondiente. Los índices son la puerta de entrada del repositorio para personas y máquinas. Si se crea o actualiza una copia local rápida del texto completo, también debe actualizarse `06_indices/textos-oficiales.yaml`.

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
- `experto-normativa-canaria`: normativa autonómica Canaria.
- `experto-eso`: currículo y ordenación de ESO.
- `experto-primaria`: Infantil y Primaria.
- `experto-bachillerato`: Bachillerato.
- `experto-formacion-profesional`: Formación Profesional.
- `perfil-docente`: revisión de claridad para profesorado.

## 15. Criterios de cierre de tarea

Una tarea solo pasa a `Hecha` si tiene fuente oficial, fecha de consulta, formato válido, entrada en índice, ID correcto, relaciones si aplica, estado de vigencia si es norma, resumen IA si corresponde, preguntas abiertas si hay dudas y registro en el diario.

## 16. Trabajo en paralelo (varios agentes a la vez)

Asume siempre que **otra IA u otra persona puede estar trabajando en el repositorio al mismo tiempo**. Sigue este procedimiento para evitar pisarte con su trabajo y para no romper la regla R10 (IDs estables y no reutilizables).

### 16.1 Antes de empezar (pre-flight obligatorio)

1. `git fetch origin main && git pull --rebase origin main` — sincroniza con remoto.
2. Lee `status.yaml` para ver qué `TAREA-NNN` están en estado `En progreso`. **No toques los archivos asociados a una tarea ajena en curso** (revisa su campo `relacionadas` y la ficha en `08_tareas/backlog/`).
3. Calcula los siguientes IDs libres ejecutando, desde la raíz del repo:

   ```bash
   for p in FTE NOR REL CUR CHUNK PREG TAREA DEC; do
     last=$(grep -rhoE "${p}-[0-9]{3,5}" 06_indices 02_normativa 03_curriculos 05_relaciones 07_corpus_ia 08_tareas 09_decisiones-editoriales 01_fuentes 2>/dev/null \
            | sort -V | tail -1)
     echo "$p siguiente libre tras $last"
   done
   ```

   Anota los IDs que vas a usar en tu plan **antes** de crear ficheros.

### 16.2 Reserva temprana de IDs

- En cuanto sepas qué `NOR-NNN`/`FTE-NNN`/`TAREA-NNN` necesitas, **regístralos cuanto antes en su índice YAML** (`06_indices/normativa.yaml`, `06_indices/fuentes.yaml`, `06_indices/tareas.yaml`, etc.) y haz commit + push pronto. El push publica tu reserva y bloquea ese ID frente a otros agentes.
- No agrupes muchas TAREA en un único commit gigante: divide en commits pequeños (uno por bloque lógico) y empuja cada uno en cuanto valide. Cuanto antes empujes, antes ven los demás agentes lo que has reservado.

### 16.3 Antes de cada commit

1. `git fetch origin main` — comprueba si hay nuevos commits.
2. Si los hay, `git pull --rebase origin main` y resuelve cualquier conflicto antes de continuar.
3. Vuelve a comprobar IDs libres por si el rebase ha incorporado nuevas reservas.
4. `python3 -c "import yaml,pathlib; [yaml.safe_load(pathlib.Path(p).read_text()) for p in ['status.yaml','06_indices/tareas.yaml','06_indices/normativa.yaml','06_indices/fuentes.yaml','06_indices/relaciones.yaml','06_indices/curriculos.yaml','06_indices/chunks.yaml','06_indices/preguntas.yaml','06_indices/textos-oficiales.yaml']]; print('OK')"` — valida que todos los índices YAML parsean limpios.

### 16.4 Selección de archivos a `git add`

- **Solo añade los archivos que tú has tocado en esta tarea.** No incluyas archivos `?? untracked` que pertenezcan a otra tarea ajena (suelen verse en `git status` como creados por otra rama de trabajo).
- En `status.yaml` y `06_indices/tareas.yaml` toca **solo los bloques de tu propia TAREA**, no los del trabajo paralelo.
- No incluyas `.omc/` ni otros artefactos de tooling.

### 16.5 Manejo de colisiones de ID y de path

Si al hacer `git fetch`/`git pull` o al crear ficheros descubres que el ID que ibas a usar ya existe:

1. **No reutilices el ID** (R10). Renumera tu trabajo al siguiente ID libre.
2. Renombra ficheros (Markdown y YAML), actualiza el frontmatter (`id:`), las cabeceras (`# NOR-XXX — ...`), las referencias internas (otros `NOR-`, `REL-`, `relacionadas:` en TAREA, etc.) y los enlaces relativos en otras fichas que ya apunten al ID antiguo.
3. Actualiza la entrada del índice YAML correspondiente.
4. Documenta el cambio en el diario y en la sección «Coordinación con trabajo paralelo» de la ficha de TAREA.
5. Vuelve a validar YAML antes del commit.

### 16.6 Reglas de oro

- **Sincroniza pronto, sincroniza a menudo**: `git fetch` antes de iniciar bloque, antes de validar y antes de commit.
- **Commits pequeños** centrados en una sola TAREA: facilitan el merge y minimizan colisiones.
- **No edites ficheros de la TAREA de otra IA mientras esté `En progreso`**: ni `CUR-NNN` ni `NOR-NNN` ni su `TAREA-NNN.md`. Si necesitas cruzar referencia, hazlo desde tu lado.
- **Tras un push exitoso, anuncia en el diario** los IDs que has consumido para que el siguiente agente los vea de un vistazo.
- **Si sospechas que tu árbol local tiene ediciones de otro agente** (ficheros modificados que tú no has tocado), no los `git add`: déjalos para que la otra IA los empuje en su commit.
