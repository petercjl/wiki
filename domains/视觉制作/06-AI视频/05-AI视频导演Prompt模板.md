---
title: AI视频导演Prompt模板
type: playbook
created: 2026-06-27
updated: 2026-06-27
domain: 视觉制作
tags: [visual-production, ai-video, prompt-engineering, playbook]
sources:
  - raw/books/film-directing-shot-by-shot-2019/source.epub
  - _meta/extraction-notes/film-directing-shot-by-shot-2019/coverage-matrix.md
  - https://help.runwayml.com/hc/en-us/articles/47313504791059-Camera-Terms-Prompts-Examples
  - https://kling.ai/blog/ai-camera-control-movement-prompts-guide
  - https://www.eachlabs.ai/blog/a-guide-to-camera-movements-for-ai-video-generation
  - https://letsenhance.io/blog/all/ai-video-camera-movements/
  - https://arxiv.org/abs/2505.15145
  - https://arxiv.org/abs/2506.21356
status: active
---

# AI视频导演Prompt模板

AI 视频 prompt 的目标不是把电影术语堆满，而是把 [[domains/视觉制作/06-AI视频/03-导演式镜头设计方法|导演式镜头设计方法]] 中的镜头决策，翻译成模型容易执行的短句。

## 核心公式

```text
镜头任务 + 主体 + 场景 + 景别 + 机位 + 构图 + 主动作 + 单一运镜 + 光线/色彩 + 焦段/景深 + 时长 + 限制
```

推荐先写中文导演表，再写英文生成 prompt。中文负责思考，英文负责执行。

## 中文导演表

```text
镜头编号：
故事节点：
镜头任务：
镜头提出的问题：
镜头给出的答案：
观众感知：
主体：
场景/时间：
景别：
机位：
构图：
人物动作：
产品动作：
镜头运动：
运动速度：
光线/色彩：
焦段/景深：
画面质感：
时长：
前后衔接：
备用 coverage：
负向限制：
```

## Katz 补充：故事板标注怎么转 prompt

传统故事板不能真正播放运动，所以 Katz 书中反复使用箭头、边注、画框内画框、俯视示意图和转场间隔来说明运动。AI 视频可以直接把这些标注翻译成 prompt 字段。

| 故事板标注 | 它说明什么 | prompt 字段 |
| --- | --- | --- |
| 箭头 | 人物、物件或镜头运动方向 | `main action`, `camera movement`, `direction` |
| frame within frame | 推近、拉远、变焦、取景变化或 field cut | `slow dolly push in`, `slow pull back`, `do not zoom unless intended` |
| 俯视平面图 | 人物站位、轴线、相机路径 | `camera follows from behind`, `lateral tracking`, `subject moves left to right` |
| 多个同主体位置 | 一个镜头内的连续动作 | `the subject crosses from foreground left to background right in one continuous motion` |
| 面板间空白/说明 | dissolve、fade、cut、match action | `straight cut`, `soft dissolve`, `match on action`，或交给剪辑备注 |
| 旁注/对白 cue | 剪辑点、动作点、反应点 | `cut after she turns her head`, `hold for one second after action` |

AI prompt 不一定要写所有故事板信息。首帧/参考图已经锁定画面时，prompt 应减少构图描述，集中写动作、速度、方向和限制。

## 英文 Prompt 骨架

```text
[shot size], [camera angle], [composition].
[subject] in [scene], [time of day].
[main action].
[camera movement], [speed and direction].
[lighting and color mood], [lens/depth of field].
[commercial/cinematic realism].
Avoid [failure modes].
```

示例：

```text
Medium close-up, eye-level camera, rule-of-thirds composition.
A high-end professional woman stands beside a floor-to-ceiling window in a modern apartment at dusk, the city skyline softly blurred behind her.
She holds a smartphone quietly and looks outside, calm but slightly tired.
Slow dolly push in, very subtle and steady.
Soft mixed lighting, warm interior practical lights against blue-orange dusk, shallow depth of field, realistic premium commercial cinematography.
Avoid exaggerated acting, fast camera motion, distorted hands, and obvious product close-up.
```

## 字段写法

### 镜头任务

中文先写，英文 prompt 中可以不直译，但必须影响画面选择。

```text
建立高端都市世界
表现职场压力后的克制疲惫
从职业身份过渡到家庭身份
让手机作为保存亲子瞬间的动作自然出现
用产品画面收束“记忆保存”命题
```

### 景别

```text
extreme wide shot
wide shot
medium wide shot
medium shot
medium close-up
close-up
extreme close-up
macro close-up
insert shot
POV shot
over-the-shoulder shot
```

### 机位

```text
eye-level camera
low-angle camera
high-angle camera
side profile view
rear view
over-the-shoulder angle
top-down angle
subjective POV
```

### 构图

```text
rule-of-thirds composition
centered composition
symmetrical composition
frame-within-a-frame composition
foreground occlusion
negative space
leading lines
shallow depth of field
deep focus
```

### 运镜

```text
static locked-off shot
slow dolly push in
slow dolly pull back
smooth tracking shot following the subject
lateral tracking shot from left to right
gentle pan left
gentle tilt down
subtle handheld camera
slow crane up
```

AI 视频里优先使用 `slow / subtle / steady / gentle`。除非做动作片或概念片，否则不要用 fast、dramatic、dynamic 这类容易让模型过度发挥的词。

### 光线和色彩

```text
soft natural window light
warm interior practical lights
blue-orange dusk light
cool office lighting
low-key cinematic lighting
high-key clean commercial lighting
soft backlight and rim light
muted premium color palette
warm family atmosphere
```

### 负向限制

```text
Avoid fast camera motion.
Avoid exaggerated acting.
Avoid distorted hands.
Avoid deformed product details.
Avoid text, logos, watermarks, or UI glitches unless specified.
Avoid sudden scene changes.
Avoid multiple camera movements in one shot.
Keep the subject identity consistent.
Keep the product shape accurate.
```

## 单镜头 Prompt 模板

```text
中文导演表：
镜头任务：
主体：
场景：
景别：
机位：
人物动作：
产品动作：
镜头运动：
光线/色彩：
前后衔接：
限制：

英文生成 prompt：
[shot size], [camera angle], [composition].
[subject] in [scene].
[action].
[camera movement].
[lighting/color/lens].
Avoid [failure modes].
```

## 多镜头分镜模板

```text
项目命题：
产品价值：
人物小传：
视觉基调：
空间/轴线规则：
核心镜头问题：
核心镜头答案：

镜头 01
任务：
问题/答案：
画面：
景别/机位：
运镜：
时长：
衔接：
coverage 备选：
prompt：

镜头 02
任务：
问题/答案：
画面：
景别/机位：
运镜：
时长：
衔接：
coverage 备选：
prompt：
```

## OPPO 风格示例：职业到家庭的情绪转场

### 镜头 1：城市建立

```text
Wide establishing shot, static locked-off camera.
A high-rise apartment balcony overlooking a dense modern city skyline at dusk, blue-orange sunset reflected on glass towers.
No people visible, quiet premium urban atmosphere.
Soft dusk light, muted colors, realistic high-end smartphone commercial cinematography.
Avoid fast motion, oversaturated colors, and fantasy city details.
```

### 镜头 2：人物独处

```text
Medium close-up, side profile view, rule-of-thirds composition.
A high-end professional woman in a black turtleneck stands near a floor-to-ceiling window after work, holding a smartphone loosely in one hand.
She looks outside quietly, calm but slightly tired.
Very slow dolly push in.
Cool city light mixed with warm interior light, shallow depth of field, realistic premium commercial style.
Avoid exaggerated facial expression and obvious product posing.
```

### 镜头 3：家庭关系

```text
Medium wide shot, eye-level camera, warm family composition.
The same woman sits on a living room rug with two children drawing and building wooden blocks beside her, city dusk visible through the window.
She watches them with a soft smile, relaxed after a long day.
Static camera with only gentle natural body movement.
Warm practical lights, cozy interior, shallow depth of field, realistic lifestyle commercial cinematography.
Avoid chaotic child movement, distorted hands, and toy deformation.
```

### 镜头 4：产品动作

```text
POV insert shot, close-up of hands holding a premium smartphone camera interface.
The phone frames the children drawing on the living room rug in warm evening light.
The thumb gently taps the shutter button.
Static camera, sharp phone foreground with softly blurred family scene beyond.
Realistic smartphone screen perspective, warm family light.
Avoid fake UI text, distorted fingers, unreadable interface, and sudden zoom.
```

## 模型执行规则

- 文生视频：prompt 要更完整，场景、主体、动作和运镜都要写清楚。
- 图生视频：图片已经锁定构图，prompt 应该少改画面，多写动作、运镜和限制。
- 首尾帧：适合明确转场和运动目标，但单镜头动作不要太复杂。
- 产品视频：产品外观要靠参考图和首帧控制，不要只靠文字。
- 人物一致性：先做人物设定图，再用同一人物参考生成分镜。
- 移动镜头：必须写出运动任务，不能只写 cinematic movement。
- 对话/关系镜头：记录人物站位、视线方向和轴线，避免正反方向混乱。
- 剪辑镜头：提前标注是 cut on action、reaction shot、insert shot 还是 establishing shot。

## 检查清单

- 是否只指定一个主要运镜？
- 是否有明确景别和机位？
- 是否写了人物动作，而不是只写人物状态？
- 是否写了产品动作，而不是只写产品名称？
- 是否写了光线和色彩服务情绪？
- 是否写了模型容易犯错的限制？
- 中文导演表和英文 prompt 是否一致？

## 相关记忆

- [[domains/视觉制作/06-AI视频/20-导演知识系统/index|AI视频导演知识系统]]
- [[domains/视觉制作/06-AI视频/03-导演式镜头设计方法|导演式镜头设计方法]]
- [[domains/视觉制作/06-AI视频/04-商业短视频摄影与运镜语法|商业短视频摄影与运镜语法]]
- [[domains/视觉制作/06-AI视频/01-Doubao-Seedance-2.0视频生成模型卡|Doubao-Seedance-2.0 视频生成模型卡]]
- [[domains/视觉制作/06-AI视频/90-案例库/01-OPPO-Find-X9-Ultra：把影像能力翻译成记忆保存|OPPO Find X9 Ultra：高价影像手机的记忆保存广告]]
