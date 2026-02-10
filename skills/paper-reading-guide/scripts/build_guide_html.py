#!/usr/bin/env python3
"""Build the interactive reading guide HTML from a JSON data file.

Usage:
    python build_guide_html.py <data.json> <output.html> [--pages-dir pages]

The data.json must contain:
{
  "title": "Paper Title",
  "total_pages": 15,
  "nodes": [ ... ],
  "connections": [ ... ]
}

See references/data-schema.md for the full schema.
"""
import argparse, json, pathlib, sys

TEMPLATE_PATH = pathlib.Path(__file__).parent.parent / "assets" / "guide-template.html"

def main():
    parser = argparse.ArgumentParser(description="Build interactive reading guide HTML")
    parser.add_argument("data_json", help="Path to JSON data file with nodes/connections")
    parser.add_argument("output_html", help="Path to write the output HTML file")
    parser.add_argument("--pages-dir", default="pages", help="Relative path from HTML to page images (default: pages)")
    args = parser.parse_args()

    data_path = pathlib.Path(args.data_json)
    if not data_path.exists():
        print(f"Error: Data file not found: {data_path}", file=sys.stderr)
        sys.exit(1)

    if not TEMPLATE_PATH.exists():
        print(f"Error: Template not found: {TEMPLATE_PATH}", file=sys.stderr)
        sys.exit(1)

    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    template = TEMPLATE_PATH.read_text("utf-8")

    # Inject data into template
    html = template.replace("__TITLE_RAW__", data["title"])
    html = html.replace("__PAPER_TITLE__", json.dumps(data["title"], ensure_ascii=False))
    html = html.replace("__TOTAL_PAGES__", str(data["total_pages"]))
    html = html.replace("__NODES_JSON__", json.dumps(data["nodes"], ensure_ascii=False, indent=2))
    html = html.replace("__CONNECTIONS_JSON__", json.dumps(data["connections"], ensure_ascii=False, indent=2))
    html = html.replace("__PAGES_DIR__", args.pages_dir)

    output_path = pathlib.Path(args.output_html)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")

    print(f"Generated: {output_path} ({len(html)} bytes)")

if __name__ == "__main__":
    main()
