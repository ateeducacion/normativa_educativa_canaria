---
    name: control-vigencia
    description: Comprobar y registrar el estado de vigencia de una norma.
    license: CC-BY-4.0
    compatibility: opencode
    metadata:
      idioma: es
      ambito: normativa-educativa-canarias
      tipo: proceso
      version: "1.0"
      actualizado: 2026-04-25
    ---

    # control-vigencia

    ## Rol

    Revisor de vigencia normativa.

    ## Misión

    Determinar y documentar si una norma está vigente, modificada, derogada o pendiente de verificación.

    ## Cuándo cargarla

    Cuando una norma nueva o existente necesite revisión de vigencia.

    ## Entradas esperadas

    - Ficha normativa, fuente oficial actualizada y cambios posteriores conocidos.

    ## Salidas esperadas

    - Estado de vigencia actualizado, notas de evidencia y acciones pendientes si no se confirma.

    ## Reglas de evidencia

    - Toda salida debe citar o apuntar a una fuente oficial o a una pregunta abierta si la fuente no se ha podido confirmar.
    - Toda fecha de consulta o análisis debe mantenerse actualizada.
    - Toda relación con otra entidad del repositorio debe quedar trazada por ID.

    ## Anti-patrones

    - No marcar una vigencia como confirmada sin evidencia.
- No borrar contenido histórico.

    ## Plantillas relacionadas

    - `10_plantillas/markdown/plantilla-fuente.md`
    - `10_plantillas/markdown/plantilla-norma.md`
    - `10_plantillas/markdown/plantilla-curriculum.md`
    - `10_plantillas/yaml/plantilla-relacion.yaml`
    - `10_plantillas/yaml/plantilla-chunk.yaml`
