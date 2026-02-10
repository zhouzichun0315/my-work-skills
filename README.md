# My Work Skills

一组可复用的 [Agent Skills](https://github.com/vercel-labs/skills)，为 AI 编程助手提供专业领域能力。每个 Skill 将特定工作流封装为结构化、可重复执行的最佳实践。

## 收录的 Skills

### Paper Reading Guide — 论文交互式阅读指南

> 给定任意学术论文 PDF，自动生成一个交互式 HTML 阅读指南。

生成的阅读指南是一个**自包含的分屏网页应用**：

- **左栏**：论文各页渲染为图片，点击概念节点后自动滚动并用彩色高亮框标出相关章节
- **右栏**：可交互的概念地图（7-10 个核心概念），每个节点包含深度讲解和可展开的 Q&A

核心特性：按阅读路径逐步引导而非简单总结；每个概念节点含 8-15 条专业讲解（设计动机、公式推导、直觉类比、定量分析）；Q&A 含英文原文引用、中文学术翻译和详细解答；可拖动分隔条调整面板比例。

触发方式：「帮我读这篇论文」「给这篇论文做个阅读指南」「help me understand this paper step by step」

---

### Project Skill Generator — 项目级 Skill 生成器

> 为代码项目/服务自动生成、验证和维护 Skill 文档。

一个「元技能」——用来生成和管理其他 Skill 的 Skill。它能从代码库自动分析架构、提取核心模块、生成标准化 Skill 文档。

四大核心能力：

- **generate**：扫描代码库，自动生成 Skill 初稿（约 70% 内容），标记需人工确认的业务意图
- **validate**：检查已有 Skill 与代码的同步性，输出失效引用和建议补充的新类
- **update**：根据变更说明定向更新 Skill，保留未变更内容
- **graph**：扫描所有 Skill 的引用关系，生成 Mermaid 格式的服务依赖图谱

触发方式：「帮我为 xxx 服务生成 Skill」「检查 xxx Skill 是否过期」「生成 Skill 图谱」

## 安装

### 通过 Skills CLI 安装（推荐）

安装全部 Skills 到 [Qoder](https://qoder.com)：

```bash
npx skills add zhouzichun0315/my-work-skills -a qoder -g
```

安装单个 Skill：

```bash
# 论文阅读指南
npx skills add zhouzichun0315/my-work-skills --skill paper-reading-guide -a qoder

# 项目 Skill 生成器
npx skills add zhouzichun0315/my-work-skills --skill project-skill-generator -a qoder
```

### 支持的 AI 编程工具

本仓库遵循开放的 [Agent Skills 规范](https://agentskills.io)，兼容 35+ 种 AI 编程工具：

```bash
# Qoder
npx skills add zhouzichun0315/my-work-skills -a qoder

# Claude Code
npx skills add zhouzichun0315/my-work-skills -a claude-code

# Cursor
npx skills add zhouzichun0315/my-work-skills -a cursor

# 安装到所有已检测到的 agent
npx skills add zhouzichun0315/my-work-skills --all
```

### 手动安装

将 `skills/` 下对应的目录复制到你的 agent 技能路径：

| Agent | 路径 |
|-------|------|
| Qoder | `~/.qoder/skills/` |
| Claude Code | `~/.claude/skills/` |
| Cursor | `~/.cursor/skills/` |

## 示例

`examples/` 目录包含两篇经典论文的阅读指南成品，可直接下载体验：

| 论文 | 目录 | 说明 |
|------|------|------|
| Attention Is All You Need | [`examples/attention-is-all-you-need/`](examples/attention-is-all-you-need/) | Transformer 原始论文（15页），9 个概念节点 |
| FlashAttention | [`examples/flash-attention/`](examples/flash-attention/) | IO 感知的精确注意力算法（34页），9 个概念节点 |

**使用方式**：下载整个子目录（`reading-guide.html` + `pages/` 文件夹），用浏览器打开 HTML 即可，完全离线可用。

## 仓库结构

```
skills/
├── paper-reading-guide/            # 论文阅读指南
│   ├── SKILL.md
│   ├── assets/
│   │   └── guide-template.html         # HTML 模板（CSS + JS）
│   ├── scripts/
│   │   ├── render_pdf_pages.py         # PDF → PNG 页面渲染
│   │   └── build_guide_html.py         # JSON → 交互式 HTML
│   └── references/
│       ├── data-schema.md              # JSON 数据结构规范
│       └── content-quality.md          # 内容质量指南
│
├── project-skill-generator/        # 项目 Skill 生成器
│   ├── SKILL.md
│   └── references/
│       └── skill-template.md           # Skill 标准模板
│
examples/
├── attention-is-all-you-need/      # Transformer 阅读指南示例
│   ├── reading-guide.html
│   └── pages/                          # 15 页 PNG
│
└── flash-attention/                # FlashAttention 阅读指南示例
    ├── reading-guide.html
    └── pages/                          # 34 页 PNG
```

## 许可证

MIT
