# Skills

Skills internas del repositorio para catalogación, análisis, vigencia, currículo, control de
calidad y portal público. Cuándo cargar cada una: `AGENTS.md` §14.

## Dónde viven y por qué

El origen canónico es esta carpeta, `.agents/skills/`, siguiendo la convención `.agents`
portable entre clientes de IA. Claude Code, en cambio, solo descubre skills en
`.claude/skills/` (proyecto), `~/.claude/skills/` (personal) y plugins, así que
`.claude/skills/` contiene un enlace simbólico por skill que apunta aquí. Claude Code sigue
los enlaces y lee el `SKILL.md` del destino.

Al crear una skill nueva hay que crear también su enlace, o quedará invisible:

```bash
ln -sfn ../../.agents/skills/<nombre> .claude/skills/<nombre>
```

## Formato

Cada skill es un directorio con un `SKILL.md` cuyo frontmatter declara:

- `name`: minúsculas, números y guiones; debe coincidir con el nombre del directorio.
- `description`: qué hace **y cuándo usarla**, en tercera persona y con términos concretos.
  Es el único texto que ve el modelo al decidir si carga la skill.
- `when_to_use`: frases de disparo que complementan a `description`.
- `version` y `license`.

`description` y `when_to_use` suman como mucho 1.536 caracteres en el listado de skills.

## No confundir con `skills/`

`skills/experto-normativa-educativa-canaria/` es otra cosa: la skill **pública** y copiable
que se publica como `SKILL.md` en GitHub Pages para usarse en asistentes externos.
