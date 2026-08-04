---
name: control-vigencia
description: >-
  Comprueba en fuente oficial si una norma está vigente, modificada, derogada o pendiente de
  verificación, y documenta la evidencia. Úsala al revisar el estado_vigencia de una ficha NOR,
  al comprobar si una norma sigue en vigor, o cuando la vigencia no se pueda confirmar y haya que
  abrir una PREG-NNN de seguimiento.
when_to_use: >-
  Frases que la disparan: "¿sigue vigente", "está derogado", "comprueba la vigencia", "esta norma
  la modificó", "revisa el estado de NOR-0NN".
version: 1.1
license: CC-BY-4.0
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

- `10_plantillas/markdown/plantilla-norma.md`
- `10_plantillas/markdown/plantilla-pregunta.md`
