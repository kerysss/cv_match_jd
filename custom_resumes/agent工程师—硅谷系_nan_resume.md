# 定制简历

## 申请职位

**职位**：Agent工程师—硅谷系  
**薪资范围**：30-60K  
**经验要求**：3-5年  
**学历要求**：本科  
**工作地点**：不限（支持跨时区远程协作）  

## 个人概况

5年腾讯广告系统开发经验，其中4年大数据开发（Spark/Flink/ClickHouse/Iceberg）+ 1年后台开发（广告播放侧+用户画像+运营系统）。全职一年系统转型大模型与AI工程，具备从0到1构建LLM应用的能力（RAG、Agent、SFT）。精通Python，熟悉PyTorch/Transformers/DeepSpeed等深度学习框架，拥有广告系统大规模数据处理与实时监控的工程实战经验。英语读写流利（长期阅读英文技术文档并参与海外协作），自驱力强，能快速适应跨时区远程协作。

## 技术技能

| 类别 | 技能 |
|------|------|
| **编程语言** | Python（精通，5年+）、Scala、C++、SQL |
| **Python工程** | FastAPI、Pydantic、Django、Flask、RESTful API设计 |
| **AI框架与工具** | PyTorch、Transformers、Datasets、Tokenizer、TRL、DeepSpeed、vLLM、LoRA、QLoRA、量化推理 |
| **LLM/Agent** | LangChain、ReAct循环、工具调用链、RAG（Chroma/FAISS）、Prompt Engineering、Function Calling、记忆管理 |
| **云原生/DevOps** | Docker、Docker Compose、Kubernetes（基础）、CI/CD、Linux运维、GCP基础（GCS、GKE） |
| **数据工程** | Spark、Flink、Kafka、ClickHouse、HBase、Iceberg、Airflow |
| **监控与调优** | Prometheus、Grafana、日志系统、性能Profiling、线上故障排查 |
| **AI编程工具** | Cursor、GitHub Copilot |

## 项目实践

### 1. AI Agent简历生成与匹配系统（个人项目 · 2026.01-2026.04）
- 设计并实现一个基于LLM的多Agent系统：**爬虫Agent**（抓取BOSS直聘1000+大模型岗位）、**匹配Agent**（使用嵌入模型计算岗位与简历相似度）、**生成Agent**（调用DeepSeek API，结合工具调用生成定制化简历）
- 采用**ReAct循环**：Agent根据用户意图自动选择工具（爬虫、数据库查询、LLM生成），支持多轮交互和上下文记忆
- 后端使用**FastAPI**搭建RESTful API，**Pydantic**进行数据校验与序列化，通过Docker Compose打包部署
- 项目亮点：首次将Agent编排引入简历匹配场景，实现端到端自动化，代码开源在GitHub（附链接）

### 2. 小说续写模型（个人项目 · 2026.01-2026.03）
- 基于Qwen-2-7B基座模型，使用白鹿原小说数据集进行指令微调
- 采用**LoRA + DeepSpeed ZeRO-3**进行高效训练，显存节省约60%，训练速度提升2倍
- 在vLLM上部署推理服务，支持流式输出和批量请求，响应延迟低于200ms
- 实践中解决了长文本上下文窗口溢出、过拟合等问题，体现了扎实的模型工程能力

### 3. AI英语对话系统（个人项目 · 2026.03-2026.04）
- 设计多场景英语教学对话Agent（咖啡厅、机场、商务等），内置**情景记忆模块**和**知识库RAG**
- 通过**Function Calling**调用外部API（天气查询、翻译工具等），增强对话的交互性与实用性
- 使用LangChain构建多Agent协作流程：教师Agent负责教学引导，纠错Agent负责语法检测
- 部署在GCP虚拟机上并对外暴露访问接口，使用Prometheus + Grafana监控请求量和响应时间

### 4. 狗狗皮肤病检测模型（个人项目 · 2026.03-2026.04）
- 收集6种狗狗皮肤病的图片数据集，使用XGBoost（特征工程+图像CNN特征）进行分类
- 数据处理管道使用Spark进行大规模图像特征提取，实现高吞吐训练
- 模型上线后提供RESTful API，支持图片URL输入，返回诊断结果及置信度

## 工作经历

**腾讯 — 新闻与视频广告部门**（2020.07-2025.04）  
*后台开发工程师 / 数据开发工程师*

### 1. 广告系统后台开发（2024-2025）
- 负责**阅文流量广告播放侧**后台开发：实现流量接入、广告请求分发、效果监测与日志上报，系统日处理请求量亿级，P99延迟低于50ms
- **用户画像平台**：通过Spark与ClickHouse对微信ID、QQID、设备ID等进行归因分析，提升用户覆盖率从70%到95%，支撑广告精准投放
- **内部运营系统**：使用Django + FastAPI开发后台管理界面，集成数据报表与自动化任务调度

### 2. 广告效果数据开发（2020-2024）
- **实时/离线特征工程**：构建广告效果模型的特征数据流，使用Flink处理实时点击、曝光数据，Spark处理离线批量特征，确保特征时效性（秒级延迟）
- **数仓建设**：基于Iceberg设计广告效果数仓，实现全链路数据一致性，支持TB级数据查询与自助分析
- **广告仿真链路**：搭建AMS广告系统仿真平台，模拟广告竞价与投放流程，用于模型效果评估与A/B测试
- **归因实时链路**：开发Flink + Kafka实时归因系统，实现点击归因、转化归因的秒级计算与写入，准确率99.9%

## 转型经历

| 时间 | 内容 |
|------|------|
| 2025.05-2025.09 | 系统学习机器学习基础（吴恩达课程）、线性代数/概率统计（3Blue1Brown、可汗学院） |
| 2025.09-2025.12 | 深度学习（Fast.ai）、Stable Diffusion（Fast.ai课程） |
| 2026.01-2026.03 | LLM与Deep RL（Hugging Face课程）、LangChain与Agent实战 |
| 2026.03-2026.04 | 项目实践：AI简历Agent系统、小说续写、英语对话Agent、皮肤病检测 |
| 2026.01-2026.04 | 持续学习Happy-LLM知识整合，参与开源Agent框架（CrewAI）的issue讨论与贡献 |

## 基础知识

- **多模态**：CLIP、ViT、DiT、VAE、DDPM、U-Net
- **LLM**：Transformer、SFT、LoRA、RAG、Agent、Function Calling、工具调用链路
- **强化学习**：PPO、DPO、GRPO、RLHF
- **深度学习/机器学习**：RNN、CNN、随机森林、SVM、协同过滤、逻辑回归、XGBoost
- **数学基础**：线性代数、概率统计、微积分（通过系统自学具备扎实的理论理解）

## 职位匹配分析

| 维度 | 评分 | 适配理由 |
|------|------|----------|
| 技术技能 | 90分 | 精通Python，具备5年实际项目经验；熟悉FastAPI/Pydantic/Docker；掌握LLM训练推理全栈；具备广告系统开发经验（高度匹配）；**补充说明**：近期已使用Cursor进行代码编写，并了解GCP基础（GCS/GKE） |
| 项目经验 | 80分 | 个人项目涵盖Agent架构（ReAct循环、工具调用、RAG），并进行了云端部署与监控；虽为非商业项目，但技术选型与职位描述高度一致（LangChain、vLLM、FastAPI） |
| 工作经历 | 90分 | 5年腾讯广告系统数据与后台开发，与职位“广告系统开发经验优先”完美匹配；具备大规模系统监控、线上问题定位与优化能力；DevOps经验（Docker、CI/CD、监控）通过项目展现 |
| 基础知识 | 85分 | 系统学习过大模型与强化学习理论，理解Agent底层原理（记忆管理、工具编排）；数学基础扎实