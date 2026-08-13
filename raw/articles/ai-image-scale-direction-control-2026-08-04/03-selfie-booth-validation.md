# 自拍机新场景：比例与朝向方法论回归

日期：2026-08-04  
输出：`generated.png`（1672×941，16:9）  
对照：`reference-effect.png`（仅用于生成后比较，没有作为生成输入）

## 生成输入

只使用两张参考图：

1. `generated_1785217655_0 (1).jpg`：场景、机位、自拍机、地面和空间透视。
2. `1785204773406_821313ef.png`：鞋子身份的唯一事实来源。

## 使用的 Prompt

```text
Use case: ads-marketing
Asset type: photorealistic video keyframe.
Output format: exact 16:9 horizontal landscape composition.

Primary request:
Create a new photorealistic image based on the supplied rooftop selfie-booth scene. A single pair of the reference shoes is walking by itself from the left side of the image toward the entrance of the selfie booth. No person or body parts appear.

Strict reference roles:
1) The scene image controls the entire scene: fixed frontal camera, 16:9 framing, rooftop ground plane, skyline, central selfie machine, doorway, architecture, daylight, spatial geometry and perspective. Preserve the selfie machine as the visual destination.
2) The product image is the ONLY source of product identity. All visible product structure, proportions, component positions, materials, colors, markings and connection relationships must follow this reference. Do not add, remove, move, reinterpret or redesign product components.

Scale-control stack:
- The selfie-machine doorway is the real-world scale anchor: its opening is tall enough for an adult to enter while standing upright without bending or lowering the head.
- Place the shoes on the same continuous rooftop ground plane immediately to the left-front of the booth, at approximately the same depth as the booth entrance.
- Each shoe is ordinary wearable footwear; its heel-to-toe length is approximately one seventh of the visible doorway height at that depth plane.
- Keep the complete shoe pair inside a compact lower-left subject zone centered near x=28%, y=76%. The combined pair occupies about 15–18% of the image width and no more than 11% of the image height.
- The selfie booth remains much larger than the shoes and remains the dominant central object. Preserve abundant ground and skyline around them.

Orientation-control stack:
- Define screen coordinates: +x is from 9 o'clock to 3 o'clock, left→right, shown conceptually as →.
- Both shoes travel along +x toward the booth entrance. For each shoe, the heel→toe intrinsic axis points to screen-right; toe tips are at 3 o'clock and heels at 9 o'clock.
- Keep each heel-to-toe centerline within ±5 degrees of image horizontal.
- Show clear outer-side profiles so the travel direction is unambiguous; do not show toe-front views aimed at the camera.
- The right-side shoe is the leading shoe, closer to the entrance, grounded and weight-bearing.
- The left-side shoe trails by one natural stride, with a slight heel lift and a very small realistic air gap.
- The two shoes are consecutive phases of one walking motion, not a symmetric retail display pair.

Camera and realism:
Match the reference scene's frontal viewpoint, daylight, ground perspective, soft shadows and clean architectural photography. Add realistic contact shadows beneath the shoes. Keep the pair fully visible and physically grounded.

Priority if constraints compete:
product identity > 9-to-3 orientation > doorway-based physical scale > left-of-booth placement > gait detail > style.

Avoid:
people, legs, feet inside the shoes, trousers, human shadows, extra shoes, duplicated products, giant shoes, hero close-up, shoes touching the booth, shoes larger than the doorway scale permits, toes facing the camera, diagonal or vertical shoe axes, symmetric catalog pose, high floating, new product parts, added accessories, interface-like elements, watermark.
```

## 与效果图比较

| 检查项 | 结果 | 说明 |
|---|---|---|
| 16:9 画幅 | 通过 | 输出 1672×941，比例约 1.7779 |
| 场景/机位 | 通过 | 自拍机居中、正面机位、天际线和地面关系均保持 |
| 只出现一双鞋 | 通过 | 两只鞋，无人物或人体部位 |
| 9 点→3 点方向 | 通过 | 两只鞋鞋跟在左、鞋头在右，主轴接近水平 |
| 走向自拍机 | 通过 | 鞋位于机器左侧，右侧鞋领先且指向入口 |
| 主体画面占位 | 通过 | 鞋组约占画面宽度 17%，效果图约 15%，非常接近 |
| 主体位置 | 基本通过 | 生成图鞋组略高、略靠近机器；效果图更靠左下 |
| 真实物理比例 | 部分通过 | 自拍机明显大于鞋，但“一只鞋长≈门高 1/7”没有被严格执行，鞋相对门洞仍偏大 |
| 行走步态 | 部分通过 | 前后位置正确，但两只鞋都较平稳落地，后鞋抬跟和自然步幅不够明显 |
| 产品身份 | 基本通过 | 鞋型、颜色、材质关系较好；动作生成仍可能造成局部细节简化 |

## 方法论结论

这次换场景后，方法仍然有效，但有效范围更明确：

1. **方向控制可以跨场景迁移。** `画布 +x`、主体 `后端→前端` 轴、水平角度和指定可见面组合后，方向稳定命中。
2. **画面占位控制可以迁移。** `x/y 区域 + 组宽/组高 + 环境留白` 将鞋组放到了与效果图接近的位置和画面尺寸。
3. **常识尺度锚点只能改善合理性，不能保证严格换算。** “成年门洞约 2 米、鞋约门高 1/7”没有被精确执行；模型更服从整体构图占位。
4. **动作方向比动作相位稳定。** 模型理解了“向右走”，但没有充分执行“后鞋轻微离地”。
5. 生产模板应继续保留两套尺度描述：
   - 物理关系用于避免灾难性巨物；
   - 画布占位用于控制最终构图。

本轮结论支持此前的方法论，但不能把物理比例提示词称为硬约束。

