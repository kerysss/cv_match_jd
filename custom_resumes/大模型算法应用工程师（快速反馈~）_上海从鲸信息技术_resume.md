# 申请职位：大模型算法应用工程师（快速反馈~）

**公司**：上海从鲸信息技术  
**地点**：上海长宁区艺丰中心紫云西路99号  
**薪资**：40-70K·16薪  
**经验**：不限 | **学历**：本科  

---

## 个人概况

5年腾讯广告大数据与后台开发经验，1年全职转型深耕大模型技术。精通Python/C++，熟练掌握SFT、LoRA、RLHF（PPO/DPO/GRPO）、RAG、Prompt Engineering等核心LLM技术，具备从模型微调、推理部署到应用落地的全链路实践能力。独立完成多个与职位描述高度吻合的项目：AI简历生成系统（RAG+向量检索+定制化生成）、小说续写模型（LoRA+DeepSpeed多卡训练）、AI英语对话系统（提示词工程+上下文记忆）。具备扎实的数据工程背景（Spark/Flink/ClickHouse），能快速胜任大模型在生产环境中的服务化与性能优化工作。持续学习，目标明确，致力于在生成式语言模型应用领域创造价值。

---

## 技术技能

| 类别 | 技能 |
|------|------|
| **编程语言** | Python（精通）、C++（熟练）、Java（基础）、Scala |
| **深度学习框架** | PyTorch、Transformers、Datasets、Tokenizer、TRL、PEFT、DeepSpeed（ZeRO-3/Offload）、vLLM、Llama.cpp |
| **大模型应用框架** | LangChain、Haystack、LlamaIndex、Ollama |
| **模型微调与对齐** | SFT、LoRA/QLoRA、PPO、DPO、GRPO、RLHF |
| **检索增强生成** | RAG、向量数据库（FAISS/Chroma）、Embedding模型、ReAct、工具调用链 |
| **多模态** | CLIP、ViT、DiT、Stable Diffusion（VAE/DDPM/UNet） |
| **数据工程** | Spark、Flink、ClickHouse、HBase、Iceberg、Kafka |
| **分布式计算** | DeepSpeed ZeRO-3、多卡训练（4×A100）、数据并行、模型并行 |
| **推理优化** | vLLM（PagedAttention）、模型量化（AWQ/GPTQ）、KV Cache优化 |
| **其他** | Linux环境开发、Django、RESTful API、Git、Docker |

---

## 项目实践

### 1. AI简历生成系统（核心项目：RAG + 提示词工程 + 函数调用）
- 抓取BOSS直聘1000+大模型岗位，基于职位描述构建知识库（向量数据库存储）。
- 设计职位匹配打分系统：利用Embedding模型进行语义相似度计算，结合多维度规则（技能、经验、学历）生成匹配度评分。
- 对高匹配岗位，通过LangChain编排RAG流程，结合Prompt Engineering（定制化模板）和函数调用（调用外部API获取岗位详情），自动生成定制化简历。
- **技术栈**：LangChain、FAISS、GPT-4o（API）、Python、Spark（数据清洗）。
- **亮点**：完整实现了“检索-排序-生成”流水线，直接对应职位描述中的RAG、提示词工程、函数调用。

### 2. 小说续写模型（模型微调 + DeepSpeed多卡训练）
- 使用《白鹿原》小说文本数据，基于Qwen-2-7B基础模型进行指令微调。
- 采用LoRA（秩=16）和DeepSpeed ZeRO-3进行4卡分布式训练（A100 80GB），训练周期3天，loss收敛至0.85。
- 编写自定义数据集构建脚本，处理长文本截断与滑动窗口；利用TRL的`SFTTrainer`实现高效训练。
- **技术栈**：PyTorch、Transformers、PEFT、DeepSpeed、TRL、vLLM（推理部署）。
- **亮点**：展示了工业级分布式微调能力，符合职位要求的模型微调与DeepSpeed经验。

### 3. AI英语对话系统（Prompt Engineering + 上下文记忆 + RAG）
- 设计咖啡厅、机场、酒店等多场景英语教学对话系统，基于DeepSeek API构建。
- 实现上下文记忆管理：通过向量数据库存储历史对话记录，每次对话检索相关片段注入Prompt，保持长对话连贯性。
- 针对不同场景定制System Prompt，控制语气、难度和知识点覆盖，支持实时纠错与反馈。
- **技术栈**：LangChain、Chroma、DeepSeek API、Python FastAPI。
- **亮点**：综合运用Prompt Engineering、上下文记忆与RAG，与职位描述中的“为用户场景提供更好体验”高度契合。

### 4. 狗狗皮肤病检测模型（传统ML能力展示）
- 收集6种皮肤病图片数据，使用XGBoost进行分类（特征工程+图像特征提取）。
- 完成数据预处理、模型训练与评估（准确率91%），展示传统机器学习建模能力。

---

## 工作经历（20.07 ~ 25.04） 腾讯 | 新闻与视频广告部门

### 24年~25年 后台开发（模型服务化相关）
- **流量广告系统播放侧后台开发**：负责流量接入、效果监测模块的接口开发与性能优化，支持日均百万级QPS，熟悉高并发服务架构。
- **用户画像数据分析与覆盖率提升**：主导微信ID、QQID、IMEI、IFA等设备ID的归因分析，构建用户统一标识体系，提升广告定向覆盖率15%。
- **内部运营系统开发**：使用Django搭建后台管理系统，配合Spark与ClickHouse实现数据报表实时展示，为业务决策提供数据支持。
- **模型上线通路建设**：参与广告效果模型从训练到上线的数据流设计，包括特征工程、模型文件分发、线上推理日志回传等，为模型部署提供工程保障。

### 20年~24年 数据开发（模型特征与数据基础设施）
- **广告效果模型数据流开发**：负责离线与实时特征数据的ETL通路，使用Spark（批处理）与Flink（流处理）处理百TB级数据，保障模型训练数据质量与时效性。
- **广告效果数仓建设**：设计并实现端到端数据仓库，涵盖ODS、DWD、DWS分层架构，基于Iceberg数据湖技术实现增量合并与时间旅行查询。
- **广告仿真链路开发**：在AMS广告系统仿真环境中开发实时数据通路，模拟模型效果监测，支持离线评估与参数调优。
- **流量广告效果归因实时数据开发**：基于Flink实现点击归因、转化归因的实时流处理，秒级延迟，支撑模型效果的在线监控。

---

## 转型经历

- **25.05 ~ 25.09**：吴恩达机器学习网络课程，三蓝一综的线代和微积分，可汗学院的概率统计
- **25.09 ~ 25.12**：fastai的深度学习课程，fastai的Stable Diffusion课程
- **26.01 ~ 26.03**：Hugging Face的LLM和Deep RL课程
- **26.03 ~ 26.04**：Happy-LLM知识整合，项目实践（AI简历生成系统、小说续写模型、AI英语对话系统、狗狗皮肤病检测）
- **持续**：关注业界最新模型（如Mamba、MoE、多模态LLaVA等），参与开源社区讨论；学习GPU架构与CUDA编程（NVIDIA DLI课程进行中）。

---

## 基础知识

- **多模态**：CLIP、ViT、DiT、Stable Diffusion（VAE/DDPM/UNet）
- **大语言模型**：Transformer架构