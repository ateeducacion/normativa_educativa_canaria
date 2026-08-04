---
name: publicacion-portal
description: >-
  Modifica el portal público de GitHub Pages en docs/ aplicando el sistema de diseño de DESIGN.md.
  Úsala al tocar docs/index.html u otras páginas del portal, al cambiar textos, componentes,
  estilos o lanzadores de IA, al ajustar el flujo de publicación de .github/workflows/pages.yml,
  y cuando haya que comprobar accesibilidad, diseño adaptable o funcionamiento sin JavaScript.
when_to_use: >-
  Frases que la disparan: "cambia la portada", "el portal", "docs/index.html", "añade un botón",
  "el QR", "el prompt de la web", "cómo se ve en móvil", "publica en Pages".
version: 1.0
license: CC-BY-4.0
---

# publicacion-portal

## Rol

Responsable del portal público del corpus.

## Misión

Mantener la portada y las páginas de `docs/` coherentes con el sistema de diseño, accesibles y
publicables, sin romper las URLs públicas de las que dependen personas y asistentes de IA.

## Cuándo cargarla

Cuando la tarea toque cualquier fichero de `docs/`, `DESIGN.md` o el flujo de publicación.

## Entradas esperadas

- Cambio solicitado, página afectada y, si lo hay, el diseño o maqueta de referencia.

## Salidas esperadas

- Páginas actualizadas en `docs/`, verificadas en navegador y sin enlaces rotos.

## Procedimiento

Copia esta lista y ve marcándola:

```
- [ ] 1. Leer DESIGN.md antes de tocar nada
- [ ] 2. Aplicar el cambio reutilizando tokens y componentes
- [ ] 3. Verificar en navegador a 1280 px y a 320 px
- [ ] 4. Repasar los criterios de cierre de DESIGN.md §14
```

**1. Leer `DESIGN.md`.** Es la fuente de verdad del portal. Manda sobre cualquier
maqueta: si un diseño de referencia incumple una regla (contraste, foco, objetivo
táctil), se implementa el diseño corrigiendo el incumplimiento y se avisa.

Las reglas que más se incumplen:

- §3.6 — el contenido esencial debe funcionar **sin JavaScript**; lo demás es mejora progresiva.
- §9 — WCAG 2.2 AA: foco visible, etiquetas asociadas, contraste, `prefers-reduced-motion`,
  nada que dependa sólo del color.
- §8 — una sola columna en móvil y objetivos táctiles de 44 px.
- §12.4 — nada de `innerHTML` con datos sin escapar; usar la API del DOM.
- §12.5 — consumir las propiedades personalizadas de `:root`, no hexadecimales sueltos.
- §13 — conservar el contenido y **las URLs públicas** salvo requisito explícito.

**2. Aplicar el cambio.** Reutiliza los tokens (`--ink`, `--accent`, `--accent-2`, `--rule`)
y los componentes ya definidos (`.btn`, `.terminal`, `.ai-btn`, `.example`, `.toast`) antes de
crear otros nuevos.

**3. Verificar en navegador.** No basta con que el HTML parezca correcto:

```bash
cd docs && python3 -m http.server 8777
```

Comprueba a 1280 px y a 320 px que no hay errores de consola, que la página no
desborda en horizontal y que las interacciones responden. Cierra el servidor al terminar.

**4. Criterios de cierre.** Repasa la lista de `DESIGN.md` §14 antes de dar por hecho el cambio.

## Publicación

`.github/workflows/pages.yml` compone el sitio: copia `docs/` a la raíz publicada y añade
`README.md`, `DESIGN.md`, `index.md`, `status.yaml`, `AGENTS.md`, `llms.txt`, `llms-full.txt`,
las carpetas del corpus y `SKILL.md` (dos veces, como `SKILL.md` y como `skill.md`).

Al borrar o renombrar una página de `docs/`, busca antes quién la enlaza:

```bash
grep -rn "nombre-pagina.html" --include="*.md" --include="*.html" --include="*.txt" .
```

`llms.txt` y `llms-full.txt` son recursos públicos de primer nivel: si apuntan a la página que
retiras, hay que redirigirlos en el mismo cambio.

## Reglas de evidencia

- Todo dato normativo mostrado en el portal debe proceder del corpus, no redactarse en el HTML.
- El aviso de que el resumen no sustituye la fuente oficial debe permanecer visible (R2).
- Las URLs públicas conservadas se comprueban, no se suponen.

## Anti-patrones

- No romper una URL pública sin redirigir antes lo que la enlaza.
- No introducir dependencias ni frameworks sin decisión editorial documentada.
- No dar por bueno un cambio visual sin abrirlo en un navegador.
- No usar el color como único indicador de estado.

## Plantillas relacionadas

Ninguna: el portal no produce fichas del corpus. Su referencia es `DESIGN.md`.
