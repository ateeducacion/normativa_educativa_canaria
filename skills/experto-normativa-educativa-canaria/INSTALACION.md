# Instalación de la skill «Experto en normativa educativa de Canarias»

La skill es un texto Markdown (`SKILL.md`). Para usarla, basta con **copiar su contenido** y pegarlo como **system prompt** o «instrucciones del proyecto/asistente» en la herramienta de IA que utilices.

## Tabla rápida por plataforma

| Plataforma | Cómo instalar | Documentación oficial |
| --- | --- | --- |
| **Claude.ai (web/escritorio)** | Crea un *Project* nuevo. En *Custom instructions*, pega el contenido de `SKILL.md`. Puedes añadir además los `llms.txt`/`llms-full.txt` como archivos del proyecto. | [Projects de Claude](https://www.anthropic.com/news/projects) |
| **Claude Code (CLI)** | Copia el contenido en `~/.claude/CLAUDE.md` (global) o en `CLAUDE.md` del proyecto. Alternativamente, déjalo como `~/.claude/skills/experto-normativa-educativa-canaria/SKILL.md` para invocarlo con la herramienta `Skill`. | [Claude Code memory](https://docs.claude.com/en/docs/claude-code/memory) |
| **ChatGPT (custom GPT)** | *Explore GPTs → Create*. En *Instructions*, pega `SKILL.md`. Sube `llms.txt`/`llms-full.txt` como archivos de conocimiento. | [Building custom GPTs](https://help.openai.com/en/articles/8554407-gpts-faq) |
| **ChatGPT (sin GPT)** | *Settings → Personalization → Custom Instructions*, pega un resumen de `SKILL.md` en «How would you like ChatGPT to respond?» y referencia la URL del repo. | [Custom instructions](https://help.openai.com/en/articles/8096356-custom-instructions-for-chatgpt) |
| **Google Gemini (Gems)** | *Create new Gem* → pega `SKILL.md` en *Instructions*. | [Gemini Gems](https://gemini.google/overview/gems/) |
| **GitHub Copilot Chat** | Usa el archivo `AGENTS.md` ya presente en este repo, o pega `SKILL.md` al inicio de la conversación con `/explain` o como contexto del chat. | [Copilot custom instructions](https://docs.github.com/en/copilot/customizing-copilot) |
| **OpenAI Codex CLI** | Coloca el contenido en `AGENTS.md` en la raíz del proyecto donde quieras usarlo. | [Codex CLI](https://github.com/openai/codex) |
| **Cursor / Windsurf** | Crea o edita `.cursorrules` (Cursor) o `.windsurfrules` (Windsurf) y pega `SKILL.md`. | Documentación de cada producto. |
| **Cualquier otro chat** | Pega `SKILL.md` como **primer mensaje** del chat con la indicación: «Adopta este rol y responde según estas reglas». | — |

## Modo simple — copia y pega (recomendado para empezar)

Si solo quieres una respuesta puntual, no necesitas instalar nada. Abre el chat y pega lo siguiente al inicio (sustituye `<TU PREGUNTA>`):

```
Adopta este rol durante toda la conversación:

[Pega aquí el contenido de SKILL.md]

Pregunta:
<TU PREGUNTA>
```

## Modo con contexto — pega también el `llms.txt`

Para un contexto más completo, añade al system prompt el contenido del `llms.txt` y, si lo necesitas, el `llms-full.txt`:

- `llms.txt`: https://ateeducacion.github.io/normativa_educativa_canaria/llms.txt
- `llms-full.txt`: https://ateeducacion.github.io/normativa_educativa_canaria/llms-full.txt

Esto da al asistente la estructura del corpus, las reglas de evidencia y el vocabulario de IDs (`NOR-`, `CUR-`, `FTE-`, etc.).

## Modo avanzado (opcional) — corpus completo en el proyecto

Si vas a hacer muchas consultas, descarga el repositorio y enláza/sube los YAML clave a tu proyecto/asistente:

1. `git clone https://github.com/ateeducacion/normativa_educativa_canaria`
2. Sube al proyecto/asistente al menos:
   - `06_indices/normativa.yaml`
   - `06_indices/fuentes.yaml`
   - `06_indices/curriculos.yaml`
   - `06_indices/relaciones.yaml`
   - Las fichas `02_normativa/**/*.md` que te interesen.
3. Añade `SKILL.md` como instrucciones de sistema.

## Comprobación

Después de instalar, valida con un prompt sencillo (ver `prompts.md`):

> «¿Cuál es la norma autonómica vigente que regula el currículo de ESO en Canarias y qué real decreto estatal desarrolla?»

La respuesta debería:

- Citar el **Decreto 30/2023, de 16 de marzo**, BOC n.º 58 de 23-03-2023.
- Mencionar el **Real Decreto 217/2022** como base estatal.
- Indicar que sustituye al Decreto 315/2015.
- Dejar claro que la **LOMLOE no deroga la LOE**, solo la modifica.

Si la respuesta no incluye estos datos, revisa que el `SKILL.md` se haya guardado completo.
