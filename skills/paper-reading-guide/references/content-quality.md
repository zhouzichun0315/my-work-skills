# Content Quality Guide

## Principles for Node Explanations

Each node's `content` array should provide a **deep, professional explanation** — not a simple summary. Target: 8-15 content items per node (mix of h3, p, bullet).

### What to include for each concept:

1. **Design motivation** — Why does this component exist? What problem does it solve?
2. **Core formula/mechanism** — Present the key formula, then explain each term with mathematical intuition.
3. **Step-by-step derivation** — Break complex formulas into digestible steps. Explain the "why" behind each operation.
4. **Intuitive analogy** — A concrete, relatable metaphor (e.g., "like searching a library", "like a clock with multiple hands").
5. **Comparison with alternatives** — How does this approach differ from prior/competing methods? Why is it better?
6. **Quantitative evidence** — Reference specific numbers from the paper (BLEU scores, FLOPs, ablation results).
7. **Broader significance** — How did this influence later work? What principle does it embody?

### Example of weak vs strong content:

**Weak** (too brief):
```json
{"type": "p", "text": "FFN does nonlinear transformation. 512→2048→512."}
```

**Strong** (professional depth):
```json
[
  {"type": "h3", "text": "公式与结构"},
  {"type": "p", "text": "<strong>FFN(x) = max(0, xW<sub>1</sub>+b<sub>1</sub>)W<sub>2</sub>+b<sub>2</sub></strong>"},
  {"type": "p", "text": "这是一个两层的全连接网络，中间用 ReLU 激活。维度变化：512→2048→512。先「扩展」到4倍维度（增加表达能力），再「压缩」回原始维度（便于残差连接）。论文特别指出，这等价于<strong>两个 kernel size=1 的卷积</strong>，因为它对每个位置独立操作。"},
  {"type": "h3", "text": "为什么必须有 FFN？——角色分工"},
  {"type": "p", "text": "Self-Attention 本质上只做「线性加权平均」：output = Σ(αᵢ·vᵢ)。没有非线性激活，多层堆叠仍是线性变换。FFN 中的 ReLU 提供了关键的<strong>非线性</strong>。后续研究还发现 FFN 充当「知识记忆体」角色。"}
]
```

## Principles for Q&A Items

Each node should have 3 Q&A items (`thinkAbout`). Each item has four parts:

- `q`: A thought-provoking question that guides the reader to engage with the paper critically
- `en`: The **exact** original English text from the paper that answers or relates to this question
- `zh`: A **professional academic Chinese translation** (not casual, not machine-translation-style)
- `a`: A detailed, insightful answer that connects the question to the paper's content

### Q&A quality checklist:
- Questions should require **thinking**, not just lookup
- English quotes must be **verbatim** from the paper
- Chinese translations should read like a published academic paper
- Answers should provide **insight beyond** what the paper explicitly states

## Highlight Position Estimation

When specifying `highlights` for each node, estimate the position of relevant content on the PDF page:

- `top`: percentage from top of page where the relevant section starts (0 = very top, 100 = very bottom)
- `height`: percentage of page height that the section spans

Guidelines:
- Title/author block: top=0, height=15
- Abstract: top=15, height=20
- A typical section takes 30-50% of a page
- Figures typically take 40-60% of page height
- Be generous with highlights — better to include slightly more than to miss content
