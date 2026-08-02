---
title: 可编辑海报 PSD 重建 Skill
type: playbook
created: 2026-06-15
updated: 2026-07-20
domain: 视觉制作
tags: [visual-production, ai-agent, skill, photoshop, psd, typography, ecommerce]
sources:
  - /Users/pechen/.codex/skills/editable-poster-psd-rebuild/SKILL.md
status: active
---

# 可编辑海报 PSD 重建 Skill

`editable-poster-psd-rebuild` 把一张已经扁平化的 AI 电商海报，重建成可以继续交给美工编辑的分层 PSD。

它不是把 JPG/PNG “另存为 PSD”，而是把海报拆成三类资产重新装配：

```text
无文案画面底图（像素层）
+ 原始完整海报（隐藏参考层）
+ 按原版式重建的文案（Photoshop 原生 type 文字层）
= 可继续编辑和交付的 PSD
```

核心目的有两个：一是让文字真正可编辑；二是把 AI 图片中来源不明的字体替换为用户指定或白名单字体，降低商业字体风险。

## Skill 定位

- Skill：`editable-poster-psd-rebuild`
- 当前实现：可分享的核心工作流 + 必需的 PSD 渲染适配器
- 当前已实现适配器：macOS + AppleScript + Adobe Photoshop
- 图像编辑能力：需要支持“以原海报为参考，只移除文字”的参考图编辑
- 最终结构验证：使用 `psd-tools` 读回 PSD，检查原生 `type` 层

这里把“方法”与“本机工具”分开：海报拆层、字体规划、版式协议和 QA 属于可移植核心；AppleScript、Photoshop 应用名和 Codex 图像编辑工具属于平台适配。

## 为什么这样设计

AI 图片里的文字同时带来三个问题：

1. 字符容易错，不能直接改文案。
2. 字体来源和授权状态通常不可追溯。
3. 文字与背景已经烘焙成像素，设计师不能调整字号、字距、位置和颜色。

因此不尝试识别并复刻 AI 的未知字体，而是让 AI 只负责“补回文字后面的背景像素”，再让 Photoshop 用确定字体生成原生文字层。高自由度的视觉修复交给参考图编辑模型；字体、坐标、图层和验收交给 JSON、脚本和 PSD 解析器这些确定性节点。

## 实现主线

### 1. 检查并抄录原图

读取画布尺寸，逐行确认文案、标点、换行、层级、颜色、位置、字号和字距。模糊字符不能静默猜测，必须标为待确认。

先写 `font-plan.json`，为每个文字角色记录：

- 选用字体；
- 来源是用户指定还是白名单；
- Photoshop PostScript 名称；
- 是否存在低置信度或阻塞。

### 2. 生成无文案底图

把原始海报直接作为参考图，只要求模型移除文字并补回文字遮挡区域。提示词不复述产品结构，而是锁定参考关系：所有非文字内容、结构、比例、位置、材质、颜色、光影和连接关系跟随原图，不新增文字、标记、部件或界面元素。

生成后必须检查：

- 尺寸和比例没有变化；
- 文案已清除；
- 产品、人物、家具、背景和光影没有被重画或移动；
- 文字后面的补图区没有明显破绽。

用户已经提供无字底图时也不能跳过这一门禁。可用闪烁对比、差分图，以及在文字移除遮罩之外计算的 SSIM/RMSE 辅助判断；数值阈值必须连同遮罩和图片编码条件记录，不能把单一阈值当成所有图片的真理。遮罩外出现可见语义、结构或位置变化就必须停止，不能先构建再把它当成合格交付。

如果失败，只收紧参考锁并重新编辑，不用长篇产品描述强迫模型重构。

### 3. 把版式写成数据

用 `layout-spec.json` 描述 PSD，而不是把坐标硬编码在临时脚本里。核心字段包括：

```json
{
  "background_path": "./background-no-text.png",
  "reference_path": "./original-reference-resized.png",
  "psd_path": "./output/editable-poster-rebuild.psd",
  "preview_path": "./output/editable-poster-rebuild-preview.png",
  "reference_opacity": 45,
  "reference_visible": false,
  "text_layers": [
    {
      "name": "headline line 1",
      "text": "示例标题",
      "x": 80,
      "y": 360,
      "size": 84,
      "color": "#574E45",
      "tracking": 80,
      "font_role": "chinese_main_headline",
      "font_candidates": ["SourceHanSerifCN-Regular"]
    }
  ]
}
```

每一条视觉行或同样式短文本单独成为一个文字层。`x/y` 使用像素坐标；当前 Photoshop 适配器创建的是点文本，`y` 对应基线位置。

脚本先做静态预检：输入路径、输出扩展名、参考层透明度、文字层名称唯一性、字号、字体候选等有问题时，不启动 Photoshop。

### 4. 用 Photoshop 原生能力组装 PSD

`build_editable_poster_psd.py` 完成两段工作：

1. Python 读取 `layout-spec.json`，校验字段并生成 Photoshop ExtendScript（JSX）。
2. macOS 用 `osascript` 控制 Photoshop 执行 JSX。

JSX 的实际动作是：

1. 打开无文案底图，把它作为基础像素层；
2. 打开原始完整海报，检查它与底图尺寸一致；
3. 将原图复制进 PSD，设为隐藏、约 45% 透明度的参考层；
4. 为每条文案创建 `LayerKind.TEXT` 原生文字层；
5. 写入文字、基线坐标、字号、RGB 颜色、字距和 PostScript 字体名；
6. 写入字体后再次读取字体名，发现 Photoshop 静默替换就报错；
7. 保存带图层 PSD，并由 Photoshop 自己导出 PNG 预览。

所以“PSD 重建”本质上是：AI 负责像素修复，JSON 负责描述版式，Photoshop 负责原生图层落地，解析器负责结构验收。

### 5. 双重验收

结构验收运行 `verify_psd_layers.py`：

- 文字层数量必须与 `layout-spec.json` 完全一致；
- 必须存在无文案背景层；
- 必须存在且隐藏原始参考层；
- 参考层必须覆盖完整画布、位于 `(0, 0)`，透明度符合规格；
- 读取并报告每个文字层保存的实际字体名；
- 输出 `psd-layer-report.json` 作为证据。

视觉验收对比 Photoshop 导出的预览与原图：

- 文案和标点；
- 换行和层级；
- 位置、字号、字距、颜色；
- 是否溢出、遮挡或裁切；
- 非文字画面是否保持。

PSD 解析通过只证明“图层结构正确”，不能证明“版式视觉一致”；预览相似也不能证明文字可编辑，因此两种证据必须同时通过。

## 默认字体标准

用户没有指定字体时：

- 中文大标题：思源宋体 CN Regular / `SourceHanSerifCN-Regular`
- 中文辅助文案：思源黑体 CN Regular / `SourceHanSansCN-Regular`
- 英文眉题和英文注释：思源黑体 CN Regular / `SourceHanSansCN-Regular`
- 用户明确要求中黑时：`SourceHanSansCN-Medium`
- 英文品牌字、眉题、注释默认 Photoshop `tracking = 200`
- 中文字距按参考图逐层记录

字体文件位置不写进 Skill。执行时由目标机器检查字体是否能被 Photoshop 按 PostScript 名称实际应用；失败就停止，不静默换成系统字体。

## 关键失败分支

- 文案无法确认：暂停该层，回到抄录节点确认字符。
- 去字图改变产品或构图：拒绝结果，收紧参考锁，回到图像编辑节点。
- 用户提供的无字底图不合格：构建前停止；只有用户明确要求“结构草稿”时才可继续，并标记 `partial / visual QA failed`。
- 用户只要求部分文字：记录被省略文字，并将结果标记为“部分文字重建”，不能暗示整张海报已完成。
- 字体缺失或被替换：停止构建；只有 `font-plan.json` 已批准的候选才可继续尝试。
- Photoshop/AppleScript 不可用：标记缺少渲染适配器，不能声称 PSD 已完成。
- PSD 结构与预览结论不一致：同时保留两类证据，修复后回到双重验收。

每个异常分支都必须回到明确主线节点，不能在异常路径上直接宣布完成。

## 输出与完成标准

典型交付目录：

```text
background-no-text.png
original-reference-resized.png
font-plan.json
layout-spec.json
editable-poster-rebuild.psd
editable-poster-rebuild-preview.png
psd-layer-report.json
```

完成必须同时满足：

- 非文字画面保持参考图；
- 原始完整海报存在于 PSD 且默认隐藏；
- 原生文字层数量与规格完全一致；
- 所有字体已授权/批准且没有 fallback；
- Photoshop 预览通过版式对照；
- 三个审计文件 `font-plan.json`、`layout-spec.json`、`psd-layer-report.json` 齐全。

## Portable Skill Creator 验证口径

2026-07-20 整理后按 `portable-skill-creator` 重新检查：

- 目标画像：`shareable core + adapter-required`；
- 基础创建规范：系统 `skill-creator`；
- 平台隔离：Codex 参考图编辑映射和 macOS Photoshop 渲染映射放入独立 adapter reference；
- 路径策略：Skill 内资源全部使用相对路径，不固化作者本机字体和应用路径；
- 确定性节点：规格预检、JSX 生成、PSD 图层验证；
- 运行证据：格式校验、可移植性扫描、脚本代表性测试和干净上下文前向测试应分别记录，不能用静态扫描代替端到端出图。

本次实际验证证据：

- 系统 `quick_validate.py`：通过；
- `validate_portability.py --profile shareable`：7 个 Skill 文件，0 error、0 warning、0 suppression；
- 本机适配器：macOS + Adobe Photoshop 2025，于 2026-07-20 实际生成并读回 PSD；
- 正向干净上下文：输入有效原图/无字底图，生成 973×1616 PSD，2/2 个原生文字层、隐藏满画布参考层 45.1%、实际字体名和 Photoshop 预览全部通过；
- 异常干净上下文：输入不合格无字底图，遮罩外 51.356% 像素存在明显差异，Skill 正确在 Step 2 停止且没有生成 PSD；
- 未实测范围：其他 Agent 的工具映射、Windows Photoshop 或其他 PSD 渲染器，因此只能声明核心规范兼容，不能声称这些平台已测试。

## 与其他页面关系

- [[domains/视觉制作/03-AI商业视觉/02-Codex与Photoshop协作自动化能力边界|Codex 与 Photoshop 协作自动化能力边界]]：Photoshop、OCR、PSD 检查和导出的底层能力边界。
- [[domains/AI Agent工程/03-Skill设计/04-可分享跨Agent Skill创建方法|可分享跨 Agent Skill 创建方法]]：可分享核心、隐私清理和平台适配方法。
- [[domains/AI Agent工程/03-Skill设计/03-主对话与干净子Agent的Skill回归测试方法|主对话与干净子 Agent 的 Skill 回归测试方法]]：前向回归与 `partial-pass` 红线。
- [[domains/视觉制作/03-AI商业视觉/01-AI在商业视觉设计中的应用方法与实践/04-图片工作流：提示词结构与参考控制|图片工作流：提示词结构与参考控制]]：参考图锁定和图像编辑方法。
