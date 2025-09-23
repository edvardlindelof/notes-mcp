import yaml
import argparse
from pathlib import Path
from typing import Dict, Any, List
from fastmcp import FastMCP


parser = argparse.ArgumentParser(description="YAML frontmatter markdown notes MCP server")
parser.add_argument("root_dir", help="Root directory for notes")
root_dir = Path(parser.parse_args().root_dir)


mcp = FastMCP("Notes MCP")


@mcp.tool()
def read(path: str) -> str:
    """Read a note file and return YAML frontmatter and markdown content."""
    return (root_dir / path).read_text()

@mcp.tool()
def write(path: str, yaml_frontmatter: str, markdown_content: str) -> str:
    """Write a note file with YAML frontmatter and markdown content."""
    yaml.safe_load(yaml_frontmatter)  # validate YAML
    (root_dir / path).write_text(f"---\n{yaml_frontmatter}\n---\n{markdown_content}")
    return f"File written: {path}"

@mcp.tool()
def glob(pattern: str) -> List[str]:
    """Find files matching a pattern in the content directory."""
    return [str(p) for p in root_dir.glob(pattern)]

@mcp.tool()
def mkdir(path: str) -> str:
    """Create a directory."""
    (root_dir / path).mkdir(parents=True, exist_ok=True)
    return f"Directory created: {path}"

@mcp.tool()
def rm(path: str) -> str:
    """Remove a file."""
    (root_dir / path).unlink(missing_ok=True)
    return f"File removed: {path}"

@mcp.tool()
def rmdir(path: str) -> str:
    """Remove a directory."""
    (root_dir / path).rmdir()
    return f"Directory removed: {path}"

@mcp.tool()
def search(query: str, in_frontmatter: bool = True, in_markdown: bool = True) -> List[Dict[str, Any]]:
    """Search for text in YAML frontmatter and/or markdown content."""
    raise NotImplementedError("Search functionality is not implemented yet.")


mcp.run()
