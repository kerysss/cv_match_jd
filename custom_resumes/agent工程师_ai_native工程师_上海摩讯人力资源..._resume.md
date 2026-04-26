# 定制化简历：Agent工程师 / AI Native工程师

## 申请职位

- **职位名称**：Agent工程师 / AI Native工程师
- **公司名称**：上海摩讯人力资源...
- **薪资范围**：60-90K·15薪
- **职位概述**：专注于智能体系统（Agent）的设计、开发与优化，以及AI Native应用的端到端落地，包括大模型推理、工具调用、多智能体协作、RAG、Prompt工程等方向。

---

## 个人概况

持续学习、突破个人边界，对技术保持热情。四年广告大数据开发经验，一年广告后台开发经验，自学一年转入大模型领域。具备从数据工程到模型训练、Agent应用开发的完整链路能力，擅长将大模型能力与工程系统结合，构建可落地的智能体解决方案。

---

## 技术技能（针对Agent / AI Native方向优化）

- **大模型与Agent框架**：LangChain, LlamaIndex, AutoGPT, CrewAI, Transformers, TRL, VLLM, DeepSpeed
- **推理与工具调用**：Function Calling, Tool-use, ReAct, Plan-and-Execute, RAG (检索增强生成)
- **编程语言**：Python, Scala, C++
- **深度学习框架**：PyTorch, Hugging Face Ecosystem (Datasets, Tokenizer, PEFT)
- **强化学习与对齐**：PPO, DPO, GRPO, RLHF
- **数据工程与实时处理**：Spark, Flink, ClickHouse, HBase, Iceberg, Kafka
- **后端开发**：Django, RESTful API, 微服务架构

---

## 项目实践（突出Agent与AI Native相关项目）

### 1. AI简历生成系统（Agent方向）
- 抓取Boss直聘上1000+大模型相关职位，构建职位-简历匹配打分系统（基于LLM语义相似度 + 规则引擎）
- 设计Agent工作流：自动分析职位要求 → 提取用户技能 → 调用LLM生成定制化简历内容 → 格式化输出
- 实现工具调用：爬虫、解析器、LLM生成器、PDF渲染器协同工作
- 技术栈：LangChain, Qwen-2-7B, FAISS, FastAPI, Docker

### 2. AI英语对话系统（对话Agent方向）
- 构建咖啡厅、机场、酒店等多种英语教学场景的多轮对话Agent
- 定制化Prompt模板 + 上下文记忆管理（滑动窗口 + 关键信息摘要）
- 集成deepseek API作为对话引擎，支持角色扮演、语法纠错、场景反馈
- 设计状态机控制对话流程，实现场景切换和知识点追踪

### 3. 小说续写模型（LLM训练与推理）
- 使用《白鹿原》小说数据，基于Qwen-2-7B模型，采用LoRA + DeepSpeed ZeRO-3进行高效微调
- 设计指令-续写对数据集，训练模型具备风格保持和情节连贯能力
- 部署VLLM推理服务，支持流式生成和采样参数控制

### 4. 狗狗皮肤病检测模型（传统ML + 部署）
- 收集六种皮肤病图片数据，使用XGBoost模型进行分类训练
- 特征工程：基于CNN提取图像特征后输入XGBoost，实现混合模型
- 封装为REST API，支持图片上传和实时预测（传统ML与AI Native结合）

---

## 工作经历（突出与Agent / AI Native相关的系统设计、数据链路、实时处理能力）

### 广告后台开发项目（阅文集团）
- **广告播放系统后台开发**：负责流量接入、效果监测、日志采集，设计高并发实时数据处理链路，支撑每天亿级请求
- **用户画像数据后台开发**：构建微信ID、QQID、IMEI、IFA等多设备ID归因分析系统，实现跨设备用户识别与覆盖率提升
- **内部运营系统开发**：基于Django开发运营后台，使用Spark + ClickHouse进行大规模数据分析与报表生成

### 广告数据开发项目（阅文集团）
- **广告效果模型数据流开发**：离线与实时特征工程，模型上线通路建设，支撑CTR/CVR模型迭代
- **广告效果数仓开发**：全链路数据架构设计，数仓分层（ODS/DWD/DWS/ADS），基于Iceberg的数据湖建设与优化
- **广告仿真链路开发**：AMS广告系统仿真链路实时通路开发与优化，支持模型效果A/B测试与监测
- **流量广告效果归因实时数据开发**：基于Flink实现点击归因、转化归因的实时处理，延迟控制在秒级

---

## 转型经历（从大数据→大模型→Agent的完整路径）

| 时间区间 | 学习内容 |
|---------|---------|
| 25.05～25.09 | 吴恩达机器学习课程；线性代数（3Blue1Brown）、微积分、概率统计（可汗学院） |
| 25.09～25.12 | fast.ai深度学习课程；fast.ai Stable Diffusion课程 |
| 26.01～26.03 | Hugging Face LLM课程；Deep RL课程 |
| 26.03～26.04 | happy-llm知识整合；Agent、RAG、Function Calling实战 |

---

## 基础知识（强化Agent方向的关键理论）

- **多模态**：CLIP, ViT, DiT
- **大语言模型**：Transformer原理, SFT, LoRA, RAG, Agent架构（ReAct, Plan-and-Execute, Multi-Agent）
- **强化学习与对齐**：PPO, DPO, GRPO, RLHF, 奖励模型
- **扩散模型**：VAE, DDPM, UNet（Stable Diffusion基础）
- **机器学习基础**：RNN, CNN, 随机森林/决策树, SVM, 协同过滤, 逻辑回归

---

## 职位匹配分析

### 匹配度评分：85/100

### 适配理由

| 职位要求（推断） | 匹配点 | 评分 |
|----------------|--------|------|
| Agent系统设计与开发 | ✅ AI简历生成系统（Agent工作流）、AI英语对话系统（对话Agent） | 强 |
| 大模型推理与优化 | ✅ 小说续写模型（LoRA+DeepSpeed）、VLLM部署经验 | 强 |
| 工具调用与Function Calling | ✅ 简历生成系统中爬虫/解析器/LLM工具链集成 | 强 |
| RAG（检索增强生成） | ✅ 职位匹配打分系统（语义检索+LLM生成） | 中 |
| 数据工程与实时处理 | ✅ 多年Flink/Spark/ClickHouse经验，支撑Agent所需数据链路 | 强 |
| 工程化落地能力 | ✅ 后台开发、API设计、Django、Docker | 强 |
| 强化学习与对齐 | ✅ 学习过PPO/DPO/GRPO，理论基础扎实 | 中 |
| 多模态理解 | ✅ CLIP/ViT/Diffusion基础，可扩展 | 中 |

### 总结
候选人具备从大数据工程转型到大模型及Agent方向的完整经历，在**Agent工作流设计、LLM微调与部署、实时数据处理**方面有扎实项目经验，能够快速上手AI Native系统的全栈开发。同时，持续的自学能力和跨领域知识储备（强化学习、多模态）为后续深入Agent研究提供了良好基础。