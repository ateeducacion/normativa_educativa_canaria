# Guía de validación

## Validación recomendada con AJV

```bash
npx ajv-cli validate   --spec=draft2020   -s schemas/norma.schema.yaml   -d 06_indices/normativa.yaml
```

## Validaciones mínimas del repositorio

1. Comprobar que todos los YAML parsean correctamente.
2. Verificar que cada ID aparece en su índice correspondiente.
3. Revisar que toda ficha normativa tenga fuente oficial, fecha de consulta y estado de vigencia.
4. Confirmar que los resúmenes IA incluyen la advertencia de no sustituir la fuente oficial.
5. Revisar preguntas abiertas y tareas pendientes antes de cerrar una edición.
