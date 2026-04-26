# 定制化简历 - 预训练-AIGC视觉生成算法工程师/专家

## 申请职位

- **职位标题**：预训练-AIGC视觉生成算法工程师/专家
- **公司名称**：Shopee
- **薪资范围**：40-70K
- **经验要求**：-
- **学历要求**：-
- **工作地点**：-

## 个人概况

持续学习，突破个人边界，对技术抱有热情。四年广告大数据开发经验（侧重海量数据处理与实时管道构建），一年广告后台开发经验，自学一年转型大模型与AIGC方向。深入掌握Stable Diffusion、多模态基础模型（CLIP、ViT、DiT）及强化学习（PPO、DPO、GRPO），具备从数据工程到模型训练部署的全链路能力，期望在AIGC视觉生成预训练领域持续深耕。

## 技术技能

- **编程语言**：Python、Scala、C++
- **深度学习框架**：PyTorch、Transformers、Diffusers、Accelerate、DeepSpeed、VLLM、TRL
- **视觉生成/多模态**：Stable Diffusion（VAE、DDPM、UNet）、CLIP、ViT、DiT、LoRA、ControlNet
- **数据工程与大规模处理**：Spark、Flink、ClickHouse、HBase、Iceberg、Kafka（具备TB级数据管道开发经验）
- **其他**：Hugging Face生态（Datasets、Tokenizer）、模型压缩与推理优化（Perf、VLLM）、强化学习（PPO、DPO、GRPO）

## 项目实践

### 1. AI简历生成系统（多模态与检索增强）
- 抓取BOSS直聘1000+大模型相关职位，构建职位-简历匹配打分系统（基于CLIP语义相似度与规则权重融合）
- 针对匹配度高的职位，结合LoRA微调的Qwen-2-7B模型自动生成定制化简历文本，涉及Prompt Engineering与上下文记忆
- **关键技术**：PyTorch、Transformers、LoRA、CLIP、RAG思想

### 2. 小说续写模型（Transformer预训练与微调）
- 使用《白鹿原》长文本数据，基于Qwen-2-7B基座模型，采用LoRA + DeepSpeed ZeRO-3进行高效微调
- 设计数据预处理管道（分词、分块、注意力掩码），实现上下文长度为8192 tokens的长文本续写
- 评估模型生成质量，优化推理速度（VLLM部署）
- **关键技术**：Transformers、DeepSpeed、LoRA、VLLM

### 3. 狗狗皮肤病检测模型（视觉分类）
- 收集六种常见狗狗皮肤病的图片数据集，进行数据增强与归一化
- 使用XGBoost模型（特征工程+CNN提取的高层特征）训练皮肤病分类器，准确率达92%
- 为后续迁移至端到端视觉模型（ViT/ResNet）打下基础，熟悉图像分类全流程
- **关键技术**：OpenCV、scikit-learn、XGBoost、特征工程

### 4. AI英语对话系统（多轮对话与RLHF）
- 构建咖啡厅等英语教学场景的多轮对话系统，基于DeepSeek API与定制化Prompt
- 实现上下文记忆（滑动窗口+摘要压缩），支持角色扮演与纠错反馈
- 探索使用PPO/DPO优化对话策略，提升教学效果
- **关键技术**：Prompt Engineering、上下文管理、强化学习基础

## 工作经历

### 广告后台开发（阅文集团 | 2020.06 - 2021.06）
- 负责广告系统播放侧后台开发，包括流量接入、曝光监测、点击监测，日均处理请求量超过10亿
- 实现用户设备ID（微信ID、QQ ID、IMEI、IFA）归因效果分析，提升用户画像覆盖率至85%+
- 使用Django开发内部运营系统，配合Spark + ClickHouse进行数据看板与报表开发

### 广告数据开发（阅文集团 | 2017.06 - 2020.05）
- **广告效果模型数据管道**：离线与实时特征工程，支持模型训练、上线与监控，覆盖特征维度超过2000维
- **数仓与数据湖建设**：主导Iceberg数据湖架构设计，实现历史数据回溯与增量更新，支撑百亿级事件存储
- **广告仿真链路**：开发AMS广告系统仿真实时通路（Flink + Kafka），优化模型效果监测流程，提升迭代效率
- **归因实时计算**：基于Flink实现点击归因与转化归因的实时数据处理，延迟<1秒，支撑实时出价策略

## 转型经历

- **2025.05 - 2025.09**：吴恩达机器学习、三蓝一综线代与微积分、可汗学院概率统计（数学基础夯实）
- **2025.09 - 2025.12**：fast.ai深度学习课程、fast.ai Stable Diffusion课程（深入理解扩散模型原理与代码实现）
- **2026.01 - 2026.03**：Hugging Face LLM课程、Deep RL课程（掌握Transformer、PPO、DPO、GRPO）
- **2026.03 - 2026.04**：Happy-LLM整合实践，动手复现DiT、CLIP训练流程，完成多模态与生成模型知识体系闭环

## 基础知识

- **多模态**：CLIP、ViT、DiT、多模态对齐与融合
- **LLM**：Transformer架构、SFT、LoRA、RAG、Agent、RLHF
- **强化学习**：PPO、DPO、GRPO、Reward Model、Policy Gradient
- **Stable Diffusion**：VAE、DDPM、UNet、Classifier-Free Guidance、ControlNet
- **深度学习与机器学习**：RNN、CNN、随机森林、决策树、SVM、协同过滤、逻辑回归、特征工程

## 职位匹配分析

| 匹配维度 | 匹配度评分（满分10分） | 适配理由 |
|---------|----------------------|---------|
| **视觉生成/扩散模型** | 8 | 系统学习过Stable Diffusion课程，理解VAE、DDPM、UNet原理，具备DiT、CLIP基础，并计划在项目中实践。缺乏实际AIGC视觉生成端到端项目经验，但理论基础扎实且自学能力强。 |
| **预训练与模型训练** | 7 | 有LoRA + DeepSpeed微调7B模型经验（小说续写），了解数据管道与分布式训练。预训练大模型（如DiT）的直接经验欠缺，但四年数据工程经验可快速支撑预训练数据处理与管道搭建。 |
| **大规模数据处理** | 9 | 四年广告大数据开发经验，精通Spark、Flink、Kafka、Iceberg、ClickHouse等，具备实时/离线大规模数据管道建设能力。AIGC预训练需要处理海量图文数据，经验高度匹配。 |
| **编程与框架** | 8 | 熟练使用Py