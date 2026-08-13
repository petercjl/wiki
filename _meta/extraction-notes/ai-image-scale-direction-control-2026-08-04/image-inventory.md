# Image Inventory

| image_id | source_location | archived_path | image_class | semantic_anchor | target_pages | status | reason_or_notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IMG01 | shoe identity reference | `raw/assets/ai-image-scale-direction-control-2026-08-04/01-shoe-identity-reference.jpg` | evidence | 原始身份图的知识作用：主体细节由图像参考携带，Prompt 只写锁定关系，避免用文字重绘产品。 | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | 已嵌入参考职责章节 |
| IMG02 | crosswalk scene reference | `raw/assets/ai-image-scale-direction-control-2026-08-04/02-crosswalk-scene-reference.png` | evidence | 街景参考提供机位和环境线；产品身份和最终光色不从这张图推断。 | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | 已嵌入参考职责章节 |
| IMG03 | style reference | `raw/assets/ai-image-scale-direction-control-2026-08-04/03-style-reference.png` | evidence | 风格板只承担暖金光与冷灰阴影，不承担主体结构或构图 |  | raw-only | 风格本身不是比例与朝向结论，原图保留供审计 |
| IMG04 | crosswalk target effect | `raw/assets/ai-image-scale-direction-control-2026-08-04/04-crosswalk-target-effect.png` | knowledge | 真实构图参考把主体尺度、位置、环境留白和透视关系同时可视化，比孤立百分比更容易被模型执行。 | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | 已嵌入比例控制章节 |
| IMG05 | variant A | `raw/assets/ai-image-scale-direction-control-2026-08-04/05-variant-a-physical-anchors.png` | evidence | 物理参照链能锁方向和步态，但主体仍偏大 |  | raw-only | 结论已由 IMG06 与 IMG08 的更清晰对照覆盖，原图保留 |
| IMG06 | variant B | `raw/assets/ai-image-scale-direction-control-2026-08-04/06-variant-b-canvas-coordinates.png` | knowledge | 方案 B：方向正确，主体尺度和环境留白在第一轮中最接近目标构图。 | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | 已嵌入比例控制章节 |
| IMG07 | variant C | `raw/assets/ai-image-scale-direction-control-2026-08-04/07-variant-c-reference-hierarchy.png` | evidence | 严格参考职责能稳定方向，但不等于逐像素复制 |  | raw-only | 与 IMG06 的成功结论重复，原图保留供审计 |
| IMG08 | variant D | `raw/assets/ai-image-scale-direction-control-2026-08-04/08-variant-d-no-target-reference.png` | knowledge | 方案 D 反证：文字里的百分比不是硬包围盒，广告主角放大先验仍会覆盖它。 | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | 已作为关键反证嵌入 |
| IMG09 | variant E | `raw/assets/ai-image-scale-direction-control-2026-08-04/09-variant-e-layout-control.png` | knowledge | 方案 E 反证：抽象图能帮助控制大致位置，但没有阻止主体被放大。 | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | 已作为抽象控制图反证嵌入 |
| IMG10 | selfie booth scene | `raw/assets/ai-image-scale-direction-control-2026-08-04/10-selfie-booth-scene-reference.jpg` | evidence | 第二轮场景图同时提供固定正面机位、地面平面和成年门洞尺度锚点。 | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | 已嵌入跨场景回归章节 |
| IMG11 | selfie booth shoe identity | `raw/assets/ai-image-scale-direction-control-2026-08-04/11-selfie-booth-shoe-identity.png` | evidence | 第二场景仍以原始鞋图作为唯一产品身份来源 |  | raw-only | 身份参考规则已由 IMG01 说明，本图完整保留供审计 |
| IMG12 | selfie booth target effect | `raw/assets/ai-image-scale-direction-control-2026-08-04/12-selfie-booth-target-effect.png` | knowledge | 效果图只用于生成后比较：鞋组约占画宽 15%，右侧鞋领先并朝入口。 | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | 已嵌入跨场景回归章节 |
| IMG13 | selfie booth generated | `raw/assets/ai-image-scale-direction-control-2026-08-04/13-selfie-booth-generated.png` | knowledge | 跨场景回归：16:9、自拍机居中、鞋组左下、9→3 点方向和无人物均命中；鞋组约占画宽 17%，但鞋长≈门高 1/7 与后鞋抬跟没有严格执行。 | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | 已嵌入跨场景回归章节 |
