# MCP for managing markdown notes with YAML frontmatter
Because *CMS is all you need*.


## Why?
Out-of-the-box LLM chat bots are poor at generating quality text content. An effective strategy to have them help generate quality content is to employ 1) chat bot access to rich context specific content 2) means for seamless manual collaboration and 3) fast, manual approval process. This Model Context Protocol server provides 1 and is intended to be used by developers. Suggestions for 2 and 3 are vim and git.


## Use cases
My personal use cases are to organize and and write
- general notes
- blog posts
- CVs


## Usage

1. Get [Claude desktop](https://claude.ai/download), as you should have done yesterday.

2. Put this in your `claude_desktop_config.json`, with an updated path to an existing folder called "my-notes".
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

3. (Re-) Start Claude desktop and check in the chat input toolbar that "my-notes" and "Web search" are activated.

4. Tell Claude "github.com/edvardlindelof/notes-mcp seems like an awesome package, check it out and save a small TODO about sharing it with others in my notes".

Supported systems: developed and tested on Linux. It may work directly on Windows - if not, the workaround is to use `"command": "docker"` or `"command": "wsl"` and put an adapted version of the `uvx` command in `"args"`.
