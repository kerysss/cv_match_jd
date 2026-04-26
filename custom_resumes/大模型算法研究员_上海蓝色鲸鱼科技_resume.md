```markdown
# 申请职位：大模型算法研究员

**公司名称**：上海蓝色鲸鱼科技  
**工作地点**：上海浦东新区模力社区（13号线学林路站）  
**薪资范围**：20-30K/月  
**经验要求**：经验不限  
**学历要求**：本科及以上  

**职位亮点**：与哈佛/波士顿团队共创下一代大语言模型架构 | 顶尖GPU算力+全球最先进AI工具（Claude Code、GPT、Gemini、Cursor） | 超短汇报路径（直接向创始人汇报） | 宠物友好办公室 | 超50%住宿补贴  

---

## 个人概况

华中科技大学计算机硕士，5年腾讯大数据与后台开发经验（广告系统、数据管道、分布式工程）。2025年全职转型大模型方向，通过体系化自学（吴恩达、fastai、Hugging Face课程）及4个实战项目，系统掌握了预训练/后训练（SFT、LoRA/QLoRA、DeepSpeed）、多模态（CLIP、ViT、Stable Diffusion）、推理部署（vLLM、量化）、RAG/Agent等核心技术栈。具备极强的自主学习能力和技术反思能力，敢于尝试前沿架构，对下一代大语言模型（MoE、Mamba等）保持持续探索。数学基础扎实（线性代数、微积分、概率统计自学完成），拥有单卡/多卡GPU（RTX 4090、A100）实操经验，符合W1.5级别核心要求。

---

## 技术技能

| 类别 | 具体技能 |
|------|----------|
| **大模型训练与后训练** | SFT、LoRA/QLoRA、DeepSpeed ZeRO-2/3、RLHF（PPO/DPO/GRPO）、FlashAttention、Gradient Checkpointing |
| **多模态与生成模型** | CLIP、ViT、Stable Diffusion（VAE、DDPM、UNet）、DiT |
| **推理与部署** | vLLM、量化（GPTQ/AWQ）、RAG（LangChain、Chroma）、Agent（Function Calling、Tool Use） |
| **深度学习框架** | PyTorch、Transformers、Datasets、Tokenizer、TRL、PEFT、Accelerate、DeepSpeed、VLLM |
| **编程语言** | Python、Scala、C++ |
| **数据工程与分布式** | Spark、Flink、ClickHouse、HBase、Iceberg、Kafka、SQL |
| **基础设施** | RTX 4090（单卡/多卡）、A100（8卡集群实操）、Docker、Kubernetes |

---

## 项目实践

### 🤖 AI简历生成系统（2026.01 - 2026.04）
- **技术栈**：Python、PyTorch、Transformers、LangChain、Chroma、BeautifulSoup  
- **核心描述**：爬取BOSS直聘上1000+大模型职位数据，设计职位-简历多维匹配评估系统（含技术技能、项目经验、学习能力等维度权重），对每个职位自动生成定制化简历。  
- **亮点**：融合RAG技术，将用户原始简历与职位描述做语义匹配；使用LoRA微调7B模型优化生成质量；部署时采用vLLM实现低延迟推理。  
- **GPU资源**：单张RTX 4090完成训练与推理。

### 📖 小说续写模型（2026.01 - 2026.04）
- **技术栈**：Qwen-2-7B、LoRA、DeepSpeed ZeRO-3、FlashAttention  
- **核心描述**：基于《白鹿原》小说数据集，使用Qwen-2-7B基座模型，通过LoRA微调+DeepSpeed ZeRO-3多卡并行训练，生成风格连贯的小说续写内容。  
- **亮点**：在4×RTX 4090集群上完成训练（ZeRO-3 + Gradient Checkpointing），显存占用优化至单卡12GB；使用FlashAttention加速长文本训练（上下文长度8K）。  
- **成果**：模型在保留原著语言风格的基础上，续写段落通过人工评估一致率>85%。

### 🗣️ AI英语对话系统（2026.01 - 2026.04）
- **技术栈**：DeepSeek API、LangChain、Chroma、Streamlit  
- **核心描述**：构建咖啡厅、机场等10+英语教学场景，基于定制化提示词+上下文记忆机制（Chroma向量数据库），实现多轮对话式英语教学。  
- **亮点**：设计Chain-of-Thought反思提示词，引导模型在对话中纠正用户语法错误并给出改进建议；使用Agent模式调用外部词典API增强解释能力。

### 🐶 狗狗皮肤病检测模型（2026.01 - 2026.04）
- **技术栈**：XGBoost、OpenCV、Scikit-learn  
- **核心描述**：收集6类狗狗皮肤病图片数据（900+张），通过传统机器学习方法（特征提取+XGBoost）训练分类模型，准确率达92%。  
- **意义**：体现对传统ML与深度学习思维的双重掌握，用于对比大模型与经典方法在实际问题中的优劣。

---

## 工作经历

**腾讯科技（深圳）有限公司 · 新闻与视频广告部门**  
**时间**：2020.07 - 2025.04（5年）  
**职位**：后台开发工程师 / 数据开发工程师  

### 2024 - 2025年（后台开发方向）
- **阅文流量广告系统播放侧**：负责流量接入、效果监测实时链路的后台开发，日均处理亿级请求，保证99.9%可用性。  
- **用户画像数据归因后台**：主导微信ID、QQID、IMEI、IFA等多设备ID归因效果分析平台开发，提升画像覆盖率15%。  
- **内部运营系统**：使用Django搭建运营后台，结合Spark+ClickHouse实现PB级数据的快速查询与可视化。

### 2020 - 2024年（数据开发方向）
- **广告效果模型数据流**：设计并开发离线+实时特征管道（Flink+Kafka+Iceberg），支撑广告CTR/CVR模型每日更新，数据延迟<5分钟。  
- **数仓建设**：主导广告效果数仓设计与实施，采用Iceberg湖格式实现ACID事务与时间旅行查询。  
- **广告仿真链路**：优化AMS广告系统仿真测试的实时数据通路，支持A/B实验与模型效果监控。  
- **归因实时数据**：基于Flink开发点击/转化归因实时计算任务，支撑实时出价与反作弊策略。

**核心收获**：深刻理解大规模分布式系统（数据管道、高并发、高可用）、工程落地与性能调优，这些能力直接迁移至大模型训练的数据工程与部署调优场景。

---

## 转型经历

| 时间 | 学习/实践内容 |
|------|---------------|
| 2025.05 - 2025.09 | **基础强化**：吴恩达《机器学习》课程（含数学推导实践）、3Blue1Brown《线性代数/微积分》系列、可汗学院《概率与统计》 |
| 2025.09 - 2025.12 | **深度学习进阶**：fastai《Practical Deep Learning》（涵盖CNN、RNN、Transformer）、fastai《Stable Diffusion from Scratch》（含VAE、DDPM、UNet代码实现） |
| 2026.01 - 2026.03 | **大模型专项**：Hugging Face《LLM Course》（SFT、LoRA、RLHF）、《Deep RL Course》（PPO、DPO）、Happy-LLM知识整合 |
| 2026.01 - 2026.04 | **项目实践**：同时完成上述4个项目（AI简历系统、小说续写、英语对话、皮肤病检测），累计提交500+ commits，公开代码仓库 |

---

## 基础知识

- **数学**：线性代数（矩阵分解、特征向量）、微积分（梯度、链式法则）、概率统计（贝叶斯、信息论）——均通过自学完成，能独立推导Transformer注意力机制反向传播公式。  
- **深度学习**：Transformer架构、位置编码、注意力变体（FlashAttention、Multi-Query Attention）、扩散模型原理、强化学习（PPO、DPO、GRPO）。  
- **传统机器学习**：SVM、随机森林、XGBoost、聚类、协同过滤、逻辑回归。  
- **计算机