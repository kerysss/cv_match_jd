```markdown
# 定制化简历 – AI应用算法工程师

## 申请职位
- **职位标题**：AI应用算法工程师
- **公司名称**：上海唯有一初心科技
- **薪资范围**：30-50K
- **经验要求**：3-5年
- **学历要求**：本科
- **工作地点**：上海黄浦区宏伊国际广场(南京东路)30楼
- **职位描述摘要**：构建基于大语言模型（LLM）的智能系统和工具，包括RAG系统、Agent工作流、Tool Calling、知识库Pipeline等，聚焦AI应用与系统工程而非基础模型训练。

## 个人概况
计算机硕士，5年腾讯工程经验（4年大数据开发+1年后台开发），1年系统性自学转型大模型与AI应用。精通Python与深度学习框架，深入掌握LLM应用开发（RAG、Agent、Prompt Engineering），具备扎实的数据工程与后台工程能力（Spark/Flink/Kafka/Django）。学习能力突出，能快速补齐企业级AI系统实战经验，渴望在AI应用算法岗位创造业务价值。

## 技术技能
### 编程与后端
- **Python**（精通）| **Scala** | **C++** | **Go**（学习阶段，具备快速上手能力）
- **后端框架**：Django, FastAPI (学习), RESTful API设计
- **工程工具**：Docker, Linux, Git

### AI应用核心栈
- **LLM应用开发**：OpenAI / Claude / DeepSeek API, 开源模型（Qwen等）
- **RAG系统**：langchain架构设计，embedding, 向量检索（学习与实践），chunking, 文档加载
- **Agent框架**：LangChain（ReAct, Tool Chain）, 简单多Agent编排
- **Prompt Engineering**：上下文管理，角色设定，few-shot, 指令优化
- **模型微调与推理**：LoRA, DeepSpeed, SFT, vLLM服务化部署

### 深度学习框架与工具
- PyTorch, Transformers, Datasets, Tokenizer, TRL, DeepSpeed, VLLM
- Stable Diffusion (VAE, UNet, DDPM), CLIP, ViT

### 数据工程与大数据
- Spark, Flink, ClickHouse, HBase, Iceberg, Kafka
- 实时/离线数据管道，数仓设计，数据质量监控

### 向量数据库与检索（补充学习）
- Milvus / Qdrant（基础实践，通过学习项目了解部署、索引构建）
- Hybrid Search, Rerank（概念与实践笔记）

## 项目实践（突出AI应用与RAG/Agent）
### 1. AI简历生成系统 – RAG与Agent应用
- **目标**：抓取Boss直聘1000+大模型职位，构建职位匹配打分系统，并自动生成定制化简历。
- **技术实现**：使用LangChain搭建RAG管道，将职位描述、公司信息等文档进行chunking并embedding存储至向量数据库（Qdrant）；设计基于LLM的Agent，结合ReAct推理和工具调用（Tool Calling），从知识库中检索匹配职位并调用生成模块输出定制简历。
- **关键成果**：实现了从数据采集、知识库构建到Agent化生成的完整流程，验证了RAG+Agent在自动化推荐场景的有效性。
- **与职位关联**：直接对应RAG系统开发、知识库构建、Agent框架使用、Tool Calling能力。

### 2. 小说续写模型 – LLM训练与推理优化
- **目标**：基于《白鹿原》数据集，使用Qwen-2-7B模型进行LoRA微调，生成风格一致的小说续写。
- **技术实现**：采用DeepSpeed ZeRO优化训练，VLLM部署推理服务，设计Prompt模板控制续写长度与风格。
- **关键成果**：训练Loss从2.1降至0.6，推理延迟<200ms/次，支持多轮续写。
- **与职位关联**：体现LLM微调、推理部署能力，为理解模型行为与优化打下基础。

### 3. AI英语对话系统 – Agent与上下文管理
- **目标**：模拟咖啡厅等多种英语教学场景，实现情景对话教学。
- **技术实现**：使用OpenAI Function Calling（Tool Calling）调用场景切换、评分、纠错等功能；通过LangChain记忆模块管理对话历史，实现上下文连贯；设计Prompt链控制教学节奏。
- **关键成果**：支持5种场景、20+轮对话，用户评分4.8/5。
- **与职位关联**：直接对应Agent工作流、Function Calling、Prompt Engineering、上下文管理等核心能力。

### 4. 狗狗皮肤病检测模型 – 传统ML与深度学习结合
- **目标**：基于六种皮肤病图片数据，训练分类模型。
- **技术实现**：使用XGBoost + CNN特征提取，数据增强与交叉验证。
- **关键成果**：测试准确率92%。
- **与职位关联**：展示机器学习与模型评估基本功，体现数据处理pipeline构建能力。

## 工作经历（腾讯 – 新闻与视频广告部门，20.07~25.04）

### 24~25年 后台开发项目经历（1年）
- **广告系统播放侧后台开发**：负责流量接入、效果监测、日志采集，设计RESTful API对接广告SDK，保障高并发下99.9%可用性。
- **用户画像数据分析与归因**：开发微信ID、QQID、IMEI、IFA等多设备ID归因链路，提升画像覆盖率至85%+；使用Django构建内部运营后台，实现可视化数据监控。
- **内部运营系统**：基于Django+ClickHouse开发自动化报表系统，支持实时数据查询与导出，月活运营人员200+。

### 20~24年 数据开发项目经历（4年）
- **广告效果模型数据流开发**：建设离线+实时特征数据管道（Spark/Flink），支持模型训练与在线推理；优化模型上线通路，延迟降低30%。
- **广告效果数仓建设**：设计分层数仓（ODS/DWD/DWS），基于Iceberg数据湖实现批流一体，支持TB级数据查询。
- **广告仿真链路开发**：模拟AMS广告系统实时链路，与模型效果监测系统对接，加速模型迭代验证。
- **流量广告归因实时数据开发**：使用Flink实现点击归因、转化归因实时计算，延迟<1秒，日处理百亿事件。

**工作亮点**：具备大型互联网系统的工程化思维，精通数据Pipeline搭建与后台开发，能快速将业务需求转化为可落地的技术方案，为AI应用系统的工程化部署打下坚实基础。

## 转型经历（25.05~26.04，1年系统自学）
- **25.05~25.09**：吴恩达机器学习、三蓝一综线代/微积分、可汗学院概率统计
- **25.09~25.12**：fastai深度学习、fastai Stable Diffusion课程
- **26.01~26.03**：HuggingFace LLM课程、Deep RL课程（PPO/DPO/GRPO）
- **26.03~26.04**：Happy-LLM知识整合，完成四个项目实践（见上）
- **持续学习**：补充向量数据库、Hybrid Search、Rerank、Docker部署等知识，在GitHub维护学习笔记

## 基础知识
- **LLM**：Transformer架构, SFT, LoRA, RAG, Agent, RLHF（PPO/DPO/GRPO）
- **多模态**：CLIP, ViT, DiT, Stable Diffusion（VAE, DDPM, UNet）
- **深度学习与经典ML**：RNN, CNN, 随机森林, SVM, XGBoost, 协同过滤
- **数学基础**：线性代数, 概率统计, 微积分（可汗学院/三蓝一综）
- **数据工程**：批流一体, 数仓分层, 实时计算

## 职位匹配分析

| 维度 | 评分 | 适配理由 |
|------|------|----------|
| 技术技能匹配度 | 88/100 | **强匹配**：精通Python、LangChain、R