---
name: paper-reading-guide
description: Generate interactive HTML reading guides for academic papers. Given a PDF paper, creates a split-pane web app with PDF viewer (left, with colored highlights) and concept map + deep explanations (right). Use when users want to deeply study a paper, create guided reading materials, or build interactive paper walkthroughs. Triggers include requests like "help me read this paper", "create a reading guide", "make an interactive guide for this paper", or "help me understand this paper step by step".
---

# Paper Reading Guide

Generate an interactive HTML reading guide from any academic paper PDF. The output is a self-contained split-pane web app: left pane shows PDF pages with colored section highlights, right pane has an interactive concept map with deep explanations and expandable Q&A.

## Workflow

1. **Render PDF pages** — Run `scripts/render_pdf_pages.py`
2. **Analyze paper** — Read the PDF, extract key concepts, structure data
3. **Build data.json** — Create the JSON data file following the schema
4. **Generate HTML** — Run `scripts/build_guide_html.py`
5. **Verify** — Open in browser, test interactions, fix highlight positions

## Step 1: Render PDF Pages

```bash
python scripts/render_pdf_pages.py <paper.pdf> <output_dir>/pages --scale 2
```

Outputs `page_1.png` ... `page_N.png` and prints JSON with `total_pages`.

If pypdfium2 is missing, the script auto-installs it.

## Step 2: Analyze the Paper

Read the full paper text. Identify 7-10 core concepts that form a logical reading path. For each concept, determine:

- Which section(s) of the paper it corresponds to
- What core question it answers
- Which pages contain the relevant content
- Where on those pages the content appears (for highlight overlays)

**Concept selection guidelines:**
- Start with "problem/motivation" and end with "results/implications"
- Include both high-level architecture and key components
- Each concept should map to a specific paper section
- Arrange concepts in a logical reading order, not just paper order

## Step 3: Build data.json

Create a JSON file following the schema in [references/data-schema.md](references/data-schema.md).

Key requirements for content quality — see [references/content-quality.md](references/content-quality.md) for full guidelines:

- Each node needs 8-15 content items (h3/p/bullet/step mix)
- Include: design motivation, formula derivation, intuitive analogy, comparison with alternatives, quantitative evidence
- Each node needs 3 Q&A items with verbatim English quotes, professional Chinese translation, and insightful answers
- Highlight positions are top% and height% estimates of where content appears on each page

**Concept map layout:** Place nodes using x (0-100) and y (0-100) percentages. Suggested y-levels: 8 (top) → 30 → 52 → 74 → 95 (bottom). Connect nodes with `connections` array to show dependencies.

### Building data.json with Python

Use `json.dumps(data, ensure_ascii=False, indent=2)` to serialize. This properly handles Chinese text and all special characters, avoiding JavaScript quote-escaping issues.

```python
import json

data = {
    "title": "Paper Title",
    "total_pages": N,
    "nodes": [ ... ],
    "connections": [ ... ]
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

## Step 4: Generate HTML

```bash
python scripts/build_guide_html.py data.json <output_dir>/reading-guide.html --pages-dir pages
```

The `--pages-dir` must be the relative path from the HTML file to the page images directory.

## Step 5: Verify

Serve the output directory and open in browser:

```bash
cd <output_dir> && python -m http.server 8977
```

Test checklist:
- Click each concept node → left pane scrolls to correct page with highlights
- Highlights align with actual content on the PDF page
- Concept explanations are detailed and accurate
- Q&A items expand/collapse, showing original text + translation + answer
- Draggable divider resizes panes smoothly

## Important Notes

- All content must be serialized through `json.dumps()` — never manually concatenate Chinese text into JavaScript strings
- The HTML template at `assets/guide-template.html` uses these placeholders: `__PAPER_TITLE__`, `__TOTAL_PAGES__`, `__NODES_JSON__`, `__CONNECTIONS_JSON__`, `__PAGES_DIR__`
- Page images must be named `page_1.png`, `page_2.png`, etc.
- Final output directory structure should be:
  ```
  output/
  ├── reading-guide.html
  └── pages/
      ├── page_1.png
      ├── page_2.png
      └── ...
  ```
