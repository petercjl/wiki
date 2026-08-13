# Formal Page Plan

## Source Understanding

来源不是单个鞋子案例，而是一套经过两种场景验证的通用生图约束方法：用同平面尺度锚点、连续透视尺度链、画布占位保险控制比例；用画布坐标、主体自身轴、环境线、指定可见面和动作角色分解控制朝向；同时明确提示词、真实构图参考和确定性工具的能力边界。

## Existing Memory Search

- `04-图片工作流：提示词结构与参考控制.md` 已有产品身份参考锁定和通用图片工作流，但没有本来源的比例/朝向控制栈和实验边界。
- `07-故事板铁三角AI视频控制法.md` 说明故事板箭头、身份板和场景资产职责，可作为视频关键帧交叉链接。
- `14-AI品牌TVC的气质、视觉符号与产品登场.md` 已要求原始产品图作为唯一身份真值，可与本方法互证。

## Recommended Placement

- disposition: `create-new`
- proposed_path: `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md`
- proposed_type: `playbook`
- rationale: 本页回答的是 AI 图片/视频关键帧如何稳定落地构图的“制作方法”，属于视觉制作的 how；其跨电商、广告、角色与产品场景复用，不应塞进单个风格库或单个视频项目。

## Proposed Fusion And Routing

- 在 `domains/视觉制作/03-AI商业视觉/index.md` 新增入口。
- 在 `domains/视觉制作/index.md` 的关键工作流中新增入口。
- 在既有 `04-图片工作流：提示词结构与参考控制.md` 增加“比例与朝向专项方法”相关记忆链接，不重写旧页主体。
- 在 `domains/视觉制作/06-AI视频/04-图片与控制资产/07-故事板铁三角AI视频控制法.md` 增加关键帧构图控制交叉链接。
- 新建 `queries/AI生图主体比例与朝向控制.md`，服务“主体太大、方向不对、朝向镜头、构图比例失控、关键帧尺寸不准”等自然语言任务。
- 更新根 `index.md` 与 `log.md`。

## Alternative

- alternative: 放入 `domains/视觉制作/06-AI视频/`。
- rejection_reason: 生图方法本身跨图片和视频关键帧，主归属放 AI 视频会降低纯图片任务的检索率；更适合作为交叉链接。

## Confirmation

- status: confirmed
- user_confirmation: 确认推荐归位与交叉链接方案
- confirmation_evidence: 用户在 2026-08-04 收到具体归位提案后回复“确认”
- final_confirmed_path: `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md`
- query_entry: `queries/AI生图主体比例与朝向控制.md`
- no_formal_write_before_confirmation: true
