<fragment mode="section" requested-start="doxcnINbZiE7MjDBCWFBSZeA9Ve">
# 二、资产构建：角色定调与场景搭建

## 一）角色设计

### 1、先了解 故事

很多同学一开始做 AI 角色设计时，习惯直接从“发型、发色、衣服、颜值”入手，结果是：图看上去还行，但换一集就认不出是同一个人。问题不在于工具，而在于 人物要符合故事情节 ：

> **先 故事 ，再 人物 。**

> 先回答“ 这是什么故事 ”，再去回答“他应该长什么样”。

因此在进入任何视觉设定之前，我们都建议为每个主要角色写一份简短的“人物小传”。它不必是文学化的长篇大论，反而更像是一个高度结构化的“角色数据表”。一个适合 AI 工作流的人物小传，至少应该包含以下几个模块：

- **身份与位置** ：

  - 所在世界观中的“职业 / 阶层 /阵营”：贫民、贵族、门派弟子、佣兵、猎人、学生军等；
  - 在故事中的“功能”：主角、女主、反派、大佬、门槛 NPC、搞笑担当、情绪锚点……
- **性格与反差点** ：

  - 3–5 个核心性格标签：冲动、谨慎、要强、自卑、嘴硬心软、恋战、怂却有底线……
  - 至少 1 个鲜明的 **反差点** ：外冷内热 / 打架猛但生活废 / 外表柔弱但很能扛 / 富二代却抠门等。 反差点是角色记忆点的重要来源，也可以直接转译为视觉符号（比如钢铁直男房间里摆满可爱玩偶）。
- **核心欲望与困境** ：

  - 角色“最想要什么”：被认可、活下去、复仇、赚钱、保护某人、证明自己不是废物……
  - 角色“现在卡在哪里”：资质差、出身低、身份敏感、被误会、身上有诅咒……
- **关系网络** ：

  - 这个角色与主角、反派、组织之间的三四个关键关系：
  
    - 青梅竹马但立场对立；
    - 表面师徒实则互相利用；
    - 名义上是上司，实则被手下带着飞……
- **视觉暗示** ：

  - 这一段不直接描述五官，而是描述与视觉相关的关键词：
  
    - “总是穿得一丝不苟，即使是在废墟里也系好领带”；
    - “喜欢戴帽子，见人就调整帽檐”；
    - “左手有明显的伤疤，从不露出来”；
    - “衣服永远有口袋，随时掏出小工具”。

这些信息一方面可以喂给大模型，让它帮我们扩写；另一方面，也是后续提炼 AI 绘画提示词的来源。只有当“人物功能—性格—关系—视觉符号”形成闭环时，一个角色才有机会从“好看”变成“有记忆点”。

### 2、男频与女频

AI 短剧 的很大一部分项目来自网文改编，不同赛道的受众，对“好看角色”的期待差异非常明显。

> **男频线角色**

> 关键词：力量感、爽感、等级压制、反杀翻盘。

> 视觉上更强调：

- 轮廓分明、线条干练、肢体张力大；
- 服装设计相对简洁，更像“战斗装备”；
- 动作常态偏“前倾”“向上”，随时准备冲出去。

> **女频线角色**

> 关键词：情绪、氛围、亲密关系、成长心路。

> 视觉上更强调：

- 眼睛、睫毛、嘴角微表情，细腻的神态变化；
- 服装更有层次与细节，饰品多用于暗示身份与情绪；
- 整体镜头更柔和，远景+近景切换节奏较慢。

男频和女频的内容核心爽点的区别。

| 维度 | 男频 (Male Frequency) | 女频 (Female Frequency) |
|-|-|-|
| 核心欲望 | 权力与征服 | 情感与被爱 |
| 关键词 | 升级、逆袭、热血、称霸、兄弟情、复仇 | 虐恋、甜宠、成长、氛围、CP感、救赎 |
| 故事逻辑 | 解决问题：打怪升级，从废柴变最强。 | 体验情感：在复杂的关系中纠葛，确认自我价值。 |
| 对主角期待 | 代入感：希望他能做到我做不到的事（如一人敌千军）。 | 共情：希望她能经历我渴望的感情（如被偏爱、被守护）。 |

在写人物小传、AI绘画提示词时，不能只写“18 岁帅哥 / 温柔小姐姐”，而是要明确告诉 AI风格、角色特征等提示词。

**男频小说男主角举例：**

> 真人写实风格，线条硬朗，对比度高，硬阴影，男性荷尔蒙。一位28岁男性，地下机械师，高大精瘦，有肌肉线条，站姿慵懒微驼背。一头乱糟糟的黑色中长发，脸上留着胡茬，死鱼眼，黑眼圈，嘴里叼着一根没点燃的香烟，脖子上挂着战术护目镜，颓废帅气。穿着敞开的深绿色工装连体裤，布料有油污和磨损的做旧质感。右臂是复杂的黑色机械义肢，腰间工具带挂着扳手，脚穿重型工业靴。 表情玩世不恭，眼神冷漠傲慢，向下俯视。背景虚化。

![图片展示了一位男性角色，背景为工业风格场景，有管道和设备。该角色留着凌乱的黑发，面部有烟雾缭绕，表情冷酷，嘴唇叼着烟。他穿着沾满污渍的黑色工作服，左臂有纹身，右手持着机械手臂，腰间别着工具。整体形象粗犷、神秘，与上下文提到的男频小说男主角形象相契合，体现了冷酷、机械感等特征。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=M2RjOGJmNTY1OTc1ZWE5OGY0YzQ2NGJkZGQ4NjhjNTJfOTE0YzA0ODhkMTcwNGM5ODYxNDdmM2Y0ZmZmZTZiMjNfSUQ6NzY1ODUxNDk1ODUzOTM0NDg0M18xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM)

**女频小说男主角举例：**

> 真人写实风格，一位年轻冷艳系古风美男，冷白皮，窄脸，高鼻梁，狭长眼睛，唇色偏红，黑色长发半束发，一缕碎发垂落额前，头戴银色雕花华丽发冠，身穿黑色华贵长袍，衣袍带金色暗纹刺绣，内搭暗酒红色，身形修长清瘦，气质冷峻矜贵，正视镜头，表情克制清冷，暖金色强逆光从身后照亮，发丝边缘光明显，肩部轮廓光强，正面柔和补光，面部干净通透，珠宝与金属细节闪烁高光，背景压暗虚化，梦幻辉光，体积光，华丽神秘，高级感。

![图片展示了一位年轻冷艳系古风美男，符合女频小说男主角的设定。他冷白皮，窄脸，高鼻梁，狭长眼睛，唇色偏红，黑色长发半束发，一缕碎发垂落额前，头戴银色雕花华丽发冠，身穿黑色华贵长袍，衣袍带金色暗纹刺绣，内搭暗酒红色，身形修长清瘦，气质冷峻矜贵。暖金色强逆光从身后照亮，发丝边缘光明显，肩部轮廓光强，正面柔和补光，面部干净通透，珠宝与金属细节闪烁高光，背景压暗虚化，梦幻辉光，体积光，华丽神秘，高级感十足。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZDYwMTU0ZjJiMDU5MTJkNDhhNDFmOWUwOGVkYzMxZGZfM2NmMjg3Mjk4MDllODJmYzJjMjRlMmM4ZDUwY2QxZGJfSUQ6NzY1ODUxNDk1NjExNTQ0NjczM18xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM)

这些词不是文学装饰，而是在明确“目标读者是谁”，从而让画面与受众期待对齐。

在弄清角色本质之后，我们才开始进入“如何用 AI 把人物落地成图”的步骤。整体上，我们推荐这样一条工作流：

> **从剧本/小说中提取人物信息** → 用大模型生成结构化的人物小传 → 从人物小传中提炼视觉关键词 → 把视觉关键词组织成 AI 绘画提示词 → 迭代到稳定形象后，补充三视图与表情卡。

### 3、AI辅助提取人物信息

面对甲方甩给你的一个剧本，要一个个去熟读并解析里面的角色信息是很耗时间的。

教大家两个利用AI快速辅助生成提示词的方法：

#### 1）提示词模板

具体操作时，你可以给大模型一个类似如下所示的指令框架：

> 你是一个AI出图设计师，根据这个故事剧本，帮我罗列出所有的资产，包括人物，场景，道具。给我输出这些内容的AI出图提示词，要求是真人写实风格。

> 人物的出图提示词一定要全身正面白底，要有鞋子的描述，人物不要拿任何东西，双手垂落，全身站立，角色形象提示词要描述人物的身高，体型、年龄、发型、发色、服装、脸型、眼睛。要贴合人物角色的人种、时代、发饰和服装。人物没有任何表情，成年人（非小孩和老人）最好是8头身比，并且不要太丑太极端。即便是反派，在满足他们剧本中的特点的时候，尽可能让他们好看一点，毕竟观众都不喜欢盯着丑东西盯太久。

> 场景设计不能有人，并且根据角色的站位至少生成正反打两个场景图提示词和一个侧面全景图的提示词。

> 道具提示词一定要纯白底，不要有背景和任何人物。注意我只要提示词不要你出图，中英文各一版。

**这一轮的目标，是让AI帮我们分析故事，生成对应的人物形象，他不一定完全准确，但是可以先给我们一个底子。**

就拿下面这个小说举例。

<figure id="doxcnksZCvnJScRpQR2bOtVrysU" view-type="Preview"><source id="doxcn0umFrp2MLyp5HuY6NL2dzc" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NTQxZGJmNDNkODYxYTBmYjYzOTliMWFlOWM2YWVkMjJfZWFjNjI5NTc0NWJmNDRhZThlYjVkMzg0NWNjYjc4ODlfSUQ6NzY1ODUxNDk1OTA2Mzc5NjcxN18xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="text/plain" token="VByTbbNJbovqcYxQAiccRwwzn1d"/></figure>

![图片展示的是文档中“AI辅助提取人物信息”部分的示例内容。上方是“苏白羊与林小鹿”剧本中的人物苏白羊的描述，包括其身高、体型、着装等信息。下方是基于剧本整理的AI出图提示词，分为中文和英文两部分，分别对苏白羊的全身正面站立姿势、着装、发型、面部特征等进行详细描述，还要求背景为纯白。该图片与上下文紧密相关，直观呈现了AI辅助提取人物信息的操作示例。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MzE5MTQ2YWM3ODVkMDVjNDg4YWYwOWJkMTU0MzRhZmFfY2IxOGYyMjljNjAyMDA5OTY4M2Q0MzIzMmJhMmNjMWVfSUQ6NzY1ODUxNDk2MTU3NjAzNzMzM18xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM)

一定要注重背景故事、性格特征和视觉风格。背景故事就看是古代、现代。性格特征就是角色外在和内在契合，性格是什么样，外在表现也是一样的。是男频文还是女频文，视觉风格，比如服装配饰颜色也很重要，这些一定要都满足甲方的需求。结合这些信息再去跟AI下指令，生成的内容比直接一句话生成出来的质感和丰富程度要好很多。注意一定要加鞋子的描述词，不然人物全身图大概率不是全身。

## 二）资产图生成工具

### 1、LibTV（首推）

https://www.liblib.tv/

LibTV - 专业视频创作工具

**LibLib** 最新出的画布式工具，与Tapnow相似的聚合平台，功能强大，几乎接入了所有主流的图片、视频模型工具。也可以接入Agent，它有很多打包好的、可以直接调用的专业创作能力，通过 Skill 接口理解任务、调用模型、编排工作流并自动完成创作。

接入的图片模型包含： **Nano Banana 系列、字节的Seedream系列（即梦图片模型）、最近新出的GPT Image 2、Midjourney系列、Qwen系列、Z-image等模型**

由于一些原因，某些国外模型的名字进行了修改，但本质都是一样的，接入了API。

> **Lib Nano Pro = Nano Banana pro**

> **Lib Nano 2 = Nano Banana 2**

> **Lib Image = GPT Image 2**

接入的视频模型包含： **Seedance 2.0/2.0 Fast、Kling O3/3.0、Vidu系列、Wan系列、hailuo系列等各厂主流视频模型，后面的课程会跟大家详细介绍。**

**具体使用方法如下：**

**鼠标双击画布，添加图片节点**

![这张图展示了LibTV工具的操作界面，界面的左侧是功能菜单面板，其中“图片”选项被蓝色方框高亮标注，面板内还设有文本、视频、音频、脚本、上传、从图库选择等功能选项。图片右侧有蓝色文字标注“双击画布，选择图片”，这一内容和图片所在文档里LibTV工具的使用方法相呼应，对应文档中“鼠标双击画布，添加图片节点”的操作步骤，为使用者演示了添加图片节点的操作入口。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZGViYzYwZDlkYTMzNjM4M2I2NTM3NTI4OGQ4N2QyMTFfY2ZjZWVlZjFhZGE1MmJiOWQwZGIzODdlNjk1YWUwM2JfSUQ6NzY1ODUxNDk2MDk0NzAzOTIxMV8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM)

**根据需要，选择一个图片模型**

![图片展示了LibTV中选择图片模型的界面。画面中列出了多个图片模型选项，包括Lib Nano Pro、Lib Nano 2、Lib Image、Seedream 5.0 Lite等，每个模型后有对应的时间消耗。画面右侧有蓝色箭头指向Lib Nano 2模型，并标注“根据需要，选择任意图片模型”。该图片与文档中介绍LibTV使用方法的内容相关，用于说明在使用LibTV生成资产图时，可根据需求选择任意图片模型进行操作。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YWFlYzI0NGQ3MDBmMmQ3MzgxNTk5MzI3YWY0MTYwMTNfMjI1NDE5NTE3ODkxZjFhZmMxZmQ2NDNlNmEzOTliYzZfSUQ6NzY1ODUxNDk1OTk4MjUyOTUxMV8xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM)

**输入角色/场景/道具提示词：**

![图片展示的是LibTV生成图片的界面。画面中输入了关于角色的详细描述，包括年龄、身份、外貌、服饰等信息，如25岁古代贵族公子，身穿深青色与月白色相间的宋制文人长袍等。界面下方显示模型为Lib Nano 2，分辨率9:16，出图比例2K，还有摄像机、全景等选项，以及1张、12等参数设置。该图片与文档中介绍LibTV使用方法的内容相关，直观呈现了输入角色描述及模型选择等操作。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NGRjMGYxNTYyNGRjMWY4YzIyZjBiMzNiN2RhMDI3NjFfZTg2OTk1NTY4NzJkOTAyYjNlNGRjOWM2MTg5YzMwOTlfSUQ6NzY1ODUxNDk2MDI5ODcyNDI5OV8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM)

**选择分辨率和出图比例：**

> 一般 **角色正面全身照** 选择9:16的出图比例，2k分辨率即可。

> **角色三视图/四视图** 可以选择16:9或21:9的出图比例，2k分辨率即可。

> **场景图** 可以选择16:9的出图比例，2k分辨率即可。

> **道具图** 可以选择1:1的出图比例，1k/2K分辨率皆可。

![图片展示的是LibTV生成角色形象图时的分辨率和比例设置界面。界面中有1K、2K、4K三个分辨率选项，当前选中2K。比例部分有自适应、1:1、9:16等多种选项，其中9:16被选中。该图片与文档中介绍LibTV生成角色形象图时可选择16:9或21:9出图比例，2k分辨率即可的内容相关，直观呈现了设置界面。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YzdkZjg4OGFlNDFkMzA0MTlkODM0NTY3M2Y2OTQwNDhfODdiYzcxNzhmODk1YzJlMjQzNjc3YTA4NjBmZGJmNWZfSUQ6NzY1ODUxNDk2MjM4NTcxODIxMl8xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM)

稍等片刻，就能得到初版的角色形象图。一定要根据剧本的世界观、剧情内容、审美风格等来不断调整提示词，一次次去尝试，最终才能得到满意的人物形象图。

![图片展示的是LibTV生成的英俊的中国25岁古代贵族公子角色形象图。该角色全身照，正面视图，站立，纯白背景。其头发束成整齐的发髻，插着一根简约的玉簪。身穿华丽的带有刺绣的深青色与月白色相间的宋制文人长袍，腰间系着精致的腰带，丝绒质地，衣料垂坠感极佳。长袍下露出精致的深色鞋面一角。二八身材比例，真人写实风格。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YzE0NjNiYTdhYjBiYWViZjg5NmUwNTk0NDJkYTZjMGZfMmRiMzAzNTZhYWZiYjNkY2FkOGUyMjE0MDlhMzQxOWVfSUQ6NzY1ODUxNDk2MzEzMjQxOTAzMF8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM)

### 2、即梦AI

这是大家非常熟悉的一个平台。属于字节旗下的平台，可以出图、出视频、配音。

旗下的主流图片模型 **Seedream系列模型** 对中式风格的适配性非常好，可以为短剧定下高级的视觉基调、设计古装剧的服化道。

缺点：国内版平台只接入了自家的模型， **Seedream系列模型** 在改图、融图能力和整体美感上相较于 **Nano Banana/GPT-Image 2** 等模型差了不少.

https://jimeng.jianying.com/

即梦AI - 即刻造梦

在即梦的创作界面中，把模式改成“ **图片生成** ”。这些模型都是字节的 **Seedream** 系列的 **图片模型** ，注意要跟 **Seedance** 系列的 **视频模型** 做出区分。

选择一个图片模型， **建议选择图片4.0之后的模型** ，同一个提示词每个模型的出图效果略有不同，每个模型上面都写了模型的特点，作图的时候可以每个都尝试一遍，选择效果最好看的那个即可。其余的用法

![图片展示了即梦AI的创作界面，左侧有“图片生成”“视频生成”“数字人”“配音生成”等模式选项，其中“图片生成”模式被红色框突出显示。右侧是创作模型选择区域，有“图片生成”“视频生成”“数字人”“配音生成”等模型，其中“图片生成”模式被红色框突出显示。该图片与上下文紧密相关，上下文提到在即梦的创作界面中把模式改成“图片生成”，此图直观呈现了操作步骤中模式选择的界面情况。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YzEwNjBiMDU5MTE0ZjE5MjEyM2Y2NDI3MTM3MTY0MWJfZDU5Nzc3NTE5YTRjNGRmMDU2OGQ4ODc1OGUzNDRlODNfSUQ6NzY1ODUxNDk2NTA4MjUyNDY1MV8xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM)

![图片展示了即梦AI的创作界面中图片生成模型选择部分。画面中以红色框突出显示了多个图片生成模型，包括图片4.0、图片4.1、图片4.2、图片4.3、图片4.4、图片4.5、图片4.6、图片4.7、图片4.8、图片4.9、图片4.10等，每个模型名称后有对应的数字序号标识。这些模型均为字节的Seedream系列图片模型，用户在作图时可尝试不同模型，选择效果最好看的。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YzZjZWUwM2UwZGVkMzE5N2YwYTgyZDM0ODQzMDhkZWVfN2Q4NDJmZjkyZTA1NDdmYTM5M2Y5MjkzZDEyMTI3NDVfSUQ6NzY1ODUxNDk2NDM4NjY0NzAwNF8xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM)

## 三）不同模型生成效果

AI仿真人短剧的角色图主要用以下四种模型来出：

**第一个是香蕉（Nano Banana系列）**

**第二个是即梦图片模型（Seedream系列）**

**第三个 Z-image系列模型**

**第四个是新出的GPT Image 2模型**

在AI仿真人短剧里，在符合剧本设定的基础上，美感越好、越有真实越有呼吸感的人物效果会更好。

模型的选择通常没有明确的界限， **哪个生成的效果最好就用哪个** 。

以我们的自制古装短剧《 **重生之这满门白眼狼我不养了** 》中女主角 **沈宁** 的角色形象作为案例来举例：

> **即梦 Seedream 系列** ：对中国风元素理解更到位，价格便宜。但生成的人物整体 AI 感较为明显。

> **Z-image** ：因使用大量小红书人像图片训练，生成效果真实感强。不过有偏向网红脸的问题，作为开源模型，价格最便宜且可调用。

> **Nano Banana 系列** ：由谷歌推出，底层训练数据多为欧美数据，生成的人物样貌偏向欧美人长相。若提示词详细，能生成出色的人物角色图，适合创建真人风格与 3D 风格形象。如 **Nano Banana 2** 通过技术革新，实现了速度、质量和成本的平衡。

> **GPT Image 2** ：是 OpenAI 于 2026 年 4 月 21 日公测的模型，效果惊艳，人物美观，对提示词理解能力强。它将推理能力融入图像生成，整合了网页搜索等功能，文字渲染精度大幅提升，风格还原能力出色，但成本相对较高。

<table id="doxcnxmnXQFZ7Dw2FOlJaW2INuc"><colgroup><col/><col/><col/></colgroup><tbody><tr><td vertical-align="top"><img id="doxcnRbbKOT5S84oKN21ogfol7g" name="a790e86118a376b5d24e5630ceef2cb5.png" alt="图片展示了一位身着古装的女性。她头戴黑色发髻，发髻上别有金色发饰，身着白色上衣与浅紫色长袍，下配白色褶皱裙，脚穿绣有花卉图案的鞋子。此图对应文档中介绍GPT Image 2模型生成效果的内容，直观呈现了该模型生成人物美观、风格还原能力强的特点。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=Y2E1MGFjY2I0ZmRmMjA5NzJhNzNkM2UxOGY3YTJjYjlfMjcyZDUzYzM2MzI3YzIyZmNlMjU0Zjc2NzY2MmViOWJfSUQ6NzY1ODUxNDk2ODM2MjM3MjA1NF8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="H4Bpbl2lSonW29xcCNhcGnJtnoh"/></td><td vertical-align="top"><img id="doxcn3i8TLSknnfzAtUjEe0bBWg" name="2ac16802327ab0e584c840d362d372ee.png" alt="图片展示了一位身着古装的女性。她头戴发饰，身着紫色上衣，外披白色长裙，裙摆处有紫色花纹装饰。她双手合十，面带微笑，背景为纯白色。此图与文档中介绍不同模型生成效果的内容相关，用于直观呈现GPT Image 2模型生成的古装人物效果，体现其人物美观、对提示词理解能力强等特点。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MmEyYmI3MzM0YTA0ZjRiNzgwY2M3MDUzMDM5OWJlY2ZfNjlmNDI3NDRlZmFlNzgwYjcyY2E5NGNhNjAxZTBhZjNfSUQ6NzY1ODUxNDk2ODc5NDQzNDUxNF8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="JkeNbzKq7ohBRKxsb40cQgtsn7f"/></td><td vertical-align="top"><img id="doxcnxBW3xqqpwr2xD7F3QdpXRe" name="296180cbfa7dcbacae2c6b300373f73f.png" alt="图片展示了一位身着古装的女性。她头戴黑色发髻，佩戴着金色发饰，身着淡紫色长袍，内搭白色上衣，腰间系有紫色腰带，下身穿着白色长裙，脚踏白色鞋子。整体装扮典雅，与上下文介绍的GPT Image 2模型生成效果中人物美观、风格还原能力出色等特点相契合，直观呈现了该模型生成人物形象的美观度。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YTE3ZWVmYTZkYTk3ZTVkYzg1ZGJiYWIxMTBhYTg3NjRfMTJlMGM1NTQ5MTNmZTEyZTc4YTBhN2UwZDMwN2QwMTJfSUQ6NzY1ODUxNDk2ODcwMjIwODk5M18xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="GkKebIGAFooDmcxACtScP4kcnQg"/></td></tr></tbody></table>

<table id="doxcnmTT3LoAdDOqCH9zNZ3vkGb"><colgroup><col/><col/><col/></colgroup><tbody><tr><td vertical-align="top"><img id="doxcnsoPms7pGtbrlUtPkyNrcec" name="da2ade4c5e1eb51e9254ac94c97d6fb2.png" alt="图片展示了一位身着古装的女性。她头戴发饰，身着淡紫色长袍，袍内搭配白色内衬，腰间系有紫色腰带，下身穿着白色长裙，脚踏白色鞋子。整体装扮典雅，背景为纯白色。该图片与文档中介绍的GPT Image 2模型相关，用于展示其生成效果，体现了该模型在人物美观、风格还原等方面的能力。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MjIwZWQyYTVjNGMxODdhOTU1ZGM3MzlhMzNjZDBmMTlfZDFiYzE4NTQ3NjQzNWIyYjUxYThkYjI3MWZmMTcwZmNfSUQ6NzY1ODUxNDk3MDgwNTE2MDg5OF8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="DWmGbLNXloBeQ2xIMaNcAQ2FnFc"/></td><td vertical-align="top"><img id="doxcnkmRWLVeWMsDW0ExwtWyivf" name="22c3bd80fa1ac05052331ccd8c6a3099.png" alt="图片展示了一位身着古装的女性。她头戴精致的发饰，身着淡紫色与白色相间的长袍，袍子上有精美的刺绣花纹，腰间系有白色腰带，脚穿白色鞋子。她的双手合十，姿态端庄。此图与文档中介绍的GPT Image 2模型相关，该模型是OpenAI于2026年4月21日公测的，人物美观，对提示词理解能力强，将推理能力融入图像生成，风格还原能力出色，但成本相对较高。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NjUyNzcxZTUxMTc2OWMzYzE1NzE5NzYwNTM2YThmODJfNTBlMzU3M2Q4YTQyMjk1MGU1YWY5ODYyNjg5YzFmZjJfSUQ6NzY1ODUxNDk3MTk5MDQ2MTM4OF8xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM" mime="image/png" scale="1.000000" src="TVqpbIaotoDfb1xUcYNcCJOqn3e"/></td><td vertical-align="top"><img id="doxcnEDBNFIGyEWxKE0GTe9019e" name="ba9649e0913421206c3dce6c8fb04c0a.png" alt="这张图片呈现了一位身着宋代风格汉服的女性，她梳着古风发髻，佩戴精致的发饰与耳坠；外穿淡紫色暗纹长衫，内搭米白色交领襦裙，下着同系百褶裙，脚踩绣有花纹的浅口古风鞋，双手持绘有花枝图案的团扇，姿态优雅温婉。该图片位于《西石羊第四期SOP》中“不同模型生成效果”相关内容处，这类模型可生成符合传统古风审美、细节考究的人物图像，是其能力的体现。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NDllN2FjY2M3MjNjYmNlNmRjYThhZGI1ZmZkMjZmMDhfYjhlMjg3YjRkNDViNTQ0NDgwNWU0NTc5OTk4ODUyYWRfSUQ6NzY1ODUxNDk2ODc2Mjg3ODkzN18xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="TAAtbuJA7oY68kxEhkwcNQ3qnag"/></td></tr></tbody></table>

## 四）角色设计常见问题

在大量 AI 短剧 项目中，角色设计常出的问题，往往集中在以下几个方面：

### 1、服装造型不搭

通过前面各个模型生成的女主角沈宁的图片，大家是不是觉得各模型效果都挺不错？实际上，这些都是对提示词进行精雕细琢后的成果。像汉服、头饰等细节都描述得极为详尽，所以呈现效果相对稳定。

AI给出的提示词，常常带有刻板印象。对于现代妆造，这种情况还好，但涉及古代妆发，初版提示词基本无法使用。通常都得反复调整和尝试。在直播课上，会现场为大家演示这一过程。

![这张图片展示了两款适配古装剧不同类型的汉服造型，对应文档中服装造型适配剧集类型的内容。左侧为大红色搭配金色纹样的古装，带有华丽头饰，符合古偶剧造型偏向艳丽华贵的特点；右侧为浅紫色外衫搭配米白色内裙的古装，造型素雅，契合架空类古装权谋剧、宅斗剧等的风格要求，体现了不同古装剧类型在服装造型上的风格差异。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZjA5MjBmZjE2MzQ3MWM5NjJjMjBmY2RlYzlmZGNlMjBfZDQ3YWE5YjFmYmU3YjQzMzA4ZWJmYWNjOTk0N2QxNjdfSUQ6NzY1ODUxNDk3MzQxMjM3OTU5OF8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM)

古装剧在服化道方面相对麻烦。不同历史时期的汉服各具特色，古装剧可依据类型做出有针对性的选择。

**古偶剧** 的造型可以偏向艳丽、华贵； **仙侠类** 的造型能够突出空灵、梦幻，强调超凡脱俗的气质； **武侠类** 的造型可以展现出潇洒、飘逸，不受礼教拘束的风格；而 **世俗王朝、架空类的古装权谋剧、宅斗剧** 等，最好以某一特定汉王朝时期的服化道作为大体原型，以此营造出相应的历史氛围与风格。

<table id="doxcn8zrl8NhmG08tPBUQUvOZff"><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td vertical-align="top"><img id="doxcnQ2cWmjT0fI6QIF9hLiO8Rb" name="4430f2aff3bfe9519db1c41354cd0ea8.png" alt="图片展示了一位身着古装的男子，头戴华丽的头饰，服饰以黑色为主，饰有金色花纹，内搭红色衣物，整体造型华丽且具有历史感。该图片与文档中“世俗王朝、架空类的古装权谋剧、宅斗剧”等剧集服装造型设计相关，用以说明此类剧集最好以某一特定汉王朝时期的服化道作为大体原型，营造相应历史氛围与风格。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NWRkMzNhODdhMmJiODkxMjEwZjFmNDBhMzYyNzQ1NGRfZDY5Mzk3MTQwMWQxNjAxMWZkZjgyZDNjYWYzYTMwNjJfSUQ6NzY1ODUxNDk3MjU0ODQwMjE2M18xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM" mime="image/png" scale="1.000000" src="XA8nbJNJWo61NJxc2L9c46hRnAc"/></td><td vertical-align="top"><img id="doxcnm9YU7v1OV4pe3ic3GCQ1ee" name="caae914ddf2d2b55e843e7434835b2ca.png" alt="图片展示了一位身着古装的男子，背景为古建筑。男子长发束于脑后，面带严肃表情，目光锐利。他身着深色古装，外披黑色长袍，内搭浅色衣物，腰间系有装饰带。此图与上下文关系紧密，用于说明世俗王朝、架空类古装权谋剧、宅斗剧等以特定汉王朝时期服化道为原型营造历史氛围与风格的内容，直观呈现了此类剧集角色的服饰造型特点。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NjNmYTYwYjMzOWE0NmFmNTRjZmMzMjQyOGQ0YmQ0ZTNfZDdhNmM0ZTVjMjY3YjEyODg4ZDAzYmUwODEwOTQ2MmZfSUQ6NzY1ODUxNDk3MzYzNDcyNjg2M18xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM" mime="image/png" scale="1.000000" src="HaepbXZDToeKB0x7wVnclNgTnrb"/></td><td vertical-align="top"><img id="doxcntSBk31dUhUQ5uCYkTs0muF" name="0f4edf735bef4c32da2480da09646597.png" alt="图片展示了一位身着白色古装的男子，背景为云雾缭绕的山峦。男子长发披肩，头戴精致的发饰，面带冷峻表情，眼神锐利。他身着的古装以白色为主，衣摆飘逸，腰间束带，整体造型飘逸、空灵，符合仙侠类剧集的服装风格，与上下文提到的仙侠类造型能突出空灵、梦幻，强调超凡脱俗的气质相契合。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=Yzg1MjEwYWU4OGJhZDExZTdkYTljZGIyZGY1Yjc3ZTVfYjk2ZmFjMDU2YzFmNjk1OTc0NWE3YzZiNGE3NzFkYjZfSUQ6NzY1ODUxNDk3NDk4MTE4MDM4NF8xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM" mime="image/png" scale="1.000000" src="J07jbOcoUoPoItxdcvrcjaK6nTQ"/></td><td vertical-align="top"><img id="doxcnkIE9qYczEq5e0Sce2heKLd" name="296a196cb1b8df87658f8ce0624452c8.png" alt="图片展示了一位身着古装的男子。他头戴黑色发冠，发髻高束，面带严肃表情，目光直视前方。他身穿深色古装，外披黑色带有花纹的长袍，内搭白色衣物，衣领处有黑色装饰。背景为室内场景，有木质屏风、蓝色幔帐等装饰，整体色调偏暗，营造出庄重的氛围。此图与上下文关于不同朝代女子汉服特征的内容相呼应，直观呈现了秦汉时期女子汉服素雅质朴、深衣为主、曲裾绕襟、线条简洁的大致特征。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZjJhYzkzYzhmODI2MWIwNTRmMTI4NjU5NDk2Mzc4ZDNfYzdlNGYxYjRjNTM5MTMzYzMyNWM1MWZmODJiZWRlNGVfSUQ6NzY1ODUxNDk3NzE2MjA4NzM4NV8xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM" mime="image/png" scale="1.000000" src="AzwqbjcCzoMiSwxqxhzcS5gtnUg"/></td></tr></tbody></table>

不同朝代女子汉服的大致特征：

> **秦汉** ：素雅质朴，深衣为主，曲裾绕襟，线条简洁。

> **唐代** ：华丽开放，齐胸襦裙盛行，高髻丰腴，色彩明艳。

> **宋代** ：清雅内敛，褙子流行，窄袖素雅，发髻简约。

> **明代** ：端庄华贵，袄裙马面裙，高髻繁复，织金刺绣精致。

如果实在没有想法，那就找对标！看看现有的同题材的影视剧中的服化道都是什么样子的。

受到电视剧《知否知否，应是绿肥红瘦》的启发，我选择了 **宋制汉服，更加简约、优雅、大气** 。

<table id="doxcnfFUl57pAKuZikapWc3UtUe"><colgroup><col/><col/></colgroup><tbody><tr><td vertical-align="top"><img id="doxcntY7gJf7aaujhZGZFw7eAGb" name="38855129b2dbb635821e5e3d46d5ece4.png" alt="图片展示的是电视剧《梦华录》中盛明兰的演员定妆照。画面中盛明兰身着华贵而淡雅的天青色与象牙白相间的宋制汉服，长褙子与百迭裙相配，头戴白玉发簪，面带微笑，姿态优雅。背景为室内场景，有屏风、植物等装饰，右侧有另一名演员。图片与上下文关系紧密，是对上文提到的服装造型不搭问题调整后，即梦4.6模型生成效果的呈现，体现了最终选定的服装造型。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NDAxY2NiYzc5OGFhYWM5ZTdjMzYwMjc4NWZlNjFjYmVfZjZlNjNiNDJlNzUyOTEwNDI5YzkzNzFkMmI2OGM0YmZfSUQ6NzY1ODUxNDk3Njk2NDkzODczNV8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="QPPGbjOZjoAUSixkM9Cc8AVHnwb"/></td><td vertical-align="top"><img id="doxcngLGJ4El2QWtGXz8PCj2CMg" name="8ead14605fbf2846ed00aa1d42086023.png" alt="图片展示的是电视剧《知否知否应是绿肥红瘦》中的一幕。画面中，一位身着华贵淡雅的天青色与象牙白相间宋制汉服的女性，长褙子与百迭裙相配，头戴发簪，面带微笑，坐在桌前，桌上放着书卷。背景为室内场景，有屏风、桌椅等家具，窗外透进自然光线。该图片与文档中角色设计常见问题中服装造型不搭的上下文相关，是采用即梦4.6模型生成的服装、造型效果示例。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=Zjk2MzAwNWQwZmFlNzdhYThkOTU5YTA2OWE4MWNiMGNfODc5MTNlMTUyMjdhNDU3NzZlM2Q4OWI2M2VlMzU0YjZfSUQ6NzY1ODUxNDk3NTIxNjE0MzMwOF8xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM" mime="image/png" scale="1.000000" src="WI8KbGMx6ovpdcxMGupcFM1qnle"/></td></tr></tbody></table>

![图片展示的是电视剧《知否知否应是绿肥红瘦》里女主角婚后日常剧照，画面中女性身着淡雅宋制汉服，长褙子与百迭裙相配，头戴白玉发簪，面带微笑。图片旁有文字提示，要求仿照此衣着、发饰风格，改写女主的提示词。该图片与上下文紧密相关，是作者在角色设计中对服装造型参考的示例，用于说明服装造型不搭问题的解决思路。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NmU1M2Y1Njc1MzlhNDZjZDY5MzBmMDJmMWIwYmJlYmFfMTQ2MjZiNzFiNTgwZTlkMjdlMThlNDA4ZGJmODgwNWNfSUQ6NzY1ODUxNDk3NjA3MTg3OTYzOF8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM)

于是在初版的提示词的基础上，将衣服的主体款式改为“ **华贵而淡雅的天青色与象牙白相间的宋制汉服，长褙子与百迭裙** ”。以下是采用即梦不同模型的生成效果：

<table id="doxcnogZn0yBFUMMcSTvCRB88Sg"><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td vertical-align="top"><img id="doxcnlKPhCXUMk7sj0Uv9keHd1d" name="c0517585def7843d70603a3cc0905f36.png" alt="图片展示的是即梦4.6生成的服装造型效果。画面中人物身着淡蓝色与米色相间的古装，上衣为淡蓝色，带有白色花纹装饰，下身是米色褶皱裙，脚穿白色鞋子，头戴白色发饰。该图片与上下文紧密相关，用于对比说明在服装造型不搭问题上，即梦4.6生成的效果是我最喜欢的，没那么夸张且相对更精准。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NzgyYWI5YjY0MmYxOGZkMjA1Njg0ZWI0ZTdhMTQzMDJfOGY0NWE4ZDkxZjU4OTY2YWExODdlY2RmMDA3MjVhNmFfSUQ6NzY1ODUxNDk3ODYzMDI0MTIzNl8xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM" mime="image/png" scale="1.000000" src="MSx7bSeTUoziYfxqv4PciBDnnSh"/></td><td vertical-align="top"><img id="doxcnVLyRiJ77jG0lNRs8JHyrWg" name="70c418d8b215eae61821a383897ab77b.png" alt="这张图片呈现的是一位身着宋制服饰的女性形象，服饰为青绿色褙子搭配米白色襦裙，头上梳着古典发髻，搭配白玉发簪，妆容淡雅，面带温和的微笑，双手交叠置于身前，姿态端庄温婉。该形象是西石羊第四期SOP中，针对角色设计里服装造型问题，调整修改后，经比对确认的即梦4.6模型生成的角色定妆形象，符合演员定妆照无多余表情的要求，服装造型风格适中，造型效果精准贴合需求。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=M2ZhM2Q1Mzg2ZjFjNTQzMGIzNjdiMjQxODFhOGI0NGZfM2FhYTYxYWIxZDQ4ODQ0OTA4NTQyYzU0Mjk5MjkwY2NfSUQ6NzY1ODUxNDk3NzU5NDYyNDk3M18xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="JKcVb5daLoEUyixN17SchEKMnSh"/></td><td vertical-align="top"><img id="doxcnRFzcLZBa2PcWhgJj9Xmiff" name="69342003d36239b7b614f81f7311a3dd.png" alt="图片展示的是即梦4.6生成的服装造型效果。画面中人物身着淡蓝色与米色相间的汉服，外披淡蓝色长披风，披风上有精致花纹装饰。人物头戴白色发饰，面带微笑，双手合十于身前。该图片与上下文紧密相关，是文档中讨论服装造型不搭问题时，对比不同模型生成效果的内容之一，直观呈现了即梦4.6生成的服装造型，体现了其服装、造型相对精准、不夸张的特点。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=M2UyMGJiMTc2OGRiYWVhODU0MDQzZDI1M2IxMzAwMTBfODdmMzFmNWZlNDUyMzVhZTdiY2IwOWFiZGQyODgzZTFfSUQ6NzY1ODUxNDk3OTQxMjEzNDg4NV8xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM" mime="image/png" scale="1.000000" src="YFCPbc90RosCRmxAcSoc05NMnUe"/></td><td vertical-align="top"><img id="doxcnqHbPq0pUDb5yVJesBhryQc" name="268319f9cdef71f38397793f1a1189fa.png" alt="图片展示的是即梦4.6生成的服装造型效果。画面中，一位女性身着传统服饰，上身是浅蓝色的长袍，内搭白色衣物，下身是白色褶皱裙，脚穿浅蓝色鞋子。她的发型为高束发髻，头饰精致。该图片与文档中“角色设计常见问题”部分相关，用于对比不同模型生成的服装造型效果，经过比对，即梦4.6生成的服装、造型被作者认为是最喜欢的，没那么夸张且更精准。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NzQ0NDNkZmQ1ZTMyZjAwZDlhODljZjI4MDM3OTdiNWNfN2U1MGFjNTQzMWQ3YzVlYjMwNGIzMTc3OGIzMDQ2N2VfSUQ6NzY1ODUxNDk4MjIyNDYxMjI4OF8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="TvIMbbimhomG3DxMv6RcGqnEnPf"/></td></tr></tbody></table>

发型原提示词中的“白玉发簪”不太好看，而且演员定妆照最好不要有其他表情，经过一番调整修改后，不同模型呈现出了如下效果：

<table id="doxcnT4PLBb8VNtkacQs1c3UnUd"><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td vertical-align="top"><img id="doxcnEsmeGovCXptgWSogavJJhu" name="09b4c1e95e247d90f91045119b9b365b.png" alt="图片展示的是即梦4.6生成的服装造型效果。画面中人物身着传统汉服，上衣为浅蓝色，带有白色花纹，下摆有白色流苏；外披一件白色长袍，袖口和下摆有蓝色装饰。人物头戴黑色发髻，佩戴金色发饰，耳垂有红色耳环，脚穿白色鞋子，鞋面上有红色花纹。该图片与上下文关系紧密，用于对比说明在服装造型设计中，即梦4.6生成的效果更精准、不夸张，是作者最喜欢的一种呈现方式。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=Y2VhNmQwNjgwZjgwNGIwZGU3OGM2NWM0ZjA5MzUzMDlfNDNiYmIyYTAwM2ZlNTVkMmY2MDJhOTM0YzhhZjZiNDBfSUQ6NzY1ODUxNDk4MDY5ODIxMzM2M18xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="T5D8br9DKo7od8xNAxKcU6xZnxg"/></td><td vertical-align="top"><img id="doxcn9mplJXriDysN4S0qNQiI8e" name="2fa63ab811905775525439612d9c10d3.png" alt="这张图片展示的是古装造型效果图，对应即梦模型优化调整后的角色服饰呈现。该造型为女子古装，梳着盘发并搭配精致的金色发饰，耳戴耳坠；身着外为青蓝色带精美花纹的广袖纱衣，内搭米白色绣有纹样的长裙，脚下是带有花纹的青绿色绣鞋，整体服饰风格贴合演员定妆的效果要求，无多余表情，且服饰精致规整，符合优化后更精准不夸张的服装造型要求，属于西石羊第四期SOP中角色设计常见问题里针对服装造型问题调整后的即梦模型生成效果展示，其中即梦4.6生成的这类效果为该次比对里用户偏好的呈现。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OGRiMTgwY2I5Y2U1ZTA3NGFkNDRiODFlMGM3NDgxZWJfZDNkNWYxNzI1NWQ5ODk1MjVhOGQ1MDNmY2ViMThiOGRfSUQ6NzY1ODUxNDk4MzM2MTM4MzM5Ml8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="UMiAbg4OloKHm7xaEpscC0Ubnze"/></td><td vertical-align="top"><img id="doxcnqzAlGk9phllaWDRdZpzTHe" name="3659440ae453678344a07cb17660d005.png" alt="图片展示的是即梦4.6生成的服装造型效果。画面中人物身着传统汉服，上衣为白色，带有淡蓝色边饰和绣花图案，外披淡蓝色长披风，披风边缘有白色花纹装饰。下身搭配白色长裙，裙摆处有淡蓝色边饰。人物头戴金色发饰，耳垂有耳环，脚穿绣花鞋。此造型与上下文提到的服装造型不搭问题相关，经过调整修改后，即梦4.6生成的服装、造型被认为是最喜欢的，没那么夸张且更精准。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZTg4NDZmNTBmYzQ2OWQxNDgwY2ViZjc3NTFmMzhkZTJfY2VmZjI0MmRjYjRkMzliNTlmN2Y5NTRjNzM1MWVlNjBfSUQ6NzY1ODUxNDk4Mzg1NjI0NTY5OF8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="TEnWbLnYwo92AUxB2AlcE5w7n5b"/></td><td vertical-align="top"><img id="doxcnyKiYJAehkmPe2sCf8Gsvoc" name="a4e7ff5194bd6e263e0da58b1562264a.png" alt="图片展示的是即梦4.6生成的服装造型效果。画面中，人物身着淡蓝色与米色相间的古装，上衣为淡蓝色，下摆有白色花纹装饰，搭配米色长裙，腰间系有白色腰带，脚穿白色鞋子。头戴黑色发饰，整体造型典雅端庄。该图片与上下文紧密相关，是对文档中“服装造型不搭”问题的解决示例，通过比对不同模型生成效果，此造型被评价为最符合要求，服装、造型既不夸张又精准。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NGMxNjQ3MDRkYzIwMGRhOTAwNWNiOWM0NTQwY2FhYjhfNTdhNDUwMzQ4M2RkNDhlMDA5YWJmNmUxYmJhMWUxZTRfSUQ6NzY1ODUxNDk4NTA4MjY4NjQyOF8xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM" mime="image/png" scale="1.000000" src="MeGEbSJzaofVRCxAnnVcYOJmn8b"/></td></tr></tbody></table>

经过比对，感觉 **即梦4.6** 生成的服装、造型是我最喜欢的，没那么夸张、且相对更精准。 **于是后面的造型都选择即梦的图片4.6来出** 。

此后又经过了非常多轮次的修整，包括改服装颜色、改头饰细节、改发型等，要不断地人为去尝试调整提示词。

<table id="doxcnT7t4VQNzBAXz7KRhaWy4sI"><colgroup><col/><col/><col/></colgroup><tbody><tr><td vertical-align="top"><img id="doxcnvN9FuxBkTLY2mAv8ZHnMcN" name="c9c7e8058cfd50626130f21b03373cab.png" alt="图片展示的是即梦4.6生成的服装造型，是经过多轮次修整后的定稿版。画面中人物身着粉色外披，内搭白色上衣，下穿米色长裙，脚穿白色鞋子，头戴金色发饰，整体造型优雅精致。该图片与上下文紧密相关，是对上文提到的服装造型经过多次调整后呈现效果的直观呈现，体现了最终选定的服装造型风格。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=N2I3Nzg5YWEwZjc4MTY3ODYwYWVlYzk1Y2E3YWFmMDNfNjBjZDczYTViNWE1NmZhMjA0M2U0OTZhMzRiNTVmMGVfSUQ6NzY1ODUxNDk4MzM3NDA5NzM1OF8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="GlqVby56noTWswxMVH0cur9Annh"/></td><td vertical-align="top"><img id="doxcnzhu3trAYvKHd29We3G0Sch" name="c426fabc4c05421a4ffc6171907adf50.png" alt="图片展示的是西石羊第四期角色设计的定稿版服装造型。演员身着粉色与米色相间的汉服，外披粉色长披风，内搭白色上衣，腰间系有白色腰带，脚穿绣花鞋。头戴黑色发髻，发髻上装饰有金色发饰。整体造型优雅端庄，与上下文提到的服装造型调整、即梦4.6生成效果等信息相呼应，是经过多轮修整后的最终呈现。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ODAwODRjZjE4MDAyNTMyMjYxNjE2NTRhODgyY2M4MmZfOTk4YjhmOTZmNzA0NDA0MjVkZTMyYmY2OTAzYTlkZDNfSUQ6NzY1ODUxNDk4Njg2NzY3NDA2NV8xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM" mime="image/png" scale="1.000000" src="KqGOb0VGNoX7hLx1vI7cAJjjnKb"/></td><td vertical-align="top"><img id="doxcnlp96iE87ZVosiURMrocGDe" name="0b8d24786d3302b05eed8afb7ff22e75.png" alt="图片展示的是西石羊第四期角色设计的定稿版服装造型。画面中人物身着淡黄色汉服，外披白色长袍，腰间系有白色腰带，脚穿白色鞋子。其发型为高束发髻，头饰精致，耳垂佩戴着耳环。该造型经过多轮修整，服装颜色、头饰细节、发型等均有所调整，最终被选为即梦4.6生成的服装、造型，是作者最喜欢的一种，没那么夸张且更精准。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZTJkOTNlZmY5OWMzZTJmYjA5NGVkYzU1ODliMzAzMDFfZTUzM2ViZWI4Njc4NGRiMGY1NGI1ZjVmODZjNjc1ZWFfSUQ6NzY1ODUxNDk4ODAzMzcyMzM0MF8xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM" mime="image/png" scale="1.000000" src="Hp3ZbAkwloR3zKxllMYcFCkLneh"/></td></tr></tbody></table>

**定稿版**

![图片展示了西石羊第四期角色设计中服装造型的定稿效果。左侧为红色服装，配有金色龙纹和云纹，头饰为黑色发髻配金色发簪，整体风格华丽；右侧为紫色外袍搭配白色内裙，头饰为黑色发髻配紫色发簪，整体风格典雅。该图片与上下文紧密相关，是经过多轮修整后，即梦4.6生成的服装、造型中最喜欢的版本，用于后续角色设计参考。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OTI2Y2JjNGVjYzM4MWQ0MzUwMDI2ZjViMDJkNTAyY2FfN2QwMGZjMjc1OTNjYjllNmJmNmI3NmUzODU4YjE3MjJfSUQ6NzY1ODUxNDk4Njg2Nzc4ODc1M18xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM)

对于里面的 **女配角林娇娇** 的角色形象。她的角色定位同样能在 **《知否》** 中找到类似的角色形象。电视剧中林噙霜额头一侧的那缕发丝极为经典。经资料查证，古代已婚女子一般不会在额头留这样的发穗。这额前特意留下的一缕头发丝，增添了几分风情，很契合她在剧中侍妾的身份形象。

类似的形象，我还联想到 **《琅琊榜》** 中的秦般若。作为风月场所红袖招的经营者，她同样有着这般风情万种的造型设计。

<table id="doxcnuCmD4Eh9vk6hsgD6SpOQXh"><colgroup><col/><col/></colgroup><tbody><tr><td vertical-align="top"><img id="doxcnS0LdbSNMZcd3hsZdP9yhlV" name="241fcc64315aa1d685a205f64ba230de.png" alt="图片展示的是《琅琊榜》中秦般若的剧照。她身着粉色花纹服饰，头戴黑色发饰，面带淡妆，侧身看向画面左侧，背景为室内环境，有木质栏杆和模糊的绿植。此图与上下文关系紧密，用于说明服装造型不搭问题时，可借助《琅琊榜》中秦般若的形象作为参考，借助AI优化提示词，以提升角色造型的契合度。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZTE3OWNlNzRhM2U4NDdhNzk0YTUyMDA5OTQ2ZmRlYjlfZGZkMzMzZGJiZDI2MTY2ZWMzMmY5ODEzNGIzYTFiYmRfSUQ6NzY1ODUxNDk5MDEzMDk1NzI4MV8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="JzvxbYOBdo1vXoxTqnocIxzgnXm"/></td><td vertical-align="top"><img id="doxcnHnQJKlVgqRiG29s6n5KPDc" name="aded3b5872e4d0657747a683e392da28.png" alt="图片展示的是电视剧《琅琊榜》中秦般若的剧照。她身着紫色古装，头戴精致发饰，面带微笑，背景模糊，营造出古风氛围。右上角有“琅琊榜”字样，左下角有“百度百科”标识。该图片与上下文关系紧密，用于说明服装造型不搭问题时，可借助类似影视剧剧照作为参考，借助AI优化提示词，以找到合适角色造型。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NmUxMWJmNThmZTQ3ZGNkZDZmMmJiZjI1ZGY1MWNjYjRfOWNmM2U2NGNhYzhhYzU5M2ZkYjJmZGNhZWI4NzUxMWNfSUQ6NzY1ODUxNDk4NzY2NDkxOTUwNl8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="ODYKbtSv6oPpiwxS9VscJOa2nDh"/></td></tr></tbody></table>

因此，我们依旧能够找寻对标影视剧的剧照来当作参考，借助AI协助优化提示词。 **⚠️注意：绝对禁止直接使用演员的脸来制作视频。可以让 AI 参照演员的造型，但绝不能直接采用他们的形象照片。**

![图片展示的是关于林娇娇角色形象提示词的修改建议。画面中包含一段文字，指出林娇娇的发装和发型可参考《知否知否应是绿肥红瘦》里林噙霜的发型和妆造，尤其是她额前的一缕头发。文字还给出了描绘这缕头发的词汇，如delicate wisp of tendril、wispy and soft tendril cascading等，并附有相关参考图。该图片与上下文紧密相关，是对林娇娇角色造型设计中服装造型不搭问题的解决方案之一。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MGU4ZTkxZWYzMmU3ZjI4MTgwYTFjOWM2MmM0ZjgxMjhfZTIwZTcwZmVkZjJiY2JhZTEwYjYwOTE5Y2E0NTY1MmFfSUQ6NzY1ODUxNDk4ODQyNDAzOTM1NF8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM)

**初版形象，符合即梦刻板印象的效果，十分夸张。**

![图片展示了林娇娇角色的四种造型。左侧两张图中，林娇娇身着粉红色带有金色花纹的长袍，内搭白色上衣，下穿米色褶皱裙，头戴黑色发髻，双手自然下垂。右侧两张图中，林娇娇发型变为低马尾，其他装扮与左侧相同。这些造型体现了角色设计过程中对服装造型的精细化调整，与文档中提到的通过持续向AI提出需求、人工反复修正提示词、不断雕琢细节来确定服装造型的内容相呼应。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MjIzNTIzODc0NTc0MzNlODIzNDEyYWQzNzI2MTdhZGJfMDdmNmFhZGY0NDNlMDYzM2RhNGY0OGQ4ODg3ODQ1MjlfSUQ6NzY1ODUxNDk5MDQ3OTE5OTE4NF8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM)

**修改很多版后，确定好服装：**

![图片展示了林娇娇角色的服装造型。左侧两张图中，林娇娇身着粉色汉服，头戴发饰，面带微笑，姿态优雅。右侧两张图中，林娇娇换上白色汉服，同样面带微笑，姿态端庄。图片与上下文关系紧密，直观呈现了角色服装造型的前后变化，说明了在角色设计过程中，通过持续向AI提出需求、人工反复修正提示词及不断雕琢细节，最终确定了服装造型。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OTE2ZWYxZTdkY2Y1YTYxZjEwYWE3MTc3NzM4Y2VjMGFfZjk5NTA3NzAzODE5MjBhMWQ0ZjZiNmVjNWQ1ZTczNDFfSUQ6NzY1ODUxNDk5MzQxNjY4NjU3OV8xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM)

**即梦生成的脸往往偏向大气、温婉风格，而且脸型较为相似。于是，尝试使用Z-image，最终找到了一款合适的发型与脸型。**

![图片展示的是林娇娇角色的最终造型。她身着淡粉色汉服，外披同色系长袍，腰间系有白色腰带，下身搭配淡粉色长裙，裙摆处有精致刺绣。发型为高束发髻，发间点缀金色发饰。林娇娇面带微笑，双手轻握于身前。此图与上下文紧密相关，是通过Z - image找到的适合林娇娇发型与脸型的造型，是角色设计过程中服装造型不搭问题解决后的成果展示。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=Mjg2MzlmZTJhOTg5Y2Q3OGIxMGI4YzAwMzg2OTE1NmFfZDYzNmMyM2QwOTgzZjU0NThmNWQxYWQ4OWIwZDcxYzVfSUQ6NzY1ODUxNDk5NDU3NjgzNzU2M18xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM)

**精细化调整造型**

<table id="doxcnOEURSXQ6vZnHPK94FrRMkg"><colgroup><col/><col/><col/></colgroup><tbody><tr><td vertical-align="top"><img id="doxcnGLwLY9GtUIqUNv9qVkcKfb" name="6ace7e6b3114ec5a33dcd46b57fff7c3.png" alt="图片展示的是林娇娇角色的定稿形象。她身着粉色古装，头戴精致发饰，发型为高挽发髻，面带淡妆，表情端庄。此图与文档中角色设计常见问题部分相关，用于说明在服装造型不搭问题上，通过使用Z - image找到合适发型与脸型后，再进行精细化调整，最终得到林娇娇的定稿形象。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZDljZmI0MzJhNzFhOTY5MTA5ZmMxYTUxNWIyOGRmNDJfNmVkNzllYWNmMjgzNzA4YWQxY2FjZWI5OTA5ZTAxN2ZfSUQ6NzY1ODUxNDk5MjY1MTg5Nzc5NF8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="WJ1cbAMcvoDgUqxoN2LcstwQnrd"/></td><td vertical-align="top"><img id="doxcnzwEycTy61xBc8gYqtED4mg" name="c11b7d993e9d9e677c4686f34ac0ac22.png" alt="图片展示的是林娇娇角色的定稿形象。她身着粉色汉服，外披浅粉色披风，腰间系有金色腰带，头饰为黑色发髻，两侧有蓝色装饰物。该图片与上下文紧密相关，是上文提到的尝试使用Z - image找到的适合林娇娇发型与脸型的服装造型，是角色设计过程中精细化调整造型后的成果展示。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZjcxNDM5MGFlNjQ1NTQ3OWQxMDllYTFlNmM5YjY2M2ZfN2QwMGUwMGNjZDIxMTM2MzM0ODBmZWNiNjVmZjRjNmNfSUQ6NzY1ODUxNDk5MzMyNzA4MjQ2Ml8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="KaRUbKHSKofvMBxyBiKcUIgnnKc"/></td><td vertical-align="top"><img id="doxcnf9R3ctXijlViKK9QeDlGQf" name="8390a02b0e6c4cd2a939a74f37e87f54.png" alt="图片展示的是林娇娇角色的定稿形象。她身着粉色古装，外披淡粉色披风，内搭浅粉色上衣，腰间系有淡粉色腰带，腰带上有金色花纹装饰。头戴黑色发髻，发髻上插有金色发簪，发簪旁有粉色花朵装饰，耳垂垂下金色耳坠。背景为浅灰色。该图片与上下文紧密相关，是通过精细化调整造型后，林娇娇角色最终呈现的定稿形象，体现了角色设计过程中对服装造型的反复雕琢。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NGY0ZDgxYTBiODUwMTZiOGEwMjNkOGQ1OWUwMDUxMDhfZTBkZjUzZjhlYmE5YTg2ZDA0MDUzN2U1ZmI2ZTgzOTlfSUQ6NzY1ODUxNDk5Njc0NTM3NDcwOF8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="LtuibqsjMoB3lIxpdchc3DFZnUe"/></td></tr></tbody></table>

**林娇娇定稿：**

![图片展示的是林娇娇角色的服装造型。她身着粉色汉服，外披同色系披风，披风上有金色花纹装饰。头戴黑色发髻，发间点缀着黄色花朵。耳垂垂着长耳环，脚穿粉色鞋子。此造型是通过使用Z - image，尝试多次调整后最终定稿的，体现了角色设计中服装造型不搭问题的解决思路。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NmUzNWI3NmUwYWQ2M2ExMjMxZWFhZGIxZWUwZTA2MjNfNzI2ZjA2YWEzYzY2NTJhZGM2MGUyYWI1NGRjYmQ1ZThfSUQ6NzY1ODUxNTAwNzAxNzUyMDA5MF8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM)

其余角色皆是通过这样的方式打造出来的： **持续向AI提出需求，人工反复修正提示词，并且不断雕琢细节。** 

### 2、人物比例问题

<table id="doxcnX7Ylxi4HLdEcY2Hk5P1oHf"><colgroup><col/><col/></colgroup><tbody><tr><td vertical-align="top"><img id="doxcnioRPhxcxhuLobJOAHjHtBd" name="5b00504a63457fa8b89dd1c90cbda243.png" alt="图片展示了一位身着紫色古装的女性角色。她头戴精致的头饰，身着带有金色花纹的紫色长袍，腰间系有黑色带子。画面背景为灰色，人物姿态端庄，面带微笑，整体造型典雅。该图片与文档中关于角色定妆照要求至少有一张全身正面照的内容相关，直观呈现了角色的全身形象，符合后续生视频时远/全景画面对人物全身形象展示的需求。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YTZhZmI1ZWZhYjdiN2ZmZWEzZjI4MTRiY2Q3YmI4OTBfNjcwYmUwOWE3N2I5ZWVhMTRhNjA5ZDlkMWY3YTM1NzlfSUQ6NzY1ODUxNTAwODg2Mjc1MTY5OF8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="FlHYbsjOso2jUxxHcfTcUpPVnge"/></td><td vertical-align="top"><img id="doxcnMnkBLSahevMfa57abNy5sc" name="de47268d842e716a3045a6c20173c8f7.png" alt="图片展示了一位身着黑色西装、搭配黑色长款外套的男性角色。他双手插兜，面带微笑，站姿自然。背景为深灰色，与人物服装颜色相呼应，整体画面简洁大气。该图片与文档中“角色定妆照要至少有一张全身正面照”的要求相契合，直观呈现了角色全身正面照的样式，为后续生视频时展现人物全身形象提供参考。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ODFhZjZlZDVhMDIyYjc5ZDMxOGVmY2RmODdjYTlmNWVfZjMxMjg5NzJhMDdmOTg5M2JiZDk4MTdmZTZiNDJlMjhfSUQ6NzY1ODUxNTAxMDA0OTY5MDU5M18xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="RkCGbQ7GLoV7TrxVExVcSBS8nGb"/></td></tr></tbody></table>

角色定妆照要 **至少有一张全身正面照** ，不能只有半身照。后续生视频的时候，一些远/全景画面是需要展现人物全身形象的。

在创作过程中，务必使 **人物身材比例尽可能契合大众审美标准** 。将人物在画面中尽可能放置于居中位置，确保视觉焦点突出。同时要着重注意，不能出现腿短的情况，以营造出和谐、美观的视觉效果。

所以，在提示词里应尽可能体现这些关键要素： **采用全身构图，让人物以自然站立的姿势呈现，并且具备二八身材比例** 。倘若无法生成全身照，那么在提示词中需 **对鞋子或脚部进行相关描述** 。

### 3、美观度的问题

对于真正面向大众的平台内容来说，“朴素”与“难看”是两回事。朴素可以是干净、清爽、低调，而难看往往是比例不协调、表情僵硬、色彩脏乱。

可以给角色设计设置一份最基础的检查清单：

**缩略图检查** ：把图缩小到手机竖屏上 1/6 高度，看一眼是否能认出人物轮廓；

**表情检查** ：眼神是否对称，有没有一只眼睛飘向奇怪方向，嘴型是否自然；

**色彩检查** ：整体是否灰脏，是否出现大量混杂的中间色，让画面看起来“蒙了一层灰”。

AI 再强，也只能放大创作者本人的审美。对标优秀国漫 / 短剧 作品，持续做对比，是提升这部分的最好办法。

比如，在生成女主重生之前落魄潦倒的造型时，AI最初给的方案是基于原造型的提示词的基础上，让她变得落魄、脏乱。

大家不妨想想，这样的效果能算得上好看吗？

![图片展示了两位身着古装的人物形象。左侧人物身着淡紫色长袍，内搭浅色衣物，下身是白色褶皱裙，头戴发饰，整体造型较为精致。右侧人物则身着浅色长袍，内搭白色衣物，下身是深色褶皱裙，头饰较为简单。两人均盘起头发，面带淡妆，表情各异。此图与上下文关系紧密，是对作者脑海中浮现的“虚弱、病美”人物造型的直观呈现，帮助读者更清晰地理解角色设计的设想。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OGRhMmY4YWJmNzAxNzRlMTI2MWJmMGY4NWNlMjlhNjRfM2MwZGY4NGRiNzI0OTRmNGU4N2IwZmQwZjFmMjUwNWZfSUQ6NzY1ODUxNTAxMzEzNjU5OTk5Ml8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM)

由此我们必须再次坚定一个认知： **AI 本身并不具备审美能力，最终产出成果的审美水平，完全取决于你的审美导向。**

于是我在脑海中反复构想，思索着究竟该是怎样的造型。

最终，眼前浮现出这样一幅画面： **一位身着简约素色睡衣长袍的人物，头发随意披散着，头上的钗环全都卸下，呈现出一副虚弱、的病美人的形象** 。

于是就要跟AI继续提要求：

![图片展示了一段关于角色设计的对话及设计思路。用户希望沈宁是病危状态，身着素白睡衣，面无钗环妆容，呈现虚弱病美形象。AI给出设计思路，认为沈宁前世最悲惨、最病若青青，是被剥夺体面的弥留病人。并为沈宁在第一集柴房受虐场景定妆，给出英文提示词，描述其极度衰弱、面色惨白、眼窝凹陷、嘴唇干瘪等特征，还提及衣着为古代素白色睡衣。此图与上下文紧密相关，是用户对沈宁角色设计要求及AI反馈的呈现。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZjI3YWE2NWQ1OTU5ZjQ4Y2QyOWMxM2YxMjlhODc2NmFfNjRmNjZjM2IyMDVmOGE1YTU3NjA4M2I3MmYzY2Q1YzlfSUQ6NzY1ODUxNTAxNTAwNzI1OTYxMF8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM)

模型对于提示词的理解，有时会显得过于夸张，且偏向刻板印象，所以需要持续调整。就像“面色惨白”“极度病弱”这类词汇，经其生成的效果往往会夸张得超乎想象。

<table id="doxcnA2tE57yCoLA4hR7Vd8wDJb"><colgroup><col/><col/></colgroup><tbody><tr><td vertical-align="top"><img id="doxcnETZRBJnh2Uv3QZsHxeQP6b" name="0b27754c5d6e3146009c1cba2b93de22.png" alt="图片展示了换脸后的角色定稿效果。画面中，角色身着白色长袍，袍上沾有血迹，头发散落，面部表情显得病态，整体呈现出一种诡异的氛围。该图片与文档中“换脸，得到如下定稿”的内容对应，直观呈现了在AI模型处理下，对“面色惨白”“极度病弱”等提示词的理解效果，体现了模型在理解提示词时可能存在的夸张和刻板印象问题。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MTRhYTYxMWQxYmI5NTMyNTBjZDkwZmIxZGIzMzUzNmRfY2VlNmE5ZTY3M2JjNTdkYmZhYmNlOTRjYjRiZmM2ZjJfSUQ6NzY1ODUxNTAxMjMyMzExODA1NF8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="DIyAbCeoCoXWD3x9QBUcG63Snnf"/></td><td vertical-align="top"><img id="doxcnv3tXWSIxHyYgx6SwX81QFc" name="acb90121767c34ab1049cf5e8ff1dda5.png" alt="图片展示了一位身着白色长袍的女性，长袍上有血迹，长发随风飘扬，面带严肃表情。此图是文档中“角色设计常见问题”部分关于“美观度的问题”下，对AI换脸后得到的定稿示例。文档提到模型对提示词理解有时会过于夸张且偏向刻板印象，如“面色惨白”“极度病弱”等词汇经其生成效果会夸张超乎想象，此图即为换脸后的效果呈现。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YjEwMTI0YjE3NmFkMjhjZmQ2ZmI1ZTAwOTFkNjdhYThfZjJlYzNjNWI0MjQzODU3YTRmN2M3ODJkZmZlZmNlZTRfSUQ6NzY1ODUxNTAxNDczNDg0MjgwOV8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="J8KRbRAQWo1VPuxF25ccbz5mnuh"/></td></tr></tbody></table>

**换脸，得到如下定稿：**

![图片展示了一位女性角色的换脸定稿。她身着白色长袍，长发披肩，面带血迹，表情凝重。画面分为四部分，左侧为面部特写，右侧分别呈现其正面、侧面和背面的全身照。该图片与上下文紧密相关，是针对角色设计中美观度问题，通过与AI沟通后得到的换脸定稿示例，用于说明在角色设计时需持续调整AI对提示词的理解，以达到更符合预期的效果。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NDFkODE3M2EzY2RmYjY3YmYwMzM0MGJjYTIyNGUyNjRfMjhkZTAzMTEzZGZlNDVhOTI4NDY3YTc0YmVkODJjYTNfSUQ6NzY1ODUxNTAxNTEwMzgyNjkwNF8xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM)

### 4、其他问题

<table id="doxcnz3UdRzUw8oPa5MtRirp0De"><colgroup><col/><col/><col/></colgroup><tbody><tr><td vertical-align="top"><img id="doxcnGOkXwSN1WUNfCNeDqSx8Ef" name="df8d87d96fb337cd597ac7db6c9ff4a4.png" alt="图片展示了一位身着传统服饰的女性角色。她头戴精致发饰，身着淡紫色长袍，内搭白色上衣，下穿白色褶皱裙，脚穿紫色鞋子。双手持一把白色团扇，面带微笑，直面镜头。该图片与文档中角色设计常见问题部分相关，用于说明角色图不要带有其他背景，全身定妆照尽可能保持站立，直面镜头的要求。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YzM4MTE5OGM2MzViYmEzYjU3ODA0NThjMDU4NGRlOTVfZmFkZmNlM2ZlYWI0ODQ3YTU1NDJhYzQ1YmU0ZGE1NGFfSUQ6NzY1ODUxNTAxNTEwMzk5MDc0NF8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="Tuy8bhMc2oNuC4xrE2ycKHEzn1d"/></td><td vertical-align="top"><img id="doxcnRSVcuJGNqGqpYCZ7RMdSGf" name="6e2f6ee5de17036b7b94eb706e95bbd6.png" alt="图片展示了一位身着传统服饰的女性角色。她头戴精致发饰，身着淡紫色与白色相间的长袍，腰间系有白色腰带，脚穿白色鞋子。背景为古风建筑，两侧有柱子，远处有树木和花朵，营造出古典氛围。此图与文档中角色设计常见问题部分相关，用于说明角色图不要带有其他背景，以避免在生成视频时产生影响。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MzNhMzkwNGYxN2Q2YTFhYzI2ZGEzNTg2ZTI5OTE0MjdfMjY3MWE1OGJiYzBjYzc4MmQ1ZTdkODk2OWY2ZmU4MWRfSUQ6NzY1ODUxNTAxNTU3MTE5Njg5NF8xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM" mime="image/png" scale="1.000000" src="QfEubDQ0PoTyurxpEEsc54Ujn9e"/></td><td vertical-align="top"><img id="doxcn1WPIA56giv58DVQlMLA2cd" name="c90daa97672cb526f6491c50ad2dded2.png" alt="图片展示了一位身着古装的女性角色。她盘着发髻，头饰精致，身着淡紫色长袍，内搭白色上衣，下穿白色长裙，脚穿绣花鞋。角色图背景为纯白色，角色保持站立，直面镜头。此图与文档中关于角色设计常见问题的说明相关，用于说明角色图不要带有其他背景，以避免在生成视频时产生影响，且全身定妆照尽可能保持站立，直面镜头。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MmMwM2RjMDQ3NWM1OWU3ZmUyMjU5ZmFkMjdlNTUwMGNfODA0MTUwNjcxNDNlOWIwNzI1ZmM0YWJjN2M4Yjc1ODZfSUQ6NzY1ODUxNTAxODQ4ODc2MTMxNl8xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM" mime="image/png" scale="1.000000" src="AGcJbbOnOoIL1OxckSDcutBon6d"/></td></tr></tbody></table>

除非整集角色都拿着这个物件，不然角色图尽量 **不要带有任何物件** 。

角色图 **不要带有其他背景** ，否则在生成视频的时候有可能产生影响。 角色的全身定妆照尽可能 **保持站立，直面镜头** 。

## 五）角色三视图及四视图资产

在传统动画流程中，人物三视图与表情设定，是角色设计阶段的最终成品。它并不直接出现在画面中，却直接决定后续镜头能否稳定产出。

于是在确定好人物的全是正面图之后，往往要生成一张 **脸部特写的图+角色的三视图** ，这也是我们常说的“ **四视图** ”

**提示词如下：**

> 生成全身三视图以及一张面部特写。(最左边占满 1/3 的位置是超大的面部特写，右边 2/3 放正视图、侧视图、后视图，二八身材比例)，纯白背景。真人写实风格。

注意：提示词要描述画风风格，不然可能会导致统一图片风格不一样。

![图片展示的是角色三视图及四视图资产的最终呈现效果。左侧为一张紫色古装女性角色的图片，标注为“01沈宁正图”，尺寸为2304 x 4096。右侧是引用该节点生成的选项，包括文本、图片（海报、分镜、角色设计）、视频、视频合成（Beta）、音频、脚本（Beta）。该图片与上下文关系紧密，是文档中介绍角色三视图及四视图资产生成效果的示例，用于说明生成图片顺利通过合规校验后，可在libtv中自由生成真人视频的操作步骤。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NDA1OTNmODk1MTZlNGZmM2FjNzhlNjhkZTIzNDI2NDlfNGI4ODZkZjhlYTM4YzVjYzRkNTM2NWZhNTg4OTA5OGRfSUQ6NzY1ODUxNTAxOTc2Nzk0MjExNl8xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM)

![图片展示了角色三视图及四视图资产生成界面。左侧为角色全身图，右侧是图片节点。下方有“Lib Nano 2”“21:9 · 2K”等参数设置，以及“生成全身三视图以及一张面部特写”等提示词输入区域。画面中用蓝色框突出显示了“生成全身三视图以及一张面部特写”等关键内容，还标注了“优先使用香蕉2模型”“21:9或者16:9都可以，2k分辨率”等信息。该图片与上下文介绍的资产构建中角色三视图及四视图资产生成相关，展示了操作界面及参数设置。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NzA1MGFjYWIxNWY4MzIzZDJjN2I2NWI3YzNmMmE0MGZfNGNlMDg1NDdkNzAwOTE5MTg3YzFhNGEyNGNiZjI0ODRfSUQ6NzY1ODUxNTAyMDUzNTQ2Njk4MF8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM)

最终呈现效果如下：

![图片展示了角色三视图及四视图资产的最终呈现效果。左侧为角色正面近景，黑发高束，头戴金色发饰，身着紫色古装，耳垂有白色流苏耳环。右侧从左至右依次是角色正面远景、侧面远景、背面远景，均身着紫色古装，搭配白色内衬，整体画面背景为纯白色，角色姿态优雅，与上下文介绍的资产构建中角色三视图及四视图资产相契合。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MjVkMzBiN2E4ODM5YWYzMDc2NDdhYzMxNTllNDE5M2ZfNjU4NTIxMTY3Y2VlMmNmOTUxMDMwZTAzNDFmMGMzYWRfSUQ6NzY1ODUxNTAyMTgzNTY2ODQxMl8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM)

若想生成真人视频，还需完成最后一步操作。具体做法是右键点击“ **Seedance 2.0合规校验** ”，只要图片顺利通过校验，就能够在libtv中自由生成真人视频。一般来说，只要生成的图片不与明星撞脸，基本上AI所生成的图片都能通过。正是基于这样的机制，libtv目前放宽了对真人审核的限制，这也是我们首要推荐libtv的原因所在。

要是打算在 **即梦** 中使用 **seedance 2.** 0生成视频，很可能这张脸部特写难以通过真人审核，这种情况下就需要针对图片做其他处理，关于这部分内容，我们会在下一节课详细讲解。

![图片展示了在即梦平台中对图片进行处理的界面。画面左侧是一张人物脸部特写图片，右侧是该图片的缩略图。在缩略图上点击后弹出下拉菜单，其中“Seedance2.0合规校验”选项被蓝色框和箭头突出显示。该图片与上下文紧密相关，上下文提到在即梦中使用seedance 2.0生成视频时，脸部特写可能难以通过真人审核，需针对图片做其他处理，此图即展示了在即梦平台对图片进行合规校验的操作步骤。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZDIzMTUzNDIzNWVkNGVlYTQ1ZjM0YmViNTM1ZTllZTBfZGRjYzYwMTgxMWQ4YTAyNTU3YTlkN2FiODZmMjhiYmJfSUQ6NzY1ODUxNTAyMTY1NTQyODA0NV8xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM)

<table id="doxcnppo9iJ6Ma8nW3EWW5aK91b"><colgroup><col/><col/></colgroup><tbody><tr><td vertical-align="top"><img id="doxcnhocF76yqv2bdJXvKRZn9Nf" name="81ecf3d9686dfe4124562e2425443d30.png" alt="图片展示了角色三视图及四视图资产，左侧为一张脸部特写图片，标注“图片节点23·校验中”，右侧是同一角色的三张全身图，分别从正面、侧面和背面展示，角色身着紫色长袍，头戴发饰。该图片与上下文紧密相关，上下文提到在即梦中使用seedance 2.0生成视频时，脸部特写可能难以通过真人审核，需针对图片做其他处理，此图可能是在说明处理前的图片状态。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MDllZjA0OGQ5NjczZGYwN2ExYzU4YmJmMDZkNmE5ZTFfYWMzMDhjMDRmZDUyYmVmZDY3YjZiZTM5NjYwZGNlOGVfSUQ6NzY1ODUxNTAyMDMwMTA5MzgzNl8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="J2E7b70wDoObB9xFfihczSfKn8d"/></td><td vertical-align="top"><img id="doxcnjZ9XRBtXiOChMvI40x23kg" name="f8e6dd1a3767a50c6b7a5b80847ecb14.png" alt="图片展示了即梦平台中素材审核通过的提示界面。画面中有一张人物脸部特写图片，图片下方有“图片节点2”字样及一个蓝色的“眼睛”图标。上方蓝色框内显示“素材内容已合规，可用于Seedance2.0视频生成”。该图片与上下文紧密相关，上下文提到在即梦中使用seedance 2.0生成视频时，若脸部特写难以通过真人审核，需针对图片做其他处理，此图则说明审核通过情况，为后续处理提供参考。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZGIxM2E4ZjZiOGYxNjg5Nzk2MGQxZGVhYTY2NTEyMjhfNmI1MDI0YjJmNmNhZTBlOTI1ZThiYmJhMGRlYjgwMzlfSUQ6NzY1ODUxNTAyMTU4NDM4NzA0MV8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="QK4DbYWeuonO8txRZLUcudhGnTa"/></td></tr></tbody></table>

## 六）场景设计

角色解决的是“谁”，场景解决的是“在哪”。场景并不仅仅是“背景图片”，更是一种“空间化的叙事工具”。

### 1、了解剧本

在进入 AI 绘画之前，先不要急着画图，而是做一个类似下面的表格，把全剧/本集的关键场景找出来。

同样通过 **西羊石-视觉资产设计中心** 这个智能体，可以轻松得到场景设定库信息:

![图片展示了西石羊第四期SOP中场景设计的场景设定库内容。包含两处场景设定，场景01为阴暗柴房，主体是侯府偏僻角落的木质柴房，室内夜晚，陈设凌乱，光影色调氛围压抑、冷酷、阴森；场景02为侯府前厅，主体是气派奢华的古代侯府正厅，室内白天，陈设精美，光影色调氛围富丽堂皇但暗藏剑拔弩张的紧张感。这些设定为后续的AI绘画提供了场景基础。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NmY3Y2Y2MzYxNDViMmNmNTU5MmMzYTU2NjhhY2NhNDFfN2FlMTMzNWI4OGIwOGE0MjRkNGQ1ZjdiN2Y3YmNmNzlfSUQ6NzY1ODUxNTAyMjAyODkwMTM0Nl8xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM)

剧本的场景主要有两处。一处是女主重生前的 **侯府柴房** 。一处就是重生后的 **侯府正院的会客厅** 。

### 2、场景设计原则

即便运用 AI 辅助设计，传统场景设计的若干原则依旧行之有效：

- **景别** ：场景应具备较强的容纳性，尽可能采用全景图或超广角镜头，以便涵盖更多内容。
- **三视图 / 正反打** ：依据不同角色的站位情况，同一场景内可能需要呈现不同视角的场景画面。
- **无人物要求** ：在场景设计图中，务必避免出现任何人物。因为一旦场景图中有人物，后期生成过程中，这些人物可能会被带入相应场景，进而干扰我们期望获得的分镜图效果。

### 3、场景的优化

场景的打磨跟角色打磨的基本方法是一样的。除了美观外，就是要要符合剧本的设定。

剧本中是侯府的柴房，但AI给的初版提示词生成的图过于破旧，连古代乡下的杂物间都不如。

<table id="doxcnFgf71JRx4uGJHHr5VlenLc"><colgroup><col/><col/></colgroup><tbody><tr><td vertical-align="top"><img id="doxcnpCjIyMFPEw5IhqgMsoXzXf" name="2466f11e1226d7af752cfe53b1b84b8d.png" alt="图片展示的是剧本中设定为侯府柴房的场景。画面中，柴房内光线昏暗，地面散落着干草和木柴。左侧有一扇老旧的木门，门板上布满裂痕。门后有几道光线斜射进来，形成光束效果。右侧墙上挂着几把农具，墙角堆放着干草。该场景与上下文提到的初版提示词生成图过于破旧，不符合古代乡下杂物间标准的情况相呼应，是经过多次修改后得到的版本。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZGViOGMxYjQ4NDQ5MzlhNWZhMzNjZTc3YzBiYzg5NGRfMjQ1MWM1NzBiOGQ4NDMwOTcwNzE4ZGU1Zjk4NGY5ZWNfSUQ6NzY1ODUxNTAyNDgzMDQzNDI3Nl8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="HFVebmV5toyO0ixbdv6cBRYGn3B"/></td><td vertical-align="top"><img id="doxcnERU4yax8zWMV3QsVAOTQef" name="4e29a8ad2330c9b2dcb43e41874fa472.png" alt="图片展示的是经过多次修改后的场景设计图，为侯府的柴房。画面中，柴房内摆放着整齐的木柴和稻草，木柴堆放在高处的架子上，稻草则装在编织的竹篮中。左侧有一扇木门，门缝透出亮光，地上投射出光斑。房间内有木质柱子和砖墙，整体色调偏暗，营造出古朴的氛围。该图与上下文关于场景设计的优化内容相关，直观呈现了优化后的场景效果。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MjY5NzQ2MTE2M2RlYjlmNTAzYzc1YWQzYjEyZTY3YTBfYjdjMDcxYzBhNDMxZTljNjM0ZmQ2MjQ5NjEyNWZkZjZfSUQ6NzY1ODUxNTAyNDMzMTQ1OTUyNF8xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM" mime="image/png" scale="1.000000" src="AvcJbWgIBo4GWOxPxt8csVMCnjf"/></td></tr></tbody></table>

![图片展示的是AI生成的柴房场景图，与文档中对柴房场景的描述相关。文档提到初版提示词生成的图过于破旧，不符合大人家的柴房标准，需重新生成。图片右侧是柴房场景图，左侧有提示信息，指出柴房画出的图目前长这个样子，有点像古代乡下的柴房，不符合大人家的柴房标准，需重新生成。该图直观呈现了AI生成的柴房场景，与上下文对场景的讨论紧密相关。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YmE3ZmVjMTAxZTFmNGZlMDk3NDhhOWMxYjcwYWQxN2JfYzU2ZjU0MzIxMTVmNTQwMGJkODk4MzFjMzg0NTNlN2ZfSUQ6NzY1ODUxNTAyODM4NzA1NjYyM18xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM)

经过多次修改后，得到如下版本：

<table id="doxcnEKUCve30QFdDnQVLyvNSte"><colgroup><col/><col/></colgroup><tbody><tr><td vertical-align="top"><img id="doxcnoZi5rZmvc4yDOUD0Phqxmx" name="2a2c86ca1dddd1d562a08af86e40635d.jpeg" alt="图片展示的是经过多次修改后的场景图，为侯府的柴房。画面中，地面铺满干草，四周是木质结构的柱子和墙壁，中间有一扇较大的木门，门上方有三个小窗户。该图与上下文紧密相关，是对剧本中柴房场景的优化呈现，原初版图过于破旧，此图在多次修改后更符合古代乡下杂物间的氛围，体现了场景设计的优化过程。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YTU0ZGIwMjRhYzhjNjYyMGFlY2ZmNjRlZGRlZjcxMGZfYzMxY2MyZDUxM2M4Yjc0MWM4ZDMwMzJlODZhZjNmNGVfSUQ6NzY1ODUxNTAyNzc0NTQ5MTkzMl8xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM" mime="image/jpeg" scale="1.000000" src="K8i8b9ndQog6SYx9JCrc79IZnad"/></td><td vertical-align="top"><img id="doxcn9dnGFc5cWxIU7dy7mBE8fJ" name="77a841d9bfe35a80addb53cea0cc2f46.jpeg" alt="图片展示的是经过多次修改后的场景图，是侯府的柴房。画面中，柴房内摆放着稻草，地面和墙壁由木头构成，门半开着，门外是夜晚的庭院，有闪电划过，庭院中有一座建筑。该图与上下文紧密相关，是对剧本中柴房场景的优化呈现，原初版图过于破旧，此图则更符合古代乡下杂物间的氛围，体现了场景设计的优化成果。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MWI5NjViOTI5YTY0NzdmZTA1NDMwYmQ4MmRhMWE1Y2VfZTVkZDNmNmZhNTIzMTBlMGIxZThhMzkxNTc2MDdlNzZfSUQ6NzY1ODUxNTAyODkxOTg2NDI5MF8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/jpeg" scale="1.000000" src="GObwbbsxEoDCNEx1J4CcHPz6n9e"/></td></tr></tbody></table>

![图片展示的是经过多次修改后的场景图，为侯府的柴房。画面中，柴房内摆放着稻草，地面湿润，四周是木质结构的墙壁和柱子，显得古朴而破旧。左侧有一扇木门，门上雕有花纹，门旁是窗户，窗外风雨交加，闪电划破夜空。该图与上下文紧密相关，是对剧本中柴房场景的优化呈现，以更符合古代乡下杂物间氛围的初版提示词生成图。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MjRlMTkwNjc1YWY0YzNkNTY2OWNlNTIwZTRkZTZhZGRfYTNlNmIzODM3ZmM3YWNjYjY3NjkwYzNkMmNkOTZlN2FfSUQ6NzY1ODUxNTAyOTAxMzc3NzM2Ml8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM)

是否制作多个视角的场景，需视剧本需求而定。一般来说，若使用seedance 2.0直接生成视频素材，一张全景场景图通常就已能满足需求。

<table id="doxcncpV5HHngUqtuRJnNxhwqCb"><colgroup><col/><col/></colgroup><tbody><tr><td vertical-align="top"><img id="doxcnNlauArEktbX8pqZPRmsUJd" name="d269c3a3ed6e303661e0ac062b845190.jpeg" alt="图片展示了一个场景设计优化后的画面。画面中，一位女性角色躺在稻草堆上，身着白色上衣，头发披散，表情惊恐。背景为木质结构的房间，地面铺有稻草。右上角有“*AI生成，剧情虚构”字样。该图片与文档中“场景设计”部分内容相关，用于说明经过多次修改后得到的场景设计版本，体现是否制作多个视角场景需视剧本需求而定，若使用seedance 2.0直接生成视频素材，一张全景场景图通常已能满足需求。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=N2YyYjI5YWMyNGMyYWRjNDAyZTViNzYzMzdlMDA4MTFfMTYwYmZjNTVkYTBhZGI2ZjUyYTM2ZmU4OTQ2YTlmYzlfSUQ6NzY1ODUxNTAyODgyNzYzODc1N18xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/jpeg" scale="1.000000" src="OSy2bWdUXojVKUxtvGIcwSYZnqd"/></td><td vertical-align="top"><img id="doxcntVPoTQSc9ul2K3TtjTTk1b" name="d3d0acd0be0a5fcd87c6c70a71046634.jpeg" alt="图片展示了一对身着古装的人物，背景为古风建筑。女子身着粉色古装，头戴发饰，面带微笑；男子则身着深色古装，面带严肃表情。画面左下角有“西石羊AI视频”标识，右上角标注“*AI生成，剧情虚构”。该图片位于文档中“场景设计”部分，用于说明经过多次修改后得到的场景版本，体现其古风场景设计效果。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ODNkNTY5NWE5YmUyZjc5NDI1ZGNhNzU1ODU1ODMxOGJfZDMzODgxN2U2ZDFmZDRhMmM1Zjg4NjlmMjlmOTgxZjVfSUQ6NzY1ODUxNTAzMDIwNzY2MzA1NF8xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM" mime="image/jpeg" scale="1.000000" src="RYvTb156QozqU0xCOozclW6Xn4g"/></td></tr></tbody></table>

<table id="doxcn6JabK1Z6a6UREWr1q24kXf"><colgroup><col/><col/></colgroup><tbody><tr><td vertical-align="top"><img id="doxcnAtp5iOviALeKJaTXmQ4Pfb" name="9cbedf6d0e790b7112b2bc864f4c817b.png" alt="图片展示的是一个中式风格的室内场景。画面中央摆放着一张木制长桌，桌上摆放着绿植和茶具。两侧各有一张木制椅子，椅子旁配有小几。房间内有木质屏风，屏风后摆放着盆栽。地面铺有图案地毯，四周有木质家具和装饰。窗户上有木质格栅，窗外可见绿植。该场景可能是剧本中角色活动的场所，与上下文提到的场景设计及优化等内容相关。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OGIwYjIzZjMxYmE0MzI3MzVjOWQ1NGNmMDIxZTNiNjZfMjUwN2RjZTgyNmQ5MWVhYmNkMjA3MzIxNTAwNjlhNGVfSUQ6NzY1ODUxNTAzMjIwMzk4NzkzNV8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="Jaiqb1TA5ox7APxmkMgc22Z2nfe"/></td><td vertical-align="top"><img id="doxcnkVBkWAa4233Q5OKzIpdqwd" name="64d7b6c51ae81441d23b7c870dba164a.png" alt="图片展示的是一个室内场景，地面铺有图案地毯，两侧摆放着木质椅子。房间内有木质屏风和窗户，透过窗户可见室外的庭院，庭院中有树木和石雕。该图片位于文档中“场景设计”部分，用于说明经过多次修改后得到的场景版本，强调是否制作多个视角场景需视剧本需求而定，若使用seedance 2.0直接生成视频素材，一张全景场景图通常已能满足需求。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YTBmYjAzOGFmZDlkMjA0MGI0MzU0MmQ5YTFmMzdjMDFfMGQwMjA3MGM5OGZhNDUzOWZmMDMzZjgwMzkwMTM4ZTNfSUQ6NzY1ODUxNTAzMTA1MTA3ODYwM18xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="P0PObOjmpogNDrxQYGcchHUVnZf"/></td></tr></tbody></table>

<table id="doxcnGIG2zSzAvSW5MYq0i9Sezb"><colgroup><col/><col/></colgroup><tbody><tr><td vertical-align="top"><img id="doxcnIkaEVAL1r9NjbY5HeyIocc" name="e81cdc040c3b54b2acd3ef4e2850c5f2.png" alt="图片展示的是一个古装场景，画面中有三个人物。前景中，一位身穿浅色古装、头戴发髻的男子跪坐，面向画面右侧。画面右侧站着一位身着深色长袍、腰系棕色腰带的女子，她面带微笑，目光看向画面左侧。画面左侧站着一位身着深蓝色长袍、内搭白色长袍的男子，他面带严肃表情，目光直视画面右侧女子。背景为古风建筑，有屏风、桌椅等装饰。此图可能用于剧本场景设计的参考。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YTQxNDFhNGZjN2Y2NGEzOGFmOTY0NzQzN2MyYjBhOGZfYjk4OGY0MTZhYzNiN2Y1MmFhZTMxNzI4OWVmZTAzMjVfSUQ6NzY1ODUxNTAzMjA0MDgwMzI4OF8xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM" mime="image/png" scale="1.000000" src="Iy2UbZtwJoWJmixFmkHcK6Gjntb"/></td><td vertical-align="top"><img id="doxcnOVYD2lyl26O1EJavOcy0Jh" name="66dbfed589a8666c30e7faf4373235b7.png" alt="图片展示的是一个古装场景，一名女子身着淡绿色古装，头戴发饰，双手张开，背景为木质结构的建筑，两侧有雕花屏风，远处可见树木和建筑。画面底部有“侯爷”字样。该图片位于文档中“场景设计”部分，用于说明经过多次修改后得到的场景版本，体现是否制作多个视角场景需视剧本需求而定，若使用seedance 2.0直接生成视频素材，一张全景场景图通常已能满足需求。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MTMzZGM0Y2ZjNWZjNGRkMzFmNDkxY2U3NWI1NDZiODBfMDU3NjMzM2QzZWU5ZDhkOTIwMTQ0M2QyYzUyNDc0M2RfSUQ6NzY1ODUxNTAzNTI3NDE2OTMyNV8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="JfARbKVk1o1tFnxhabjcoXA1nvf"/></td></tr></tbody></table>

### 4、多宫格场景提示词直出

借助 **西羊石-视觉资产设计中心** ，能够迅速获取初版的场景提示词。

这里面包含两个版本的提示词，分别为 **正面全景图版本** 与 **四宫格机位版本** 。正面全景图版本仅生成一张正面的全景场景图，毕竟并非所有戏份都对各个视点的场景图有需求，许多戏份一张全景图便已足够。

**Seedance 2.0 视频模型** 的 **全能参考模式** 十分智能，在生成视频时会自动进行切镜操作，多数场景都能维持良好的氛围。

然而，对于那些对场景要求更为严苛的同学，不妨尝试使用四宫格机位版本的提示词，它能直接输出不同视点的场景图。最后，可依据自身需求在 libtv 中进行提取并放大处理。

![图片展示了M3 - 核心场景设计（Scene Prompts）中“阴暗柴房（单张全版）”和“阴暗柴房（四宫格机位版）”的场景设计提示词。前者描述了室内场景，有木柴、木板、破洞等元素，画面以冷色调为主，有丰富的环境纹理与材质细节。后者在前者基础上，增加了四宫格布局，每个画面分别呈现不同角度的场景，如正前方、左侧、右侧等，还对画面中木柴、木板、破洞等细节进行了具体描述。该图片与上下文介绍的在libtv中创建图片节点、选择GPT Image 2模型生成多宫格场景提示词等内容相关。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZWViOWQzNmJkN2VjYjRiYTM0N2QyY2I1NzlmYTEyMjlfMjJiNWNiYjkzMzc3NmY0Njg2YjBhYjVjYTQxYTc5YzRfSUQ6NzY1ODUxNTAzNTI0MDY2NDAyOF8xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM)

在libtv中，创建图片节点，选择最近极受欢迎的 **GPT Image 2模型（Lib Image），** 将四宫格提示词复制进来，选择 **16:9和2k画质** ，点击生成。

![图片展示的是一个生成图片的界面。上方有“图片节点25”标识，中间是空白的图片区域，下方是生成图片的提示词，描述了写实电影风格的古代侯府正厅场景，包含四格独立视角画面、巨大蓝色花纹地毯、对称式桌椅等细节。界面左下角有“Lib Image”标识，右下角显示“16:9 · 标准画质 · 2K”等参数，右上角有“1张”和“21”标识。该图片与上下文介绍的生成图片操作相关，是生成图片操作界面的呈现。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MTQ2MzlmMGZlMTYxYWE1ODhkZTIyMDQ5NDU0ZTYxYTZfYTYxMjJmMTBlNWZiMzNlYTIyYjRmNjdhMjQ1YzRkNjJfSUQ6NzY1ODUxNTAzNjk3MjgxMzI2MF8xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM)

可以看到，大体上各个角度的细节还是能够对得上的，室内场景相对比较复杂，一些局部细节（例如桌椅的摆放顺序）如果需要改动可以单独再用香蕉等模型进行微调。

![图片展示了多宫格场景生成的四宫格效果。画面中是一个室内场景，地面铺有蓝色带有花纹的地毯，四周摆放着木质家具，墙上装饰有屏风和挂画。上半部分画面展示了室内一角，有桌椅和挂画；右上角是整个室内场景；左下角是室内走廊部分；右下角是室内中央区域，有茶几和椅子。该图片与上下文关系紧密，是对上文提到的多宫格场景提示词直出生成效果的直观呈现。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OWVkYjE5NzNiZjBmODQ3NjJkNmRhZjVlMTZkM2M2ZjdfYTYwZjMyMDA1NDBkMzBmN2RjYTNiNWJiMTViYzNjNjNfSUQ6NzY1ODUxNTAzNjMzOTYwNDQwOF8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM)

单击生成的图片，点击上方的 **宫格切分** 选项，选择 **四宫格**

![图片展示的是在图片生成界面中选择宫格切分选项的操作界面。界面上方有“宫格”“多角度”“打光”“九宫格”“高清”“宫格切分”等选项，其中“宫格切分”被蓝色框突出显示。点击“宫格切分”后弹出下拉菜单，显示“4宫格（2×2）”“9宫格（3×3）”“16宫格（4×4）”“25宫格（5×5）”等选项，其中“4宫格（2×2）”也被蓝色框突出显示。该图片与上下文介绍的在图片生成界面中选择宫格切分选项的操作步骤相关，直观呈现了操作界面及选项。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MzMyYWM3MDkzNzkwZjVhYThkN2E4ZDFlNmRkNjBkODhfNjg5ZDg5NDBhODU5NTMxZGIxZGQ5Zjc1NDVjMDdlYTZfSUQ6NzY1ODUxNTAzNTcwNDA4NTQ2OF8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM)

然后点击 **创建生图节点**

![图片展示的是在Stable Diffusion WebUI中生成的四宫格图片界面。画面中呈现了室内场景的四个不同角度，包括地毯、桌椅摆放等细节。上方有“创建生图节点”按钮，表明已选中一个宫格。右上角显示“生成高清图片 +15 2倍”，表明可生成高清图片，且有15个生成任务，倍数为2。该图片与上下文紧密相关，是单击生成图片后，点击“宫格切分”选项选择“四宫格”后，点击“创建生图节点”操作后的呈现效果。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NTI0NzcyOTE0ZDMzM2I0Njc1MzgxNTdiMzQzODM0MThfZmJkZTU2Mzc4ZDQ0YTM2ZGJjMDk0NDYyYzhlNzZiOGVfSUQ6NzY1ODUxNTAzNjg5MzMzNDQ3Nl8xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM)

此刻分离出的图片，实际上只是对原本2k分辨率的四宫格图片实施物理裁切，其分辨率会降至原来的四分之一，画质因而会受到影响。所以， **还需再点击一次生成** ，使模型以从原四宫格分离出的这张图的模样作为参考，重新生成图片。如此一来，就能得到一张2k分辨率的清晰场景图。

![图片展示的是一个生成图片的界面。左侧有2048x1152分辨率的图片节点25，下方是生成的分镜图像。右侧上方显示“宫格生图1-2”，下方是2k分辨率的清晰场景图，图中为室内场景，有沙发、茶几等家具。下方文字提示“单独生成【第1行第2列】的分镜图像”。该图片与上下文关系紧密，是对上文提到的“还需再点击一次生成，使模型以从原四宫格分离出的这张图的模样作为参考，重新生成图片”操作结果的呈现。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YmQ2NTQyMzcxZmJiMTcyNjFiMGRkMzViNzQyOWExNGJfM2JjZjExNTMxNDhmMTJkM2Q5MDA1NTZkZWM1ZjQwNGNfSUQ6NzY1ODUxNTAzODkwMjQyMjQ2MF8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM)

值得一提的是，重新生成图片，可以换成价格更便宜的香蕉2模型。

![图片展示的是一个生成场景图的界面。左侧有多个场景图缩略图，中间是大图，右侧上方有“多角度”“打光”“九宫格”等选项。画面中有一个蓝色箭头指向“Lib Nano 2”模型，旁边文字提示“可以换成香蕉2，价格更便宜点”。右下角有“生成”按钮和数字“12”，表明可生成12张图片。该图片与文档中“多宫格场景提示词直出”内容相关，说明重新生成图片时可选择更便宜的模型。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OWQxMTVjOTg5MzNkNzI2NGM4NTVkNTU4MTUyODcxZjNfODAyZGNmNzVlMWY3NjQ5NzA1Mzg1OWJiMTI4MDc2YTBfSUQ6NzY1ODUxNTA0MTI3MTk1ODQ2OF8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM)

<table id="doxcn9QCgA1DJYtdtHsD4PodWcb"><colgroup><col/><col/></colgroup><tbody><tr><td vertical-align="top"><img id="doxcnrO4bq0eYbckCZrWS2hXxZf" name="d40dd67bd8fd86e44d82a48f92085612.png" alt="图片展示的是一个室内场景，地面铺有蓝色带有金色花纹的地毯。房间内摆放着多把木质椅子，椅子上有红色坐垫。背景墙上有山水画，两侧各有一盆绿植。房间两侧有屏风，屏风后有窗户。该图片与文档中“手动四宫格场景提示词模板”内容相关，可作为上传图，用于生成一张2*2四宫格场景多视角参考图，作为场景的唯一视觉依据。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YWI5NzAzZWQzMmQxZDRhZTAxNDA0N2NlNDk5MDcwNmNfYzFlNzZhMTlkOGVhOWYxNmU0Njk2ZTk5MzQ0ZTc5NDhfSUQ6NzY1ODUxNTA0MjEyNzY3ODQ1MV8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="AUffbECIpob9iqxtqjHcf7M1nvc"/></td><td vertical-align="top"><img id="doxcndxsiKuiuHger2ejfH9E9Kc" name="7c1112085bdf8106004a218310b3dfe8.png" alt="图片展示的是一个中式庭院场景。画面中，两侧各有一张雕花木椅，椅背上有精美的镂空花纹，椅间摆放着一张小茶几，茶几上摆放着茶具。庭院内有木质屏风和柱子，地面铺有蓝色带有花纹的地毯。远处可见一座古建筑，建筑前有树木和绿植。该图片可作为手动四宫格场景提示词模板中上传图的示例，用于生成四宫格场景多视角参考图。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OTY4NDJlMmViMzQ4ZTI4MjAyNWU1YmM1ZWE2NGI5ZTZfYmJhMmE1MzY2N2Y0NDdiNjAwNzdmMTBjYmM4NDg1YTJfSUQ6NzY1ODUxNTA0MDc4NTY4MTM5Nl8xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM" mime="image/png" scale="1.000000" src="YZeRbiOBnoXI4uxz4WzcnCv2njc"/></td></tr></tbody></table>

##### 手动四宫格场景提示词模板

> 根据上传图生成一张2\*2四宫格场景多视角参考图。上传图可以是任意角度，请将其作为该场景的唯一视觉依据。先根据上传图还原出同一个完整的三维空间，再生成四个标准视角：左上为俯拍视角，从正上方展示场景整体平面关系；右上为正向视角，从场景正面朝主体区域观看；左下为左侧视角，从场景左侧朝主体区域观看；右下为右侧视角，从场景右侧朝主体区域观看。四格必须表现同一个场景，所有元素的数量、相对位置、尺度比例、朝向、前后层次、材质和光影都要一致。对于原图未直接展示的区域，可以根据可见线索合理补全，但不要加入与原图无关的新内容。左右视角必须端正、稳定、清楚，不能歪斜，不能明显斜拍，也不能被柱子、树木、围栏、墙角、车辆、山石等近景物体大面积遮挡。整体保持同一空间、同一光照、同一色调和同一氛围，不添加文字或标签。

<table id="doxcn3GophIDmwT3SM40lThtpcd"><colgroup><col/><col/></colgroup><tbody><tr><td vertical-align="top"><img id="doxcnw5bUMCozt9Ps7tJxzL2i4g" name="903062d725f079a883cce3e43b54362c.png" alt="图片展示的是一个中式传统室内场景。画面中央摆放着一张长方形木桌，桌上有盆景，两侧各有一把木椅。两侧各有一张小几，上面各放着一盆绿植。房间内有木质屏风，屏风后有几盆绿植。地面铺着带有花纹的地毯。房间两侧有窗户，窗外可见树木。整体色调偏暖，光线柔和，营造出古色古香的氛围。此图与文档中关于多宫格场景提示词直出的内容相关，可作为场景设计参考。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NWYxYmY5NjM5ZDU4NWQwOWY3NTIzYzYxOWI4Y2QyZDJfYTJjMmY5YWI3MzkyMDVmZjgyOTM1MjAxYzdkYzUzODVfSUQ6NzY1ODUxNTA0MDg2NTQ1NTA1NF8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="GsIJb2MXLoQVaPxaNcZcFDqRnjf"/></td><td vertical-align="top"><img id="doxcntId7iwGSt9LpBGvjHEL4XB" name="f662059a3121ef06588e3ddbb27c94f4.png" alt="图片展示了多宫格场景，呈现了同一空间、同一光照、同一色调和同一氛围的室内场景。画面中设有木质家具，如椅子、茶几等，地面铺有蓝色带有花纹的地毯。房间内有窗户，窗外可见树木。房间内还摆放着绿植，增添了生机。该图片与上下文关于场景设计中多宫格场景提示词直出的内容相关，用于说明在原图未直接展示的区域可根据可见线索合理补全，但不能加入与原图无关的新内容。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MTEyYmEyNGQ4NjNiNzY0YmE0ZWIxYmFhZDZlNGQwYjdfZDU1MjEwOTgyYjAyNjExYWU1ZDVhOTYzNjQwYTBmNTJfSUQ6NzY1ODUxNTA0NDQwOTMzMDYzOF8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="LOHSbF3sNorfZexEoFpcdEF0n8e"/></td></tr></tbody></table>

### 5、LibTV全景图

如果只有单一的正面场景图，想要生成其他视角的场景图，可以在 **libtv** 里使用它内置的 **全景** 功能。

![图片展示了在libtv中使用全景功能生成的720度全景图界面。画面中呈现的是一个室内场景，有屏风、桌椅、盆景等布置，地面铺有蓝色地毯。界面顶部有“全景”“多角度”“打光”等选项卡，当前选中“全景”。右上角有截图、下载等操作按钮。该图与上下文关系紧密，直观呈现了在libtv里使用全景功能生成的场景图效果，说明其更适合室外场景构建，但对室内场景角度变化大时效果不自然。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZmEwMzBlYmM1M2QzZjI0OWYzNGYyMzQxOTM1NWE4NGNfMjhkZTRhMDc4MWI1OTFkODQ1ODM0YzdiMDRmYmEzNDVfSUQ6NzY1ODUxNTA0NDY2OTQ5MjE5Nl8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM)

会生成一个720度全景图，手动旋转到你想要的角度，点击上方的截图按钮即可。但对于室内场景，如果角度变化过大，畸变严重，效果不太自然。 **更适合室外场景的构建。**

![图片展示的是一个室内场景，可能是用于生成反打场景的参考图。画面中有一张铺着蓝色地毯的房间，房间内摆放着多把木质椅子，椅子上有红色坐垫。背景墙上有山水画，右侧有一幅挂画。画面右下角有一个蓝色边框的3D模型视图，显示了房间的三维结构。图片下方有提示词，要求描述全景画面并上传场景参考图，推荐句式为“生成/基于参考图生成一张xxx的T20全景图”。该图片与文档中手动生成反打场景的方法上下文相关，用于说明找到视觉锚点后生成反打场景的参考图示例。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YWQ0NWE3YjYwZWZiZTAwNzBhNTNiYjI1MTcxZGZjYjJfZmVlMTAxODM1Yjg4Njc4MGVhZWY3ZGNmZDAxODQ1MjNfSUQ6NzY1ODUxNTA0MzA4ODM3MDY0Ml8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM)

### 6、手动生成反打场景的方法

🌟 **基本逻辑： 找到视觉锚点**

只要根据下面的这套提示词公式，大部分复杂的反打场景都能够生成出来。

**提示词公式：**

> **起手式** + **风格** + **角度和构图** + **画面描述** + **环境氛围**

**起手式：** 参照图中的风格，生成一个反打场景图。

**风格：** 真人写实风格/3D风格/2D风格（可省略）

**角度和构图：** 从XX看向XX的反打视角，中心构图 **画面描述：** 前景是XX，前景模糊；中景是XX；聚焦在XX；背景是XX。 **环境氛围：** 整体环境的光影、色调等（可省略）

<table id="doxcnpGmhCcpgS9Ni1CNNNbBlYd"><colgroup><col/><col/></colgroup><tbody><tr><td vertical-align="top"><img id="doxcnimaPSNsKQMwkYf7Lzr07Lg" name="480da4525b129bf4cde57c28ce2b3b1d.jpeg" alt="图片展示的是西石羊第四期SOP中场景设计的LibTV全景图。画面以“XYS网咖”标识为中心，前景模糊，中景为带有蓝色和紫色霓虹灯环绕的弧形前台，聚焦在前台。背景是深色的室内环境，两侧设有拱形门洞，整体氛围科技感十足，光影效果突出。此图与文档中对场景设计的描述相契合，直观呈现了所设计场景的视觉效果。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YzM5ZjY3ZGIzOWQ5M2JjYmI4NjM1NmUxZTdlZjIzOWNfMmQzZWEwY2ZjYzYyMGRiZWM0YzA4NzdmZjI0Yjk4ZDFfSUQ6NzY1ODUxNTA0MzMwMjM2MjA4NF8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/jpeg" scale="1.000000" src="GVb3bUy2GotEXwxVtm4cxlvPnyf"/></td><td vertical-align="top"><img id="doxcnn5JHYu0juWK204OFUS5rTe" name="1996c397e7019f1225bb0be4e49ee78b.png" alt="这张图片呈现的是西石羊第四期场景设计里的LibTV全景图场景，属于真人写实风格的数字空间场景。画面采用反打视角的中心构图，前景是弧形操控台，台面上摆放着两台显示数据界面的电脑键盘与鼠标，还有堆叠的物料和一排饮品；中景是玻璃门区域，门上标注着“XYS网咖”，上方还有“出口”标识；背景是夜晚的城市建筑群，整体搭配紫色、蓝色的霓虹灯光，营造出带有科技感的电竞网咖空间氛围。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NzUyOTVmOGYyOTdiYmRiNmE5NzI2ZTkxYjcyZWMzODZfNjFkYmNlM2NkZDQxY2Q2ZDU2YjIxYWVjYzJhOWEzZmVfSUQ6NzY1ODUxNTA0Nzc5ODM0NDY1NV8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="F5ZWbwlbJoB9GfxeC5Ccdax8nDg"/></td></tr></tbody></table>

## 七）道具资产设计

道具资产设计，直接把AI给的提示词复制到Libtv中出图即可，根据我们认为这个道具的大致形象，可以选择不同的尺寸比例，一般用1:1即可。

![图片展示的是一个AI出图界面，用于设计道具资产。画面中是一把中国古代钥匙，单件物品，纯白背景，带有逼真的金属磨损痕迹，钥匙头部系着紫色丝带。下方有详细描述，包括材质、质感、背景等信息。界面顶部有“全景”“NEW”“多角度”等选项，右上角有下载、分享等按钮。该图片与上下文紧密相关，直观呈现了道具资产设计中AI出图的效果，帮助理解道具设计的具体呈现形式。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NDA0NDVhNTA4NmI3YWI3NDg0MjJlOGM4NGMxMjdkZDlfNDlmM2E5NTE5NzljOTY5MzA2ZWM5YzYyZDU3ZGUxOTdfSUQ6NzY1ODUxNTA0ODk2MDE1MDQ3M18xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM)

道具资产方面相对较为简单，但要留意古装剧需符合相应的气质。不能出现现代元素，同时也应尽量避免出现简体字。

<table id="doxcn4lECZfNEBkUV9g8UjaZ6Nc"><colgroup><col/><col/></colgroup><tbody><tr><td vertical-align="top"><img id="doxcnAKTGnuVdrqbwpaPIPm2Vmf" name="4fdf44063515e8b936b9f44b10cf9524.png" alt="图片展示的是一个古风道具，为长方形，表面有金色边框，中间是绿色背景，边缘有云纹装饰。中间大字“陆”以金色呈现，字体古朴。该图片位于文档中“道具资产设计”部分，用于说明道具设计时可从AI生成的图片中选出合适的，且强调道具设计需白色纯色背景，不能有污染画面的地方。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MzU4ZTE5ZjhiZjQ0ZmQ4MTc1YTM0NmEzN2MzMzI0NzFfYWFlNTlhMGFhYTMwZGQ4YzM0ZDlkMWQyZjc2NTY3NjJfSUQ6NzY1ODUxNTA0ODUxMTU1NjU3Nl8xNzgzNDAxMDkyOjE3ODM0MDQ2OTJfVjM" mime="image/png" scale="1.000000" src="KJUybgOeooFonIxEjbKcd029nPc"/></td><td vertical-align="top"><img id="doxcnuVIiHTpYqLTAH8x4qtJCIg" name="8045e6642f4ef454573076c744bec9f4.png" alt="图片展示了一把金色的钥匙，钥匙头呈心形，中间有四个小方格图案，钥匙柄上系着一条紫色流苏。该图片位于文档中“道具资产设计”部分，用于说明在道具设计时，要选择白色纯色背景且无污染画面的图片，此图即为符合要求的示例，可从中选出比较合适的图片进行使用。" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZThjOGM5Njc4ZTFiOTFhMzAyYmMyNTBlZDE3NmU3YWJfM2RjNTAzYmJlNGE0Y2QzMTc0MDdjNDE3ZjI1MWU3MDJfSUQ6NzY1ODUxNTA1MDI5Mzk1NTUxM18xNzgzNDAxMDkzOjE3ODM0MDQ2OTNfVjM" mime="image/png" scale="1.000000" src="Lcp8beTq2ohxa8xZH3UcGsH0njc"/></td></tr></tbody></table>

我们直接点击生成，从中选出比较合适的图片就行。

**注意道具设计也是要白色纯色背景。不要有任何别的污染画面的地方**

## 八）小结

本节我们围绕资产设计，搭建了一整套从文字到视觉的工作流。它的核心并不是“多会几个 AI 工具”，而是把传统影视与动画行业验证过的方法，迁移到 AI 短剧的生产线上。

> **角色设计** ：基于AI技术，从人物小传出发，精心打造契合剧情发展、逻辑合理、符合设定且满足审美需求的人物角色定妆照提示词。此过程需深度剖析人物性格、背景等要素，为后续定妆照创作提供精准指引。

> **定妆照与视图资产获取** ：运用 Libtv 等相关工具，并结合不同模型的特点与优势，通过反复尝试和对比，筛选出效果最佳的人物角色定妆照以及涵盖多角度的四视图资产，确保角色形象全面且立体地呈现。

> **多角度场景图生成** ：借助智能体与 libtv 等工具，深入探索并熟练掌握多种生成多角度场景图的有效方法。依据不同场景需求，灵活运用这些方法，为剧情营造恰当的环境氛围。

> **反打场景生成逻辑掌握** ：以核心提示词为基础，通过手动优化方式，深入研究并掌握反打场景的生成逻辑。通过不断实践与调整，精准把控反打场景的呈现效果，使其与整体剧情相得益彰。

## 九）第二次作业：为你的剧本设计角色、场景和道具资产

针对你剧本中 **待制作的那一集** ，需生成以下资产图：

1. **角色设计** ：绘制主要角色具有一致性的图片。具体涵盖正面、侧面、背面的全身三视图，以及脸部特写，全方位展现角色形象。

2. **场景图** ：创作该集所需的主要场景图，为故事搭建起相应的环境背景。

3. **道具图** ：生成与剧情紧密相关的道具图片。

4. **提交作业** ：作业内容应包含 **剧本的梗概、角色设计图（四视图）、核心场景图、道具图** 。注意，仅提交这些内容，切勿添加其他无关信息。
</fragment>
