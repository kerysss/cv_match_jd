# 申请大模型算法工程师（NLP/多模态/Agent）

**目标公司**：拼多多集团-PDD  
**职位**：大模型算法工程师（NLP/多模态/Agent）  
**薪资**：40-70K·16薪  
**地点**：上海长宁区金虹桥国际中心商场四期

---

## 个人概况

华中科技大学计算机硕士，5年腾讯广告数据与后台开发经验，1年系统性自学完成大模型领域转型。掌握大模型后训练（SFT、RLHF/PPO/DPO/GRPO）、多模态理解（CLIP、ViT）、生成模型（Stable Diffusion）、推理部署（vLLM、量化）及RAG/Agent技术。具备扎实的数据工程基础（Spark、Flink、ClickHouse），对模型训练数据管道、特征工程及系统部署有直接支撑能力。具备极强的学习自驱力和技术落地能力，致力于在大模型算法领域持续深耕。

---

## 技术技能

### 大模型训练与调优
- **后训练技术**：SFT、RLHF（PPO/DPO/GRPO）、LoRA/QLoRA、PEFT
- **分布式训练**：DeepSpeed、FlashAttention、ZeRO优化
- **推理部署**：vLLM、量化（GPTQ/AWQ）、ONNX Runtime
- **框架生态**：PyTorch、Transformers、Datasets、Tokenizer、TRL、Pef

### 多模态与生成模型
- **多模态理解**：CLIP、ViT、图文对齐、多模态融合
- **生成模型**：Stable Diffusion（VAE、DDPM、UNet）、DiT、ControlNet

### NLP与Agent
- **大模型应用**：RAG（LangChain、知识检索）、ReAct Agent、提示词工程、上下文记忆
- **模型微调**：Qwen、DeepSeek系列模型的SFT与RLHF调优

### 数据工程与后端开发
- **数据处理**：Spark、Flink、ClickHouse、HBase、Iceberg、Kafka
- **后端开发**：Django、Python/C++/Scala、广告系统模型上线通路

---

## 项目实践

**1. AI简历生成系统（RAG + Agent + 职位匹配）**  
- 爬取BOSS直聘1000+大模型相关职位信息，构建职位画像数据库  
- 设计基于大模型的职位匹配打分系统，融合职位描述、技能要求、候选人画像多维特征  
- 对高匹配度职位，利用RAG技术检索候选人项目经历与技能，自动生成定制化简历内容  
- **技术栈**：LangChain、Qwen系列模型、向量检索、PyTorch、Spark数据处理

**2. 小说续写模型（SFT + LoRA + DeepSpeed）**  
- 基于《白鹿原》小说文本数据，使用Qwen-2-7B基座模型进行SFT微调  
- 采用LoRA低秩适配与DeepSpeed ZeRO-3分布式训练策略，单机多卡高效训练  
- 模型在保持原文风格基础上实现连贯续写，评估指标：困惑度（PPL）降低15%  
- **技术栈**：Qwen-2-7B、LoRA、DeepSpeed、Transformers、Datasets

**3. AI英语对话系统（Agent + 提示词工程 + 上下文记忆）**  
- 设计咖啡厅、机场等10+场景化英语教学对话Agent，支持多轮交互  
- 定制化提示词模板实现角色扮演、语法纠错、难度自适应教学  
- 实现上下文记忆模块，长对话中保持语义连贯性  
- 基于DeepSeek系列模型完成对话生成与意图识别  
- **技术栈**：LangChain、DeepSeek、提示词工程、上下文管理

**4. 狗狗皮肤病检测模型（多分类图像任务）**  
- 采集6类狗狗皮肤病图像数据，完成数据增强与标注  
- 使用XGBoost模型完成图像特征提取与分类，准确率达87%  
- **技术栈**：XGBoost、OpenCV、数据增强

---

## 工作经历

**腾讯科技（深圳）有限公司 | 新闻与视频广告部门**  
*数据开发/后台开发工程师 | 2020.07 - 2025.04*

### 后台开发项目（2024-2025）
- **广告系统播放侧后台**：负责阅文流量广告的播放侧后台开发，包括流量接入、效果监测与日志回传，支撑日均亿级请求
- **用户画像数据平台**：负责用户设备ID（微信ID、QQID、IMEI、IFA等）归因分析后台开发，提升用户画像覆盖率至90%+
- **内部运营系统**：使用Django框架开发运营后台，结合Spark、ClickHouse进行数据可视化与分析

### 数据开发项目（2020-2024）
- **广告效果模型数据管道**：负责模型训练数据的离线与实时数据流建设，包括特征工程、样本生成、模型上线通路全链路开发
- **广告效果数仓**：主导Iceberg数据湖架构设计与ETL开发，支撑每日数百GB级数据存储与查询
- **广告仿真链路**：开发AMS广告系统仿真链路，支撑模型效果离线评估与迭代优化
- **流量广告归因**：基于Flink实现点击归因、转化归因的实时数据链路，延迟低于分钟级

---

## 转型经历

- **2025.05-2025.09**：系统学习吴恩达机器学习课程、三蓝一综线代与微积分、可汗学院概率统计  
- **2025.09-2025.12**：完成fast.ai深度学习课程及Stable Diffusion专项课程  
- **2026.01-2026.03**：完成Hugging Face LLM课程及Deep Reinforcement Learning课程  
- **2026.03-2026.04**：系统整合happy-llm等知识体系，完成多模态基础理论研究  
- **2026.01-2026.04**：实践项目（AI简历系统、小说续写、英语对话、皮肤病检测），积累模型训练与调优经验

---

## 基础知识

- **多模态**：CLIP、ViT、DiT、多模态对齐与融合  
- **大语言模型**：Transformer架构、SFT、RLHF（PPO/DPO/GRPO）、RAG、Agent  
- **生成模型**：Stable Diffusion（VAE、DDPM、UNet）、ControlNet  
- **深度学习与机器学习**：RNN、CNN、Transformer；随机森林、SVM、XGBoost、逻辑回归  
- **强化学习**：PPO、DPO、GRPO、价值函数与策略梯度  

---

## 职位匹配分析

| 维度 | 匹配度 | 适配理由 |
|------|--------|----------|
| 技术技能 | 85分 | 掌握大模型后训练（SFT、RLHF/PPO/DPO/GRPO）、多模态理解（CLIP、ViT）、生成模型（Stable Diffusion）、推理部署（vLLM、DeepSpeed）；正持续积累大规模分布式训练经验 |
| 项目经验 | 80分 | AI简历系统（RAG+Agent+匹配评分）、小说续写（SFT+LoRA）、英语对话（Agent+提示词工程）与职位方向直接相关；项目规模和个人练习为主