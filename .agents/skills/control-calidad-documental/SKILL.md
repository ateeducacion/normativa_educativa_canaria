---
    name: control-calidad-documental
    description: Validar estructura, trazabilidad y consistencia documental.
    license: CC-BY-4.0
    compatibility: opencode
    metadata:
      idioma: es
      ambito: normativa-educativa-canarias
      tipo: proceso
      version: "1.0"
      actualizado: 2026-04-25
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
