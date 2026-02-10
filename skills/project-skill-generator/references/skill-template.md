# Skill 标准模板

生成项目/服务级Skill时使用此模板。

## 文件结构

```
{skill-name}/
├── SKILL.md          # 主文件（必需）
└── references/       # 参考文档（可选）
    ├── api-docs.md   # API详细文档
    └── examples.md   # 扩展示例
```

## SKILL.md 模板

```markdown
---
name: {service-name}
description: {服务名称}架构与实现指南。适用场景：(1) 在{服务名称}上开发新功能模块 (2) 将{服务名称}的能力迁移到其他服务 (3) 对{服务名称}进行架构重构。{核心能力概述}。
code_path: {代码库绝对路径}
last_verified: {YYYY-MM-DD}
---

# {服务名称} Skill

## Overview

{一句话描述服务定位}，主要应用于 **{应用场景1}** 和 **{应用场景2}**。{技术架构概述}。

**业务价值：**
- {价值点1}
- {价值点2}
- {价值点3}

**核心能力：**
- {能力1}
- {能力2}
- {能力3}

## Architecture

```
{ASCII架构图}
```

**数据流：**
```
{数据流转说明}
```

## Core Modules

### 1. {模块名称}

**基类：** `{BaseClassName}`
- 模板方法：{方法说明}
- 关键方法：{关键方法}
- 语义：{如何扩展}

**实现类：**

| 名称 | 类名 | 说明 |
|-----|------|-----|
| {实现1} | `{ClassName1}` | {说明} |
| {实现2} | `{ClassName2}` | {说明} |

### 2. {模块名称}

...

## Dependencies

### 内部依赖

**{依赖类型}：** `{接口名}` / `{实现类名}`
- `{方法1}()` - {说明}
- `{方法2}()` - {说明}

### 外部依赖（接口契约）

**{中间件名称}：** `@ref:{middleware-skill-name}`
- 用途：{用途说明}
- 接入类：`{GatewayImpl}`

## Usage Patterns

### {扩展场景1}

```java
@Component
public class New{Type}Action extends Base{Type}Action {
    
    @Autowired
    private {Gateway} gateway;
    
    @Override
    protected {ReturnType} do{Method}({Context} context) {
        // 实现逻辑
    }
}
```

**配套修改：**
1. {修改点1}
2. {修改点2}

## Pitfalls & Notes

### {踩坑点1标题}

{问题描述}

**解决方案：**
```java
// 正确做法
```

### {踩坑点2标题}

{注意事项说明}
```

## 填写指南

### Frontmatter 字段

- **name**：服务名称，与目录名一致
- **description**：一句话描述 + 适用场景列表
- **code_path**：该服务的本地代码库绝对路径。此字段用于后续 validate/update 操作时自动定位代码
- **last_verified**：最后一次验证Skill与代码同步性的日期

### Overview 章节

- **服务定位**：一句话说明服务做什么
- **应用场景**：具体的业务场景（如"移动端首页"、"产品详情页"）
- **业务价值**：3个要点，说明为什么需要这个服务
- **核心能力**：3-5个技术能力点

### Architecture 章节

- **架构图**：使用ASCII绘制，展示主要组件和调用关系
- **数据流**：用箭头表示数据如何流转

### Core Modules 章节

- **按职责分组**：如召回/过滤/排序、或输入/处理/输出
- **基类说明**：模板方法模式的关键方法
- **实现类表格**：列出所有实现，便于快速查阅

### Dependencies 章节

- **内部依赖**：Gateway、Config等内部封装
- **外部依赖**：使用 `@ref:xxx-skill` 引用其他Skill
- **接口契约**：列出关键方法和参数

### Usage Patterns 章节

- **代码模板**：可直接复制使用的示例代码
- **配套修改**：列出需要同步修改的地方

### Pitfalls & Notes 章节

- **踩坑经验**：开发中遇到的问题和解决方案
- **注意事项**：框架约束、配置要求等

## 符号引用规范

### 类引用

- 完整类名：`com.example.service.UserService`
- 简短类名：`UserService`（同包或已导入时）

### 方法引用

- 类.方法：`UserService.getUser()`
- 带参数：`UserService.getUser(String id)`

### 语义描述（兜底）

在符号引用后添加语义描述，即使类名变化也能定位：

```markdown
**用户服务：** `UserService.getUser()` 
- 语义：根据用户ID获取用户信息，搜索关键词：用户、ID、查询
```

## 内容深度指南

### AI可自动生成（约70%）

- 代码结构和类层次
- 方法签名和参数
- 调用关系图
- 接口契约

### 需要人工补充（约30%）

- 业务背景和目标
- 设计决策的原因
- 踩坑经验
- 隐性约束和规则
