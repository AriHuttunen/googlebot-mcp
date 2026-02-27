"""
Minimal MCP server that fetches web pages using a GoogleBot user-agent.

Usage:
    pip install mcp httpx
    python server.py
"""

import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("googlebot-fetch")

USER_AGENT = (
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
)


@mcp.tool()
async def fetch_page(url: str, max_length: int = 100_000) -> str:
    """Fetch a web page using a GoogleBot user-agent.

    Args:
        url: The URL to fetch.
        max_length: Max characters to return (default 100 000).
    """
    async with httpx.AsyncClient(
        follow_redirects=True,
        timeout=30,
        headers={"User-Agent": USER_AGENT},
    ) as client:
        resp = await client.get(url)
        resp.raise_for_status()

    text = resp.text
    if len(text) > max_length:
        text = text[:max_length] + f"\n\n[Truncated at {max_length} characters]"
    return text


if __name__ == "__main__":
    mcp.run()
