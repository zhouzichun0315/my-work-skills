# My Work Skills

A collection of reusable [Agent Skills](https://github.com/vercel-labs/skills) for AI coding assistants. These skills package domain expertise into structured, repeatable workflows.

## Available Skills

### Paper Reading Guide

> Generate interactive HTML reading guides for academic papers.

Given any PDF paper, this skill creates a **self-contained, split-pane web app**:

- **Left pane**: PDF pages rendered as images, with colored highlight overlays on relevant sections
- **Right pane**: Interactive concept map with 7-10 core concepts, deep explanations, and expandable Q&A

**Key features:**

- Step-by-step guided reading path — not just a summary
- Each concept node includes 8-15 detailed content items covering design motivation, formula derivation, intuitive analogies, and quantitative evidence
- Expandable Q&A with verbatim English quotes, professional Chinese academic translation, and insightful answers
- Click a concept node to auto-scroll to the relevant paper pages with visual highlighting
- Draggable divider to resize panes

**Trigger phrases:**

- "help me read this paper"
- "create a reading guide for this paper"
- "help me understand this paper step by step"

## Installation

### Via Skills CLI (Recommended)

Install to [Qoder](https://qoder.com):

```bash
npx skills add zhouzichun0315/my-work-skills --skill paper-reading-guide -a qoder
```

Install globally (available across all projects):

```bash
npx skills add zhouzichun0315/my-work-skills --skill paper-reading-guide -a qoder -g
```

### Supported Agents

This skill follows the open [Agent Skills specification](https://agentskills.io) and works with 35+ AI coding tools. Some examples:

```bash
# Qoder
npx skills add zhouzichun0315/my-work-skills -a qoder

# Claude Code
npx skills add zhouzichun0315/my-work-skills -a claude-code

# Cursor
npx skills add zhouzichun0315/my-work-skills -a cursor

# Install to all detected agents
npx skills add zhouzichun0315/my-work-skills --all
```

### Manual Installation

Copy the `skills/paper-reading-guide/` directory to your agent's skill path:

| Agent | Path |
|-------|------|
| Qoder | `~/.qoder/skills/paper-reading-guide/` |
| Claude Code | `~/.claude/skills/paper-reading-guide/` |
| Cursor | `~/.cursor/skills/paper-reading-guide/` |

## Repository Structure

```
skills/
└── paper-reading-guide/
    ├── SKILL.md              # Skill definition and workflow
    ├── assets/
    │   └── guide-template.html   # HTML template with CSS + JS
    ├── scripts/
    │   ├── render_pdf_pages.py   # PDF → PNG page renderer
    │   └── build_guide_html.py   # JSON data → interactive HTML
    └── references/
        ├── data-schema.md        # JSON data structure spec
        └── content-quality.md    # Content quality guidelines
```

## How It Works

1. **Render PDF** — Convert each page of the paper to a PNG image using `pypdfium2`
2. **Analyze** — AI reads the full paper and extracts 7-10 core concepts
3. **Build data** — Structure the analysis into a JSON file (nodes, content, Q&A, highlights)
4. **Generate HTML** — Inject the JSON into the HTML template to produce a self-contained interactive guide
5. **Verify** — Open in browser to test all interactive features

## Preview

After generation, the output looks like this:

```
output/
├── reading-guide.html    # Open this in any browser
└── pages/
    ├── page_1.png
    ├── page_2.png
    └── ...
```

Simply open `reading-guide.html` in a browser — no server required, fully offline.

## License

MIT
