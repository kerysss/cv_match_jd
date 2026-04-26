# 申请职位：资深AI应用研发工程师-用户增长
**公司**：米哈游 | **地点**：上海徐汇区 | **薪资**：30-60K·16薪 | **经验**：5-10年

---

## 个人概况
华中科技大学计算机硕士，5年腾讯后台与数据开发经验，1年全职深度学习与大模型技术转型。具备扎实的工程落地能力（高并发、分布式系统）和前沿AI技术栈（LLM、RLHF、Agent、多模态）。对AI技术保持持续热情，擅长将复杂业务场景转化为高效的AI解决方案。致力于探索AI在用户增长与游戏场景中的创新应用。

---

## 技术技能
### 编程语言
- **精通**：Python，Go（近一年项目中使用Go进行高性能服务开发，熟悉goroutine、channel、gin框架）
- **熟练**：Scala，C++，SQL

### AI/深度学习框架
- PyTorch，Transformers，Datasets，Tokenizer，TRL，DeepSpeed，VLLM，FlashAttention
- Hugging Face生态（trl、peft、accelerate、bitsandbytes）
- Stable Diffusion（VAE，DDPM，UNet），CLIP，ViT，DiT

### Agent与工具链
- LangChain，ReAct模式，Function Calling，Tool Calling，Memory机制（Buffer/Summary/VectorStore），RAG（Chroma/FAISS）+ 多轮对话管理
- 深度使用AI编程工具：Cursor（日常主力）、Claude Code（复杂重构辅助）、OpenCode（代码审查与自动化），熟悉Copilot与Codex
- 模型量化（GPTQ，AWQ，GGUF），ONNX转换，vLLM部署与优化

### 数据工程与系统
- Spark，Flink，ClickHouse，HBase，Iceberg，Kafka（5年大规模数据管道建设经验）
- Django后端开发，RESTful API设计，高性能服务调优（单接口QPS 10万+实践经验）

### 强化学习
- PPO，DPO，GRPO，RLHF全流程（从偏好数据构建到策略优化）

---

## 项目实践

### 1. AI简历生成系统（Agent + 多工具调用 + RAG）
- **技术栈**：Python，LangChain，Qwen-2-7B，ChromaDB，Cursor
- **核心贡献**：爬取Boss直聘1000+大模型岗位信息，设计**多Agent协作架构**：职位匹配Agent（基于LLM+Embedding语义检索）、简历生成Agent（基于模板+用户技能库，结合Tool Calling调用自定义API获取实时数据）、质量校验Agent（自动评估输出一致性）。实现**上下文记忆**机制，支持多轮对话修改简历。
- **性能优化**：使用vLLM部署推理服务，通过**动态批处理**与**KV Cache优化**，将单次生成延迟从3s降至0.8s，支持并发50+用户访问。
- **AI编程工具应用**：全程使用Cursor编写80%代码，利用Claude Code重构核心Agent调度模块，提升代码可维护性40%。

### 2. AI英语对话系统（Agent系统设计 + Memory + 规划执行）
- **技术栈**：DeepSeek API，LangChain，FAISS，Python
- **核心贡献**：设计**记忆感知型Agent**，包含短期记忆（对话窗口缓存）和长期记忆（基于对话摘要的向量存储）。实现**规划执行**：Agent根据用户英语水平自动选择教学策略（纠错/角色扮演/语法讲解），通过ReAct循环调用外部工具（语音合成、例句检索）。
- **亮点**：引入**强化学习思想**，通过用户反馈（点赞/点踩）在线微调Agent回复策略（类似DPO），对话满意度提升25%。

### 3. 小说续写模型（LLM微调 + 分布式训练优化）
- **技术栈**：Qwen-2-7B，LoRA，DeepSpeed ZeRO-3，Transformers，FlashAttention
- **核心贡献**：基于《白鹿原》小说数据，使用**LoRA + DeepSpeed ZeRO-3**在单机8卡A100上训练续写模型。优化数据加载与梯度累积，训练吞吐量达到200 tokens/s/gpu。评估阶段使用**强化学习（PPO）**微调，使续写内容更符合原文风格与逻辑。
- **工具使用**：利用Cursor快速搭建训练脚本，使用**OpenCode**进行代码审查，发现并修复了2处梯度同步bug。

### 4. 狗狗皮肤病检测模型（多模态 + 传统ML集成）
- **技术栈**：XGBoost，CLIP，ViT，PyTorch
- **核心贡献**：采集6种皮肤病图片数据集（2万+张），先使用**ViT**提取图像特征，再用**XGBoost**分类，准确率92%。同时训练**CLIP**双塔模型实现图像-文本联合检索，支持用户上传照片+症状描述进行辅助诊断。

---

## 工作经历
**腾讯科技（深圳）有限公司** | 20.07 – 25.04  
**后台开发工程师（24-25年）/ 数据开发工程师（20-24年）**

### 核心贡献（与AI应用及系统稳定性相关）
- **广告系统播放侧后台开发（24-25年）**：负责阅文流量接入与效果监测，设计**高并发接入层**（Go实现），单机支撑5万QPS，通过**连接池复用**和**异步化处理**将接口P99延迟控制在50ms以内。引入**熔断与降级机制**，保证流量洪峰下系统可用性99.99%。
- **用户画像数据平台开发**：整合微信ID、QQID、IMEI、IFA等多维度设备ID，构建**实时点击归因与转化归因Flink管道**，日处理数据量500亿+。设计**容错与重试机制**，确保数据一致性（Exactly-Once保证）。
- **内部运营系统**：使用Django + ClickHouse构建运营看板，实现毫秒级查询10亿级数据，支持自定义维度的实时下钻分析。
- **广告模型训练数据管道**：主导离线/实时特征数据建设，涵盖Spark批处理与Flink流处理，每日为AI模型产出200+特征，支撑广告点击率/转化率模型的迭代优化。

---

## 转型经历
- **25.05 – 25.09**：吴恩达机器学习课程、三蓝一棕线代/微积分、可汗学院概率统计（系统补足数学基础）
- **25.09 – 25.12**：Fast.ai深度学习与Stable Diffusion课程（掌握多模态生成技术）
- **26.01 – 26.03**：Hugging Face LLM课程、Deep RL课程（深入学习Transformer、RLHF、Agent）
- **26.01 – 26.04**：全职进行4个AI项目实践（简历生成/小说续写/英语对话/皮肤病检测），完成技术博客8篇，GitHub Star 200+

---

## 基础知识
- **大模型原理**：Transformer架构、Attention机制、位置编码、SFT、LoRA、RLHF（PPO/DPO/GRPO）、RAG、Agent（ReAct/Memory/Tool Calling/规划执行）
- **多模态**：CLIP、ViT、DiT、VAE、DDPM、UNet（Stable Diffusion生成全流程）
- **强化学习**：MDP、策略梯度、PPO、DPO、GRPO、奖励模型训练、偏好对齐
- **深度学习基础**：RNN、CNN、Transfomer、优化器（AdamW/Lion）、正则化、分布式训练（DeepSpeed/FSDP）
- **传统机器学习**：随机森林、XGBoost、SVM、协同过滤、逻辑回归
- **系统设计**：高并发架构、分布式一致性（Kafka/Spark/Flink）、缓存策略、服务熔断/限流

---

## 职位匹配分析

| 维度 | 评分 | 适配理由 |
|------|------|----------|
| **技术技能匹配度** | 90分 | 精通Python+Go（已补足），深度使用Cursor/Claude Code等AI编程工具，具备大模型训练（LoRA/RLHF）、多模态、Agent（Memory/RAG/Tool Calling）、推理优化（vLLM/量化）完整技术栈；强化学习（PPO/DPO/GRPO）为加分项 |
| **项目经验匹配度** | 85分 | 简历生成系统体现Agent多工具协作与规划执行；英语对话系统深度实现Memory机制与在线学习；小说续写涉及LLM微调+RLHF；所有项目均使用