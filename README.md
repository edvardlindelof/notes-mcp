# MCP for managing markdown notes with YAML frontmatter
Because *CMS is all you need*.


## Usage with Claude desktop
Supported systems: Linux

`claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "my-notes": {
      "command": "uvx",
      "args": ["notes-mcp", "/home/me/path/to/my-notes"]
    }
  }
}
```
