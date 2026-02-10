# Data Schema for Paper Reading Guide

The `data.json` file drives the entire interactive guide. Structure:

```json
{
  "title": "Paper Title Here",
  "total_pages": 15,
  "nodes": [ <NodeObject>, ... ],
  "connections": [ {"from": "node_id_1", "to": "node_id_2"}, ... ]
}
```

## Node Object

```json
{
  "id": "unique_snake_case_id",
  "label": "显示名称 (2-5字)",
  "emoji": "🎯",
  "color": "#ef4444",
  "x": 50,
  "y": 8,
  "section": "第X节：Section Title",
  "pages": [1, 2],
  "scrollTo": 2,
  "highlights": [
    {"page": 1, "top": 35, "height": 60},
    {"page": 2, "top": 5, "height": 90}
  ],
  "keyQuestion": "这个概念要回答的核心问题？",
  "content": [
    {"type": "h3", "text": "小节标题"},
    {"type": "p", "text": "段落正文，可用 <strong>加粗</strong>、<sub>下标</sub>、<sup>上标</sup> 等 HTML"},
    {"type": "bullet", "text": "<strong>要点标题</strong>：要点解释"},
    {"type": "step", "text": "① 步骤说明"}
  ],
  "thinkAbout": [
    {
      "q": "引导问题（中文）",
      "en": "Relevant original English text from the paper",
      "zh": "对应的专业中文学术翻译",
      "a": "问题的详细解答"
    }
  ],
  "paperRef": "论文第X页 Section Y"
}
```

## Field Details

### Position Fields
- `x`, `y`: Percentage position (0-100) in the concept map. `x=50, y=8` means horizontally centered, near top.
- Layout tip: Use y=8 for top, y=30 for upper-mid, y=52 for middle, y=74 for lower-mid, y=95 for bottom.

### Page Reference Fields
- `pages`: Array of page numbers that contain this concept's content.
- `scrollTo`: Which page to auto-scroll to when this node is clicked.
- `highlights`: Array of highlight overlays. Each has `page` (1-indexed), `top` (% from top of page), `height` (% of page height). These create colored semi-transparent overlays on the PDF pages.

### Content Types
- `h3`: Sub-section heading within the explanation.
- `p`: Paragraph. Supports inline HTML: `<strong>`, `<em>`, `<sub>`, `<sup>`, `<code>`.
- `bullet`: Bulleted item with dot prefix.
- `step`: Numbered/labeled step (bold text).

### Connections
Each connection draws a dashed line between two nodes in the concept map. Use to show prerequisite/dependency relationships between concepts.

## Color Palette (suggested)

| Purpose | Hex |
|---------|-----|
| Red (problem/motivation) | #ef4444 |
| Amber (core mechanism) | #f59e0b |
| Purple (advanced concept) | #8b5cf6 |
| Blue (architecture) | #3b82f6 |
| Cyan (component) | #06b6d4 |
| Green (encoding/input) | #10b981 |
| Pink (training) | #ec4899 |
| Indigo (results) | #6366f1 |
| Orange (analysis) | #f97316 |
