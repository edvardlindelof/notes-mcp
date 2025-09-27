import re
import yaml
import argparse
from pathlib import Path
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
    match_yaml = re.match(r"---\n(.*?)\n---", yaml_frontmatter, re.DOTALL)
    if not match_yaml:
        raise ValueError(r"YAML frontmatter doesn't match '---\n(.*)\n---'")
    yaml.safe_load(match_yaml.group(1))  # validate

    (root_dir / path).write_text(f"{yaml_frontmatter}\n{markdown_content}")
    return f"File written: {path}"

@mcp.tool()
def glob(pattern: str) -> list[str]:
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

# TODO consider extending and optimizing
@mcp.tool()
def search(query: list[str], path: str = ".", in_markdown: bool = False) -> list[str]:
    """Search for text in YAML frontmatter, and optionally in markdown content.

    Return a list of file paths that match the query.
    """
    files_content = (
        (str(p), p.read_text().lower().split("---", 2))
        for p in (root_dir / path).rglob("*.md") if p.is_file()
    )
    return [
        p for p, (_, yaml_part, md_part) in files_content
        if any(q.lower() in yaml_part for q in query)
        or (in_markdown and any(q.lower() in md_part for q in query))
    ]


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
