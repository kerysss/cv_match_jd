# 定制化简历

## 申请职位

**大模型算法工程师【大模型独角兽】**  
薪资范围：40-70K·15薪  
经验要求：3-5年  
学历要求：硕士  

**岗位职责**：  
1. 负责文本和多模态大模型的研发与应用，涵盖 SFT、RL、Agent/Multi-Agent、RAG 等方向，探索前沿训练与优化方法；  
2. 基于业务场景，设计模型微调方案及算法/系统解决方案，推动模型落地应用；  
3. 跟踪前沿技术动态，探索 AI 在公共服务、民生场景中的智能化与普惠化应用，推动相关领域技术创新。

---

## 个人概况

- 计算机科学与技术硕士，5年腾讯大数据工程与后台开发经验，1年系统性大模型方向转型（含系统课程学习与项目实践）  
- 深度学习/大模型技术栈：SFT、LoRA/QLoRA、PPO/DPO/GRPO、RAG、Agent、多模态（CLIP/ViT/DiT）、Stable Diffusion、Transformer  
- 工程能力：PyTorch、DeepSpeed、TRL、vLLM、Spark、Flink、ClickHouse、Django  
- 具备从数据处理、模型训练到推理部署的全链路能力，对后训练（Post-training）和模型工程化落地有浓厚兴趣  
- 持续学习、突破边界，已独立完成多个大模型项目（小说续写、AI对话、简历生成等），展现出色的问题解决与创新能力

---

## 技术技能

| 类别 | 技能 |
|------|------|
| **大模型训练与微调** | SFT（Supervised Fine-Tuning）、LoRA/QLoRA、DeepSpeed ZeRO-2/3、PPO/DPO/GRPO、TRL框架、RLHF |
| **多模态** | CLIP、ViT、DiT、Stable Diffusion（VAE/DDPM/UNet） |
| **推理与部署** | vLLM、AWQ/GPTQ量化、模型服务化（FastAPI + vLLM）、Hugging Face Transformers/Datasets/Tokenizer |
| **深度学习框架** | PyTorch、Transformers、TRL、DeepSpeed、Hugging Face 生态 |
| **数据工程与后台** | Spark、Flink、ClickHouse、HBase、Iceberg、Kafka、Django、Scala、C++ |
| **其他** | RAG（LangChain、Chroma）、Agent（ReAct模式、Multi-Agent协作）、随机森林/XGBoost/CNN/RNN等经典ML |

---

## 项目实践

### 1. AI简历生成系统（体现Agent/RAG思路）
- 抓取 BOSS 直聘上 1000+ 大模型招聘职位，构建职位画像与职位匹配评分模型（基于BERT embedding + 多维度规则）
- 设计 Agent 流程：根据用户简历与目标职位匹配评分，自动调用 LLM（Qwen-2-7B）生成定制化简历内容，融入提示词工程与上下文记忆
- 技术栈：Python、LangChain、Chroma（RAG）、Qwen-2-7B、vLLM 推理、Flask 后端
- 成果：简历生成耗时<3秒，匹配度提升约30%（基于人工评估）

### 2. 小说续写模型（SFT + LoRA + DeepSpeed）
- 数据：白鹿原小说全文（约30万字）及续写风格标注，清洗后构建约1.2万条（上下文+续写）训练样本
- 基座模型：Qwen-2-7B，使用 LoRA 微调（rank=16, alpha=32），DeepSpeed ZeRO-3 训练，单卡 A100-80G 约6小时
- 训练后困惑度（perplexity）从 4.2 降至 2.8，续写内容风格与原著一致性获5人盲评平均4.3/5分
- 技术栈：Hugging Face Transformers、TRL（SFTTrainer）、DeepSpeed、PyTorch

### 3. AI英语对话系统（Agent + 提示词工程 + 上下文记忆）
- 场景：咖啡厅、机场、酒店等10种英语教学场景，模拟真实对话
- 设计 Agent：基于 DeepSeek 模型，通过提示词定义角色、场景、教学目标，并维护多轮对话历史（滑动窗口+摘要压缩）
- 引入记忆模块：将用户常犯语法错误存入短期记忆，在回复中隐式纠正
- 技术栈：DeepSeek API、LangChain、Chroma（记忆存储）、Streamlit 演示界面
- 成果：对话连贯性评分（GPT-4 评估）平均 4.6/5，用户留存率（试用用户中）达 70%

### 4. 狗狗皮肤病检测模型（多分类 + 特征工程）
- 数据：6种皮肤病类别，共 5000+ 图像（数据增强后 12000+）
- 方案：使用 XGBoost 配合 ResNet-50 提取的视觉特征（迁移学习），训练多分类模型
- 测试准确率 92.3%，F1-score 0.91，并部署为 Flask API 服务
- 此项目展现了从数据采集、特征提取到模型训练部署的完整工程能力

---

## 工作经历

### 腾讯 — 新闻与视频广告部门  
**后台开发 & 数据工程师** | 2020.07 ~ 2025.04

#### 24～25年：后台开发（与模型服务化、推理部署相关）
- **广告系统播放侧后台开发**：负责阅文流量接入、效果监测模块，涉及高并发 API 设计（日均请求量 5000w+），熟悉服务化部署与性能优化
- **用户画像数据归因分析后台**：处理微信ID、QQID、IMEI、IFA 等多源设备ID的归因效果分析，为广告模型提供高质量训练标签
- **内部运营系统开发**：使用 Django 框架搭建后台系统，结合 Spark、ClickHouse 进行数据统计与可视化

#### 20～24年：数据开发（与训练数据管道、特征工程相关）
- **广告效果模型数据流建设**：设计并实现离线（Spark）+ 实时（Flink）数据管道，涵盖特征提取、样本拼接、标签生成，支撑每日千万级模型训练样本产出
- **数仓建设与数据湖开发**：主导 Iceberg 数据湖架构搭建，实现数据 T+1 到实时流的平滑演进，提升模型迭代效率 40%
- **广告仿真链路开发**：构建 AMS 广告系统仿真环境实时通路，用于模型效果监测与离线评估，降低线上踩坑风险
- **点击/转化归因实时数据开发**：基于 Flink 开发实时归因链路，延迟<1分钟，支撑广告竞价模型的在线学习

**与目标职位的关联**：  
- 深度参与模型训练数据全链路（特征→样本→标签→评估），可无缝迁移至大模型数据构建与 SFT/RL 数据管道  
- 后台开发经验直接支撑模型服务化部署（vLLM、FastAPI）及 Agent 类应用的工程落地  
- 熟悉大规模分布式系统、容器化部署（Docker/K8s），具备生产环境稳定运行能力

---

## 转型经历

- **2024.05～2024.09**：系统学习机器学习基础（吴恩达课程）、线性代数/微积分/概率统计（3Blue1Brown、可汗学院）
- **2024.09～2024.12**：深度学习与多模态课程（fast.ai：深度学习、Stable Diffusion）
- **2025.01～2025.03**：大模型与强化学习专项（Hugging Face LLM Course、Deep RL Course）
- **2025.03～2025.04**：整合实践（happy-llm 项目、个人项目集中产出）
- **项目实践同期**：完成小说续写、AI英语对话、简历生成、皮肤病检测四个完整项目，涵盖 SFT、RLHF、RAG、Agent 等核心方向

---

## 基础知识

- **多模态**：CLIP、ViT、DiT、Stable Diffusion（VAE/DDPM/UNet）  
- **大语言模型**：Transformer 架构、SFT、LoRA/QLoRA、PPO/DPO/GRPO、RLHF、RAG、Agent/Multi-Agent  
- **强化学习**：PPO、DPO、GRPO 原理与 TRL