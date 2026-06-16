---
title: Codex 与 Photoshop 协作自动化能力边界
type: playbook
created: 2026-06-15
updated: 2026-06-15
domain: 视觉制作
tags: [visual-production, photoshop, codex, automation, ocr, psd, toolchain]
sources:
  - raw/articles/codex-photoshop-toolkit-validation-2026-06-15.md
status: active
---

# Codex 与 Photoshop 协作自动化能力边界

这页记录的是 Peter 当前本机环境下，Codex 与 Photoshop 协作做电商视觉生产时的真实能力边界。它不是“理论上 Photoshop 能做什么”，而是“Codex 当前能稳定调度什么”。

## 最终判断

Codex 适合作为 Photoshop 的脚本编排器和批处理控制器，稳定执行 PSD 结构化编辑、图层操作、文字替换、图片置入、OCR 坐标提取和导出检查。

Codex 不应默认承担高质量 OCR、复杂背景去字、生成式修复这类视觉语义任务。OCR 可以用 Apple Vision 辅助；复杂去字需要 Photoshop 人工修复、预制干净模板，或后续接入 IOPaint/LaMa 这类 inpainting 工具。

## 当前工具栈

当前可用工具分四层：

| 层级 | 工具 | 作用 |
| --- | --- | --- |
| Photoshop 控制 | JSX + AppleScript bridge | 打开/新建文档、图层操作、文字层、保存 PSD、导出图 |
| OCR 与坐标 | Apple Vision OCR CLI、Tesseract | 识别图中文字，输出文字和像素坐标 |
| 图像处理与检查 | ImageMagick、ExifTool、OpenCV、Pillow、scikit-image | 读图、预处理、mask、尺寸和元数据检查 |
| PSD 外部检查 | psd-tools | 在 Photoshop 外读取 PSD 结构，做验证和调试 |

工具入口：

```text
/Users/pechen/AI/Research/codex-ps-toolkit/
```

核心命令：

```bash
/Users/pechen/AI/Research/codex-ps-toolkit/bin/run_jsx.sh /absolute/path/to/job.jsx
/Users/pechen/AI/Research/codex-ps-toolkit/bin/vision_ocr /path/to/image.png --lang zh-Hans,en-US
/Users/pechen/AI/Research/codex-ps-toolkit/bin/check_env.sh
```

## 已验证稳定能力

Photoshop probe 在 2026-06-15 复测结果为 11/12 通过。

已验证稳定：

- 启动和激活 Photoshop。
- 通过 AppleScript 把 JSX 源码字符串交给 Photoshop 执行。
- 新建 RGB 文档。
- 打开外部 PNG。
- 创建普通像素图层。
- 创建选择区。
- 对选择区做纯色填充。
- 创建可编辑文字图层，并设置内容、位置、字号、颜色。
- 复制、隐藏、重命名、尝试锁定图层。
- 保存带图层 PSD。
- 导出 PNG / JPEG。
- 置入外部图片为图层或智能对象。
- 使用 `psd-tools` 在 Photoshop 外检查 PSD 图层结构。

稳定调用方式是先让 Codex 读取 JSX 文件为 UTF-8 文本，再执行：

```applescript
tell application id "com.adobe.Photoshop"
  activate
  do javascript jsCode
end tell
```

不要优先使用：

```applescript
do javascript (POSIX file "/path/to/script.jsx" as alias)
```

本机 Photoshop 2025 对直接传 JSX 文件 alias 的方式返回过通用错误 `8800`。

## OCR 结论

Apple Vision OCR 是当前最适合做图中文字层提取的默认工具。它能输出识别文本和像素坐标，适合后续自动生成 Photoshop 文字层。

样图 `/Users/pechen/Downloads/generated_1781366886467_a47c4d86.png` 的 Apple Vision OCR 结果：

```text
SHANJU 杉居
SILICONE HEAT PAD
热锅落地
台面安心
铂金硅胶 耐高温不伤桌
一日三餐 杉居相伴
```

Tesseract 可作为补充工具，适合局部 OCR、脚本化批处理和多语言兜底。但在大字号中文艺术字、版式化海报中，Tesseract 容易产生噪声；不要把它当最终排版真值。

## 失败边界

当前明确失败或不稳定：

| 能力 | 状态 | 边界说明 |
| --- | --- | --- |
| 无 UI 内容识别填充 | 失败/不稳定 | Photoshop Action Descriptor 调用未稳定通过，不能作为默认去字能力 |
| 自动完美去除烘焙文字 | 不可靠 | OCR 能定位文字，但背景修复需要 inpainting 或人工修复 |
| UXP Developer Tools | 暂停 | 已安装但登录状态异常；不是当前刚需 |
| Alchemist | 未安装 | 需要 UXP Developer Tools 或 `.ccx` 安装流程；后续需要录 batchPlay 时再处理 |
| IOPaint/LaMa | 未安装 | 是去字/修复增强项，依赖模型和 PyTorch，暂不作为基础环境 |

## 工作流模板：从成品图恢复可编辑文字

目标是从一张只有成品图的电商图中，恢复“干净底图 + 可编辑文字层 + 原图备份”。

合理三层结构：

1. `Original image backup`
   - 原图完整保留。
   - 默认隐藏或锁定。

2. `Clean image`
   - 去掉烘焙文字后的干净底图。
   - 这是最难、最不稳定的步骤。

3. `Editable text`
   - 每行或每组同字体同颜色文字作为可编辑文字层。
   - 由 Apple Vision OCR 坐标和人工/模型判断的字体样式生成。

可自动化部分：

- OCR 提取文字和坐标。
- 根据坐标生成 Photoshop 文字层。
- 保留原图备份层。
- 保存 PSD。
- 导出预览图并检查。

不应默认自动化承诺的部分：

- 复杂背景无痕去字。
- 字体完全匹配。
- 生成式填充/内容识别填充的无 UI 稳定调用。

## 工作流模板：PSD 模板批量生产

这是当前最稳的使用方式。

1. 人工或设计师先做一个干净 PSD 模板。
2. 模板中保留：
   - 产品智能对象。
   - 文案文字层。
   - 背景层。
   - 尺寸/平台导出规范。
3. Codex 读取结构化输入，如 SKU、图片路径、文案、价格、卖点。
4. Codex 调用 Photoshop JSX：
   - 替换智能对象或置入图片。
   - 修改文字图层内容。
   - 调整图层可见性。
   - 批量导出 PNG/JPEG。
5. 用 ImageMagick / psd-tools / OCR 做输出验证。

这个工作流比“成品图反向拆 PSD”稳定得多，也更适合电商批量图生产。

## 何时需要后续工具

### 需要 Alchemist / UXP

当任务需要把 Photoshop 菜单命令、滤镜、复杂命令录成可复用 action/batchPlay，而 JSX DOM 没有稳定 API 时，再处理 UXP Developer Tools 和 Alchemist。

典型场景：

- 某个菜单操作只有 UI，没有 DOM API。
- 需要录制 Photoshop 实际执行出的 Action Descriptor。
- 需要长期开发 Photoshop 面板插件。

### 需要 IOPaint/LaMa

当任务变成“只有成品图，需要批量自动去除烘焙文字并补背景”时，再安装 IOPaint/LaMa。

典型场景：

- 批量从竞品图或生成图中擦掉文字。
- 用 OCR mask 自动去字。
- 需要在 Photoshop 外批处理背景修复。

边界：

- CPU 上可能慢。
- 复杂背景不保证完美。
- 仍需要导出预览和人工抽检。

## Agent 使用规则

当 Peter 要求 Codex 控制 Photoshop 时，先判断任务类型：

| 用户任务 | 推荐路径 |
| --- | --- |
| 修改 PSD 文案/图层/导出 | 直接用 JSX bridge |
| 从图中提取文字坐标 | 优先 Apple Vision OCR |
| 从成品图恢复可编辑文字层 | OCR + Photoshop 文字层，去字部分单独确认 |
| 批量生成电商图 | PSD 模板化 + JSX bridge |
| 复杂背景去字 | 不承诺 JSX；考虑人工 PS、IOPaint/LaMa 或生成式修复 |
| 录制不可脚本化 PS 命令 | 后续处理 UXP Developer Tools + Alchemist |

不要把 Photoshop 当作 OCR 或智能修图模型。Photoshop 是强大的编辑器和渲染器；Codex 当前最擅长调度确定性的图层和文件工作流。

## 相关记忆

- [[domains/视觉制作/03-AI商业视觉/01-AI在商业视觉设计中的应用方法与实践/04-图片工作流：提示词结构与参考控制|图片工作流：提示词结构与参考控制]]
- [[domains/视觉制作/03-AI商业视觉/01-AI在商业视觉设计中的应用方法与实践/06-定制视觉智能体与团队重构|定制视觉智能体与团队重构]]
- [[domains/AI Agent工程/index|AI Agent 工程知识域]]
