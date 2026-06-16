---
title: Codex-Photoshop 协作工具链验证记录
type: source-summary
created: 2026-06-15
updated: 2026-06-15
domain: 视觉制作
tags: [visual-production, photoshop, codex, automation, ocr, toolchain]
status: raw
---

# Codex-Photoshop 协作工具链验证记录

## 来源

本记录来自 2026-06-15 在 `/Users/pechen/AI/Research` 工作区完成的本机工具链搭建与验证。

主要本地文件：

- `/Users/pechen/AI/Research/codex_photoshop_control_research.md`
- `/Users/pechen/AI/Research/codex-ps-toolkit/docs/environment.md`
- `/Users/pechen/AI/Research/codex-ps-toolkit/work/output/validation-2026-06-15/`

## 环境

- macOS + Codex Desktop
- Adobe Photoshop 2025
- Photoshop bundle id: `com.adobe.Photoshop`
- Photoshop version: `26.11.0`

已安装并验证：

- `tesseract` 5.5.2
- `tesseract-lang`，包含 `chi_sim`、`chi_tra`、`eng`、`jpn`、`osd`
- `imagemagick` 7.1.2-18
- `exiftool` 13.50
- Python 3.12.13 本地环境：`/Users/pechen/AI/Research/ps-codex-env`
- Python 包：`pillow`、`numpy`、`opencv-python-headless`、`pytesseract`、`psd-tools`、`scikit-image`
- Apple Vision OCR CLI：`/Users/pechen/AI/Research/codex-ps-toolkit/bin/vision_ocr`

未启用：

- Adobe UXP Developer Tools：已安装但登录状态异常，暂时跳过。
- Alchemist：未安装。
- IOPaint/LaMa：未安装。

## 验证摘要

增强后验证目录：

```text
/Users/pechen/AI/Research/codex-ps-toolkit/work/output/validation-2026-06-15
```

Photoshop probe:

```text
photoshop_probe_pass 11 of 12
photoshop_probe_fail 1
FAIL 09 content aware fill via legacy action descriptor
```

Apple Vision OCR 对样图识别结果：

```text
vision_ocr_lines 6
SHANJU 杉居
SILICONE HEAT PAD
热锅落地
台面安心
铂金硅胶 耐高温不伤桌
一日三餐 杉居相伴
```

UPIA 插件状态：

```text
0 extension installed for Photoshop 2025 (ver 26.11.0)
0 extension installed for Others
```

PSD 工具验证：

```text
psd_size 640 420
layer 背景 pixel visible= True
layer raster fill layer pixel visible= True
layer editable text layer type visible= True
layer duplicated hidden locked text layer type visible= True
```

## 原始结论

Codex 可以稳定作为 Photoshop 的脚本编排器和批处理控制器，适合执行 PSD 结构化编辑、图层操作、文字替换、图片置入、OCR 坐标提取和导出验证。

当前最大能力缺口仍是高质量自动图像修复：无 UI 内容识别填充没有稳定通过；复杂背景去字不应默认由 JSX 脚本承担。
