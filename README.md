# GoogleBot Fetch MCP Server

Minimal MCP server that fetches web pages using a GoogleBot user-agent string.

## Setup

```bash
cd googlebot-mcp
uv sync
```

## Add to Claude Desktop

Edit your Claude Desktop config (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

```json
{
  "mcpServers": { 
    "googlebot-fetch": {
      "command": "uv",
      "args": ["run", "--directory", "/Users/ari/github/googlebot-mcp", "python", "server.py"]
    }
  }
}
```

Then restart Claude Desktop.

## Tool

**fetch_page(url, max_length?)** — Fetches the given URL with `Googlebot/2.1` user-agent. Returns the raw HTML. `max_length` defaults to 100 000 characters.
