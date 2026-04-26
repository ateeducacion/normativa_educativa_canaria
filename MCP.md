# Uso del repositorio con GitHub MCP Server

GitHub MCP Server no convierte este repositorio en una API jurídica pública por sí mismo. Su función es permitir que un cliente compatible con MCP (Model Context Protocol) acceda a los archivos del repositorio en GitHub y los use como contexto de trabajo para una IA.

Este repositorio está pensado para ayudar a localizar, relacionar y resumir normativa educativa aplicable a Canarias. No sustituye la consulta de BOE, BOC ni otros portales oficiales.

## Casos de uso recomendados

- pedir a un cliente de IA que busque dentro del repositorio;
- preguntar por una norma usando los archivos del repositorio como contexto;
- pedir relaciones entre currículo, etapa educativa y regulación aplicable;
- indicar al cliente que abra primero `llms.txt`;
- pedir que revise `06_indices` antes de responder.

## Flujo recomendado

1. Abra el repositorio `ateeducacion/normativa_educativa_canaria`.
2. Lea primero `llms.txt`.
3. Si hace falta más detalle, lea `llms-full.txt`.
4. Revise los índices YAML de `06_indices`.
5. Localice las fichas y fuentes relevantes.
6. Responda citando la norma por su nombre oficial y, cuando proceda, por artículo, disposición o anexo.
7. Si falta evidencia, consolidación o verificación de vigencia, indíquelo.

## Regla de cita jurídica al usuario final

No utilice como cita principal identificadores internos como `NOR-001`, `CUR-002`, `REL-003` o `CHUNK-004`.

Use la cita jurídica oficial habitual en España, por ejemplo:

- `Ley Orgánica 2/2006, de 3 de mayo, de Educación.`
- `Ley Orgánica 3/2020, de 29 de diciembre, por la que se modifica la Ley Orgánica 2/2006, de 3 de mayo, de Educación.`
- `Real Decreto 217/2022, de 29 de marzo, por el que se establece la ordenación y las enseñanzas mínimas de la Educación Secundaria Obligatoria.`
- `Decreto 211/2022, de 10 de noviembre, por el que se establece la ordenación y el currículo de la Educación Primaria en la Comunidad Autónoma de Canarias.`

Si necesita trazabilidad interna, añádala solo como información secundaria.

## Cómo conectar GitHub MCP Server

GitHub mantiene el servidor oficial en [github/github-mcp-server](https://github.com/github/github-mcp-server). Hay dos vías habituales hoy: el servidor remoto hospedado por GitHub y el servidor local en Docker. La vía remota es la recomendada cuando el cliente la admite, porque no requiere instalación.

> El paquete antiguo `npx @github/github-mcp-server` y `@modelcontextprotocol/server-github` están deprecados desde abril de 2025. No se recomiendan.

### Vía 1 — Servidor remoto hospedado (recomendado)

Endpoint público: `https://api.githubcopilot.com/mcp/`.

Para un repositorio de consulta como este, conviene usar el modo de solo lectura: `https://api.githubcopilot.com/mcp/x/repos/readonly`.

#### VS Code 1.101 o superior

Cree `.vscode/mcp.json` en su espacio de trabajo o añádalo a la configuración de usuario:

```json
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/x/repos/readonly"
    }
  }
}
```

VS Code abrirá el flujo OAuth la primera vez. No necesita un *personal access token* si tiene Copilot habilitado.

Si prefiere autenticarse con un token clásico de GitHub:

```json
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/x/repos/readonly",
      "headers": {
        "Authorization": "Bearer ${input:github_mcp_pat}"
      }
    }
  }
}
```

#### Claude Code

```bash
claude mcp add-json github '{
  "type": "http",
  "url": "https://api.githubcopilot.com/mcp/x/repos/readonly",
  "headers": { "Authorization": "Bearer YOUR_GITHUB_PAT" }
}'
```

#### Cursor

En `~/.cursor/mcp.json` o `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "github": {
      "url": "https://api.githubcopilot.com/mcp/x/repos/readonly",
      "headers": {
        "Authorization": "Bearer YOUR_GITHUB_PAT"
      }
    }
  }
}
```

#### Claude Desktop

Claude Desktop no admite todavía OAuth contra el servidor remoto. Use la vía local con Docker (más abajo).

### Vía 2 — Servidor local con Docker

Imagen oficial: `ghcr.io/github/github-mcp-server`.

Para Claude Desktop, edite `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) o el equivalente en otros sistemas:

```json
{
  "mcpServers": {
    "github": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-e", "GITHUB_PERSONAL_ACCESS_TOKEN",
        "ghcr.io/github/github-mcp-server"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "TU_TOKEN_AQUI"
      }
    }
  }
}
```

Para forzar solo lectura sin pasar por la URL `/readonly`, añada la variable de entorno `GITHUB_READ_ONLY=1` en la lista `args` y `env`.

### Cómo se indica el repositorio

GitHub MCP Server no tiene un parámetro de configuración para "anclar" el servidor a un repositorio concreto. La selección del repo es siempre parte del prompt al modelo, mediante las herramientas del *toolset* `repos` (`get_file_contents`, `search_code`, etc.). Por ejemplo:

```text
Abre el repositorio ateeducacion/normativa_educativa_canaria. Lee primero llms.txt y después responde usando los archivos del repositorio como contexto.
```

## Seguridad

- Use el token de GitHub con el menor privilegio posible.
- Para hacer preguntas y leer archivos, el acceso de solo lectura suele ser suficiente. Use el endpoint `/readonly` o `GITHUB_READ_ONLY=1`.
- Nunca suba archivos `.env` con secretos al repositorio.
- Mantenga `.env` ignorado por Git.
- Prefiera acceso a repositorios públicos cuando baste con ello.
- Antes de habilitar acciones de escritura, revise si el cliente MCP puede crear issues, pull requests o modificar contenido.
- Verifique permisos del token y del servidor MCP antes de usar capacidades de escritura.

## Prompts recomendados

```text
Abre el repositorio ateeducacion/normativa_educativa_canaria. Lee primero llms.txt. Después responde usando los archivos del repositorio como contexto. Al citar normas, usa la cita jurídica oficial habitual en España y no los IDs internos del repositorio.
```

```text
Busca en el repositorio ateeducacion/normativa_educativa_canaria la normativa vigente sobre evaluación y promoción en Educación Secundaria Obligatoria en Canarias. Usa títulos oficiales, artículos y referencias de publicación cuando estén disponibles.
```

```text
Inspecciona los índices YAML de 06_indices antes de responder. Usa los IDs internos solo para localizar archivos, no como formato público de cita.
```

## Recordatorio final

Este repositorio ayuda a estructurar y recuperar contexto documental. No reemplaza la fuente oficial ni la comprobación de vigencia de una norma.
