# 大模型训练数据系统工程师 - 定制化简历

## 申请职位

**职位标题**：大模型训练数据系统工程师  
**公司名称**：MiniMax  
**薪资范围**：30-60K  
**工作地点**：上海徐汇区新研大厦B座

---

## 个人概况

持续学习者，五年腾讯广告数据与后台开发经验，一年全职大模型转型经历。具备深厚的**数据工程基础**（Spark、Flink、Kafka、ClickHouse等大规模数据管道建设）与**模型后训练实战能力**（SFT、LoRA、RLHF、Agent设计）。能够将传统工业级数据系统经验高效迁移至LLM训练数据构造与增强场景，擅长构建从数据采集、清洗、生成到模型微调、评测的全链路系统。目标成为兼具数据系统能力与模型理解力的复合型大模型工程师。

---

## 技术技能

### 编程语言
- **精通**：Python
- **熟练**：C++
- **了解**：SQL、Shell

### 深度学习与模型训练框架
- **框架**：PyTorch、Transformers、Datasets、Tokenizer、TRL、PEFT、DeepSpeed、VLLM
- **模型后训练**：SFT（Supervised Fine-Tuning）、LoRA / QLoRA、RLHF（PPO、DPO、GRPO）
- **Agent**：LangChain、ReAct 模式、工具调用、上下文记忆管理
- **多模态**：CLIP、ViT、DIT、Stable Diffusion（VAE、DDPM、UNet）

### 数据工程与系统
- **大数据处理**：Spark（批处理）、Flink（实时流处理）、Kafka
- **数据存储**：ClickHouse、HBase、Iceberg（数据湖）
- **数据管道**：ETL/ELT 设计、特征工程、数据仓库建设、数仓分层设计
- **系统开发**：Django（后台）、RESTful API 设计

### 工具与平台
- **容器化**：Docker（个人项目实践）
- **版本控制**：Git
- **其他**：Linux、Shell 脚本

---

## 项目实践

### 1. AI简历生成系统（数据管道 + Agent设计）
- 采集Boss直聘1000+大模型相关职位信息，设计**数据抓取、清洗、结构化存储**全流程数据管道（Python + 自定义爬虫），数据清洗环节使用Spark进行去重与格式统一
- 构建**职位匹配度评分系统**，基于职位描述与用户技能库计算多维度匹配分数，支持自定义权重
- 基于评分结果，自动生成定制化简历，涉及**提示词设计**与内容生成
- **容器化部署**：使用Docker封装数据采集与评分系统，实现环境一致性与快速迭代
- **技术栈**：Python、Spark、LangChain、OpenAI API、Docker

### 2. 小说续写模型（数据预处理 + 模型微调）
- 使用《白鹿原》小说数据，构建**文本数据预处理流程**：章节拆分、句子切分、清洗特殊符号、构建（instruction, input, output）指令对数据集
- 基于Qwen-2-7B模型，使用**LoRA + DeepSpeed ZeRO-3**进行SFT微调，训练出具备风格一致性的小说续写模型
- 设计了**数据配比与采样策略**，确保模型在不同场景下的续写多样性
- **技术栈**：PyTorch、Transformers、Datasets、PEFT、DeepSpeed

### 3. AI英语对话系统（Agent设计 + 数据自动化生成）
- 设计**咖啡厅、机场、酒店等12种英语教学场景**，通过定制化提示词引导模型生成高质量的对话数据
- 开发**上下文记忆模块**（基于向量数据库），实现多轮对话的连贯性，模拟真实人机交互
- 基于DeepSeek模型，构建**AI-Agent**实现自动对话