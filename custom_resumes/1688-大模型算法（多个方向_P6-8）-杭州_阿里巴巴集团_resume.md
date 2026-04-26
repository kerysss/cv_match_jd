# 申请职位：1688-大模型算法（Agent方向，P6-8）-杭州

**公司**：阿里巴巴集团  
**地点**：上海浦东新区阿里巴巴(中国)网络技术有限公司1  
**薪资范围**：40-70K·16薪  
**经验要求**：3-5年 | **学历要求**：本科  

---

## 个人概况

华中科技大学计算机硕士，5年腾讯广告数据工程与后台开发经验，1年全职转型大模型方向。具备扎实的LLM/RL/Agent理论基础，熟练掌握SFT、DPO、PPO、GRPO等alignment方法，并具备PyTorch/DeepSpeed/vLLM全链路训练推理实践。拥有Agent对话系统（定制化prompt、上下文记忆）及后训练（LoRA/DeepSpeed）项目经验，熟悉大规模数据处理与实时流计算，能够将数据工程能力高效迁移至后训练数据合成场景。持续学习、技术热情高，致力于在AI Agent产品落地中发挥算法与工程结合的价值。

---

## 技术技能

- **大模型训练与对齐**：SFT、LoRA、DPO、PPO、GRPO、RLHF；Transformers、TRL、DeepSpeed、vLLM  
- **Agent技术栈**：ReAct模式、Tool Use、Function Calling、LangChain、上下文记忆管理、Prompt Engineering  
- **多模态**：CLIP、ViT、DiT、Stable Diffusion（VAE、DDPM、UNet）  
- **深度学习框架**：PyTorch、HuggingFace（Datasets、Tokenizer、Accelerate）  
- **数据工程**：Spark、Flink、ClickHouse、HBase、Iceberg、Kafka；离线/实时数据流设计  
- **编程语言**：Python（熟练）、Scala（使用）、C++（基础）  
- **核心基础**：Transformer架构、RNN/CNN、随机森林、XGBoost、协同过滤、逻辑回归  

---

## 项目实践

### 1. AI简历生成系统（Agent数据合成方向）  
**技术栈**：GPT API、LangChain、ReAct、Spark  
- 抓取Boss直聘1000+大模型招聘职位，构建职位画像与候选人匹配模型  
- 设计多维度匹配打分Agent（技能/经验/背景），自动为每个职位生成定制化简历内容  
- 涉及Tool Use（调用职位搜索API、数据清洗函数）、Planning（多步信息抽取与重组）  
- 该项目可作为Agent数据合成Pipeline雏形：从异构源头抽取信息，通过LLM生成结构化输出  

### 2. AI英语对话系统（Agent对话形态）  
**技术栈**：DeepSeek API、LangChain、Prompt Engineering、上下文记忆  
- 构建咖啡厅、机场等10种英语教学场景，定制化对话流与角色设定  
- 实现多轮对话的上下文记忆管理（滑动窗口+摘要压缩），支持用户自由切换场景  
- 具备工具调用能力：查词典、语法纠错、场景知识检索，提升交互体验  
- 该项目的Agent对话框架可迁移至业务Agent的tool use与planning增强  

### 3. 小说续写模型（后训练实践）  
**技术栈**：Qwen-2-7B、LoRA、DeepSpeed、SFT  
- 使用《白鹿原》小说数据，进行数据清洗与分段处理，构建续写训练语料  
- 基于Qwen-2-7B模型，采用LoRA+DeepSpeed ZeRO-3进行SFT微调，训练收敛稳定  
- 产出模型在保持原作文风的基础上续写，完成率与连贯性达预期  
- 该实践验证了从数据构建到后训练的全流程能力，可直接复用于Agent后训练场景  

### 4. 狗狗皮肤病检测模型（分类任务）  
**技术栈**：XGBoost、图像特征提取  
- 收集6类皮肤病图像数据，进行数据增强与特征工程  
- 使用XGBoost训练多分类模型，准确率85%，部署为简易API服务  

---

## 工作经历

### 腾讯 新闻与视频广告部门 | 20.07 – 25.04  
**后台开发工程师（24-25年）**  
- 阅文流量广告系统播放侧后台开发：负责流量接入、效果监测模块，每日处理广告请求超亿级  
- 用户画像数据分析与覆盖率提升：主导微信ID、QQID、IMEI、IFA等多设备ID归因效果分析，优化用户匹配准确率15%  
- 内部运营系统开发：使用Django搭建后台，结合Spark/ClickHouse完成数据报表与监控  

**数据开发工程师（20-24年）**  
- **广告效果模型数据流建设**：负责特征数据离线/实时开发，为CTR/CVR模型提供训练与在线推理所需的特征管道，涉及Spark Streaming与Flink实时计算  
- **广告数仓开发**：设计并搭建整条数据通路（ODS→DWD→DWS→ADS），采用Iceberg数据湖实现高效存储与回溯  
- **广告仿真链路**：开发AMS广告系统仿真链路实时通路，支持模型效果线上监测与A/B实验分析  
- **流量广告效果归因**：基于Flink实现点击归因、转化归因的实时数据处理，延迟<1秒，支撑广告计费与优化  

**与算法团队的协作亮点**：  
- 多次参与模型效果归因分析，深入理解特征工程对模型效果的影响  
- 为算法团队提供高质量离线训练样本（数仓清洗+去偏采样），推动模型迭代  
- 熟悉大规模分布式数据处理、实时流计算，具备将数据工程能力迁移至后训练数据合成场景的坚实基础  

---

## 转型经历

| 时间 | 学习内容 | 关键成果 |
|------|----------|----------|
| 25.05 – 25.09 | 吴恩达机器学习、线性代数/概率统计基础 | 构建扎实数学与ML理论 |
| 25.09 – 25.12 | fastai深度学习、Stable Diffusion课程 | 掌握CNN、Diffusion、ViT等前沿模型 |
| 26.01 – 26.03 | HuggingFace LLM课程、Deep RL课程 | 深入理解RLHF、PPO、DPO、GRPO |
| 26.03 – 26.04 | happy-llm整合学习 | 系统梳理LLM全链路知识 |
| 26.01 – 26.04 | 项目实践（4个项目） | 产出可用模型与Agent系统，验证学习成果 |

---

## 基础知识

- **LLM**：Transformer、SFT、LoRA、RAG、Agent、Alignment（PPO/DPO/GRPO）  
- **强化学习**：Policy Gradient、PPO、DPO、GRPO、RLHF  
- **多模态**：CLIP、ViT、DiT、VAE、DDPM、UNet  
- **机器学习**：RNN、CNN、随机森林、XGBoost、SVM、协同过滤、逻辑回归  
- **数据工程**：Spark、Flink、ClickHouse、Iceberg、Kafka，流批一体架构  

---

## 职位匹配分析

### 总体评分：80分（良好）

| 维度 | 评分 | 关键匹配点 |
|------|------|------------|
| 技术技能 | 85分 | 熟悉SFT/DPO/PPO/GRPO等alignment方法；掌握Agent相关技术（ReAct、Tool Use、Function Calling）；PyTorch/DeepSpeed/vLLM全链路经验；多模态基础 |
| 项目经验 | 75分 | 小说续写（后训练）、英语对话（Agent雏形）、简历生成（数据合成思路）；项目虽非工业级但覆盖核心方向，可根据面试进一步深化 |
| 工作经历 | 70分 | 5年腾讯数据工程经验，精通大规模数据处理、实时流计算、特征工程，可高效迁移至后训练数据合成场景；有与算法团队协作经验 |
| 基础知识 | 85分 | 系统自学ML/DL/RL，理论基础扎实；对LLM/Agent概念理解清晰 |
| 转型能力 | 90分 | 华中科大计算机硕士，1年全职跨领域转型，展现出极强的自驱力与技术热情，符合职位对“技术热情”的要求 |
| 职位要求 | 85分 | 5年经验（超3-5年要求）、硕士学历（高于本科）、技术栈高度匹配；无顶会论文/开源贡献（加分项缺失） |

### 适配理由

1. **alignment方法全覆盖**：具备SFT/DP