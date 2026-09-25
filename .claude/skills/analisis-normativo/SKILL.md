---
name: analisis-normativo
description: Crear o actualizar una ficha NOR-NNN. Úsalo al catalogar un decreto, una orden, una resolución o una ley, o al revisar una ficha normativa.
version: "1.2"
license: CC-BY-4.0
---

# Análisis normativo

La ficha sale de la fuente oficial. No se resume una norma que no se ha abierto. La interpretación se marca `[INTERPRETACIÓN]`.

## Qué abrir según el asunto

| Asunto | Referencia |
| --- | --- |
| LOE, LOMLOE u otra norma básica estatal | [references/lomloe-loe.md](references/lomloe-loe.md) |
| BOC, Consejería o encaje autonómico | [references/normativa-canaria.md](references/normativa-canaria.md) |
| Texto consolidado estatal que no esté en el corpus | [../legalize-es/SKILL.md](../legalize-es/SKILL.md) |

Si el producto es un currículo y no una ficha de norma, el skill es `analisis-curricular`.

## Cierre de la ficha

- ID `NOR-NNN` correlativo, fecha de consulta y estado de vigencia.
- Plantilla: `10_plantillas/markdown/plantilla-norma.md`.
- Entrada en `06_indices/normativa.yaml`.
- Si falta un dato, `[PENDIENTE]` o una `PREG-NNN`. No se inventa.
