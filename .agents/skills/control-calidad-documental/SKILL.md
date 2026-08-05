---
name: control-calidad-documental
description: >-
  Valida estructura, trazabilidad y consistencia documental del corpus: frontmatter, esquemas,
  índices YAML, enlaces, IDs y fechas obligatorias. Úsala antes de cerrar una TAREA, después de
  cambios amplios, o cuando haya que comprobar que cada entidad está en su índice y cumple las
  reglas R1 a R16 de AGENTS.md.
when_to_use: >-
  Frases que la disparan: "valida el repositorio", "revisa la calidad", "está todo indexado",
  "antes de cerrar la tarea", "comprueba la trazabilidad".
version: 1.1
license: CC-BY-4.0
---

# control-calidad-documental

## Rol

Revisor de calidad documental.

## Misión

Comprobar que Markdown, YAML, índices, enlaces y estados cumplen las reglas del repositorio.

## Cuándo cargarla

Antes de cerrar tareas o después de cambios amplios.

## Entradas esperadas

- Árbol afectado, índices, schemas y dudas detectadas.

## Salidas esperadas

- Informe de validación, correcciones propuestas y bloqueos documentales.

## Procedimiento

Copia esta lista y ve marcándola:

```
- [ ] 1. Ejecutar el validador
- [ ] 2. Resolver los errores
- [ ] 3. Revisar los avisos
- [ ] 4. Volver a validar hasta 0 errores
```

**1. Ejecutar el validador.** Comprueba de una vez los esquemas de `schemas/`, la
coincidencia entre el `id` del frontmatter y el nombre del fichero, la cobertura de
los índices de `06_indices/` en ambos sentidos, que cada `ruta` del índice resuelva
a su propia ficha, que los campos que el índice duplica coincidan con la ficha, que
las entidades citadas en campos de relación existan, y que las copias locales de
`07_corpus_ia/textos-completos/` no estén dobles-codificadas:

```bash
pip install --quiet pyyaml jsonschema   # sólo la primera vez
python3 11_calidad/validar_corpus.py
```

Opciones: `--sin-avisos` para ver sólo lo que bloquea, `--tipo NOR` para acotar a
un tipo de entidad, `--json` para consumir el resultado desde otro proceso.

**2. Resolver los errores.** Devuelve código 1 y bloquean el cierre de tarea
(AGENTS.md §15). El más habitual es «existe como ficha pero no está en el índice»:
se corrige añadiendo la entrada al índice correspondiente, derivándola de la propia
ficha. Nunca se resuelve un error inventando el dato que falta (R1); si no hay
evidencia, se marca `[PENDIENTE]` (R15) y se abre una `PREG-NNN` (R12).

**3. Revisar los avisos.** No bloquean. Señalan campos recomendados ausentes y
entradas de índice sin ficha, que son deuda documental histórica.

Si el error es de codificación en `TEXTOS`, se repara con:

```bash
python3 11_calidad/reparar_mojibake.py 07_corpus_ia/textos-completos --aplicar
```

**4. Volver a validar** hasta que el total de errores sea 0.

El mismo validador corre en integración continua
(`.github/workflows/validar-corpus.yml`) en cada push y cada pull request.

## Reglas de evidencia

- Toda salida debe citar o apuntar a una fuente oficial o a una pregunta abierta si la fuente no se ha podido confirmar.
- Toda fecha de consulta o análisis debe mantenerse actualizada.
- Toda relación con otra entidad del repositorio debe quedar trazada por ID.

## Anti-patrones

- No dar por válida una ficha sin índice.
- No ignorar dudas abiertas o fechas ausentes.

## Plantillas relacionadas

- `10_plantillas/markdown/plantilla-fuente.md`
- `10_plantillas/markdown/plantilla-norma.md`
- `10_plantillas/markdown/plantilla-curriculum.md`
- `10_plantillas/yaml/plantilla-relacion.yaml`
- `10_plantillas/yaml/plantilla-chunk.yaml`
