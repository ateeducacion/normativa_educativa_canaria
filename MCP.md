# Uso del repositorio con GitHub MCP Server

GitHub MCP Server no convierte este repositorio en una API jurídica pública por sí mismo. Su función es permitir que un cliente compatible con MCP acceda a los archivos del repositorio en GitHub y los use como contexto de trabajo para una IA.

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

## Configuración de ejemplo

### VS Code / Copilot compatible

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@github/github-mcp-server"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "TU_TOKEN_AQUI"
      }
    }
  }
}
```

### Cliente MCP local genérico

```json
{
  "servers": [
    {
      "name": "github",
      "transport": "stdio",
      "command": "github-mcp-server",
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "TU_TOKEN_AQUI"
      }
    }
  ]
}
```

### Ejemplo con Docker

```bash
docker run --rm -i \
  -e GITHUB_PERSONAL_ACCESS_TOKEN=TU_TOKEN_AQUI \
  ghcr.io/github/github-mcp-server:latest
```

## Seguridad

- Use el token de GitHub con el menor privilegio posible.
- Para hacer preguntas y leer archivos, el acceso de solo lectura suele ser suficiente.
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
