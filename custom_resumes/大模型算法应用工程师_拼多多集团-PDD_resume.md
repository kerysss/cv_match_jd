# 申请职位：大模型算法应用工程师

**公司**：拼多多集团-PDD  
**薪资范围**：45-75K·18薪  
**经验要求**：3-5年 | **学历要求**：硕士  
**工作地点**：上海长宁区金虹桥国际中心31楼  

---

## 个人概况

华中科技大学计算机硕士，5年腾讯广告工程经验（大数据+后台开发），1年全职转型大模型算法。熟练掌握SFT、LoRA、RLHF（PPO/DPO/GRPO）、RAG、Agent等大模型核心技术，具备从模型微调、推理部署到应用落地的全流程实战能力。在个人项目中独立完成基于Qwen-2-7B的小说续写模型（DeepSpeed ZeRO-3 + LoRA）、基于LangChain的AI英语对话系统（RAG+提示词工程）、以及AI简历生成系统（职位匹配+RAG体系）。具备扎实的工程基础（Python/C++、PyTorch、Spark、Flink、Kafka），熟悉Linux环境开发和分布式系统。强自驱力，善于将前沿技术快速转化为可交付成果。

---

## 技术技能

| 类别 | 技能明细 |
|------|----------|
| **大模型核心** | Transformer、SFT、LoRA/QLoRA、RLHF（PPO/DPO/GRPO）、RAG、Agent、Function Calling、Prompt Engineering |
| **应用框架** | LangChain（熟练）、LlamaIndex（学习实践）、Haystack（入门）、vLLM、Ollama、LmDeploy（了解） |
| **深度学习框架** | PyTorch、Transformers、Datasets、Tokenizer、TRL、DeepSpeed（ZeRO-2/3）、FlashAttention、Gradient Checkpointing |
| **推理部署** | vLLM（模型服务）、模型量化（AWQ/GPTQ）、Ollama本地部署、Llama.cpp（了解） |
| **编程语言** | Python（精通）、C++（熟练）、Scala（熟练）、SQL（精通） |
| **大数据工程** | Spark、Flink、ClickHouse、HBase、Iceberg、Kafka、Django |
| **分布式计算** | DeepSpeed ZeRO、Spark分布式、Flink流式；了解MPI/Horovod原理 |
| **多模态** | CLIP、ViT、DiT、Stable Diffusion（VAE、DDPM、UNet） |
| **其他** | Linux环境开发、Git、Docker、Nginx |

---

## 项目实践

### 1. AI简历生成系统（大模型应用落地）  
**时间**：2026.01 - 2026.04  
**技术栈**：Python、LangChain、vLLM、Qwen-2-7B、RAG、Function Calling  
- 抓取Boss直聘上1000+大模型相关职位，构建职位知识库（向量数据库+Elasticsearch）  
- 设计职位匹配打分系统，基于提示词工程+向量相似度+规则权重，对候选人简历与JD进行多维度匹配  
- 对匹配度高的职位，调用大模型进行定制化简历生成：通过Function Calling获取用户技能清单，结合职位要求动态生成项目描述  
- 使用vLLM部署Qwen-2-7B模型，推理延迟<500ms，支持并发请求  
- **亮点**：完整实践了大模型应用的全链路（数据采集→向量检索→Prompt Engineering→Function Calling→模型服务），与拼多多职位描述中的RAG、函数调用、提示词工程高度吻合

### 2. 小说续写模型（模型微调+分布式训练）  
**时间**：2026.01 - 2026.02  
**技术栈**：PyTorch、Transformers、DeepSpeed ZeRO-3、LoRA、Qwen-2-7B  
- 基于《白鹿原》小说数据（约50万字），构造续写数据集（前文-后文对）  
- 使用Qwen-2-7B作为基座模型，采用LoRA+DeepSpeed ZeRO-3在单机8卡A100上进行参数高效微调  
- 训练过程中应用FlashAttention、Gradient Checkpointing优化显存，训练速度提升40%  
- 评估指标：Perplexity从原始模型6.8降至2.1，生成文本风格一致性通过人工评测达87%  
- **亮点**：展示了大模型微调和分布式训练的全流程能力，与职位要求的“模型微调+DeepSpeed”完全匹配

### 3. AI英语对话系统（RAG+提示词工程+上下文记忆）  
**时间**：2026.02 - 2026.03  
**技术栈**：LangChain、DeepSeek、ChromaDB、Prompt Templates  
- 构建咖啡厅、机场、酒店等10种英语教学场景知识库（ChromaDB向量数据库）  
- 定制化提示词模板，包含角色设定、场景约束、互动规则，实现情境化口语教学  
- 引入上下文记忆模块（ConversationBufferMemory），支持多轮对话连贯性  
- 集成DeepSeek API作为底座模型，通过RAG检索场景相关知识，回答准确率提升35%  
- **亮点**：完整实现了提示词工程+向量检索+上下文管理的RAG系统，与职位核心技术高度一致

### 4. 狗狗皮肤病检测模型（传统ML+模型部署）  
**时间**：2026.03 - 2026.04  
**技术栈**：Python、XGBoost、Flask、Docker  
- 收集6种狗狗皮肤病图片数据，提取颜色直方图、纹理特征等，使用XGBoost训练分类模型  
- 模型准确率92%，使用Flask封装为RESTful API，Docker容器化部署  
- **亮点**：展示了端到端的模型训练到部署能力，体现工程基础

---

## 工作经历

### 腾讯科技（深圳）有限公司 · 新闻与视频广告部门  
**时间**：2020.07 - 2025.04（4年10个月）

#### 后台开发工程师（2024 - 2025）  
- **流量广告系统播放侧后台开发**：负责阅文流量接入、广告请求分发、效果监测，日均处理请求量超10亿，系统可用性99.99%  
- **用户画像数据分析与覆盖率提升**：整合微信ID、QQID、IMEI、IFA等多设备ID，构建统一用户画像归因体系，覆盖率从65%提升至92%  
- **内部运营系统开发**：基于Django+ClickHouse，开发广告效果看板、投放分析工具，服务运营团队日常决策  
- **工程能力体现**：Linux环境后端开发、高并发系统设计、分布式组件（Kafka、Redis）应用、团队协作与需求评审

#### 大数据开发工程师（2020 - 2024）  
- **广告效果模型数据流开发**：负责特征数据离线/实时生产以及模型上线通路建设，支持CTR/CVR模型每日更新  
- **广告效果数仓建设**：设计分层数据仓库（ODS→DWD→DWS→ADS），基于Iceberg数据湖实现增量更新，数据产出时效性从T+1提升至小时级  
- **广告仿真链路开发**：搭建AMS广告系统仿真环境实时通路，支持模型效果回测与对比实验，提升迭代效率  
- **归因实时数据开发**：基于Flink实现点击归因、转化归因的实时流处理，延迟<1秒，支撑实时竞价系统  
- **技术栈**：Spark、Flink、ClickHouse、HBase、Iceberg、Kafka，具备扎实的