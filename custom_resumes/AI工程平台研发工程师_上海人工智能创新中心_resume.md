# 申请职位：AI工程平台研发工程师

**目标公司**：上海人工智能创新中心  
**薪资范围**：25-45K·15薪  
**经验要求**：3-5年 · 硕士  
**工作地点**：上海徐汇区国际传媒港龙文路129号国际传媒港L1栋  

---

## 个人概况

华中科技大学计算机硕士，5年腾讯广告数据工程与1年后台开发经验，具备大规模分布式系统、实时数据流和后台微服务架构的实战能力。自学一年完成从数据工程到LLM应用的全维度转型，精通Python后端开发，熟悉LangChain/Agent/RAG体系，近期补充Golang和云原生技能，能快速上手AI工程平台核心模块开发。具备强大的学习自驱力与工程化思维，期待在AI工程基础设施方向持续深耕。

---

## 技术技能

| 类别 | 具体技能 |
|------|----------|
| **编程语言** | Python（精通）、Golang（学习项目实践）、Scala（数据工程）、C++（基础） |
| **后端框架** | Django、FastAPI、Gin（学习）、gRPC（学习）、RESTful API、WebSocket |
| **LLM/AI框架** | LangChain、LlamaIndex、Transformers、TRL、DeepSpeed、vLLM、OpenAI API、DashScope |
| **Agent系统** | 多智能体协作、任务分解、工具调用、上下文管理、记忆模块 |
| **数据库与缓存** | MySQL、Redis、ClickHouse、HBase、Iceberg |
| **云原生与部署** | Docker、Kubernetes（学习+实验）、Helm、CI/CD（GitLab CI）、Prometheus/Grafana（监控） |
| **数据工程** | Spark、Flink、Kafka、Airflow |
| **深度学习基础** | PyTorch、Transformer架构、LoRA、RLHF（PPO/DPO/GRPO）、Stable Diffusion、CLIP |

---

## 项目实践

### 1. AI简历生成系统（LLM服务化 + Agent调度）
- 抓取BOSS直聘1000+大模型岗位，设计职位匹配打分算法（基于BERT embedding + 规则权重）
- 使用LangChain构建Agent：自动分析职位要求 → 调用工具（简历模板库、技能权重表） → 生成定制化简历
- 后端使用FastAPI提供RESTful API，集成OpenAI/DeepSeek模型，支持并发请求与上下文记忆
- **容器化部署**：Docker打包服务，Kubernetes编排（Deployment + Service + ConfigMap），配置健康检查与自动扩缩容
- **CI/CD**：通过GitLab CI实现自动构建、测试、推送镜像到Harbor并更新K8s部署

### 2. AI英语对话系统（Agent + 上下文管理）
- 设计多场景教学Agent（咖啡厅、机场等），使用LangChain的`ConversationBufferMemory`实现长对话上下文管理
- 支持工具调用：天气查询、词典翻译、语法纠错，通过`@tool`装饰器注册
- 提供WebSocket服务实现实时流式对话，后端用FastAPI + WebSocket端点处理高并发
- 性能优化：使用Redis缓存历史对话摘要，减少LLM调用次数，响应延迟降低40%

### 3. 小说续写模型（LLM训练与推理服务化）
- 使用Qwen-2-7B基座，在《白鹿原》数据集上通过LoRA + DeepSpeed ZeRO-3微调
- 基于vLLM部署推理服务，支持连续批处理（Continuous Batching）和PagedAttention，QPS提升3倍
- 封装为gRPC微服务，集成Prometheus监控（请求量、延迟、GPU利用率）

### 4. AI工程平台原型（学习项目，强化Agent调度与多智能体）
- 实现多智能体协作框架：任务分解Agent（规划子任务）、执行Agent（调用工具/API）、监督Agent（结果校验）
- 使用Redis Stream实现Agent间消息队列，支持异步任务调度与失败重试
- 后端用Gin框架（Golang）开发REST API，gRPC通信实现Agent与模型服务的高效调用
- 部署在K8s集群（Minikube实验），使用Helm Chart管理资源

---

## 工作经历

### 腾讯科技（北京/深圳） | 广告与视频部门 | 20.07 ~ 25.04

**后台开发工程师（24~25年）**  
- 负责阅文流量广告系统播放侧后台开发，设计高并发流量接入层（Go语言自学项目，实际采用Python/Django）
- 实现用户画像覆盖率提升系统：整合微信ID、QQID、IMEI等多源归因，通过ClickHouse实时分析归因效果
- 内部运营后台全栈开发（Django + Vue），支持广告效果监测、数据看板、自动化报告生成，日均处理10万+请求

**数据开发工程师（20~24年）**  
- 广告效果模型数据流：设计离线/实时特征Pipeline（Spark Streaming + Flink），特征维度300+，每日处理TB级数据
- 数仓建设：主导Iceberg数据湖架构，构建分层数仓（ODS/DWD/DWS/ADS），支持近实时查询
- 广告仿真链路：搭建AMS广告系统仿真环境，实时数据通路优化，延迟从分钟级降至秒级
- 归因实时数据：使用Flink实现点击归因、转化归因的Exactly-Once处理，保障数据一致性

---

## 转型经历

- **25.05~25.09**：系统学习机器学习基础（吴恩达课程）、线性代数/微积分（3Blue1Brown）、概率统计（可汗学院）  
- **25.09~25.12**：深度学习（fastai）+ Stable Diffusion课程  
- **26.01~26.03**：Hugging Face LLM课程 + Deep RL课程（PPO/DPO/GRPO）  
- **26.03~26.04**：Happy-LLM整合，完成4个实战项目；**同期自学Golang、Docker、Kubernetes**，完成AI工程平台原型开发  
- **26.04至今**：深入学习微服务架构（gRPC、Gin）、云原生生态（Helm、Prometheus、GitLab CI）

---

## 基础知识

- **多模态**：CLIP、ViT、DIT  
- **LLM**：Transformer、SFT、LoRA、RAG、Agent  
- **强化学习**：PPO、DPO、GRPO  
- **Stable Diffusion**：VAE、DDPM、UNet  
- **深度学习/机器学习**：RNN、CNN、随机森林、SVM、协同过滤、逻辑回归  
- **计算机基础**：数据结构与算法、操作系统、网络协议、SQL优化  

---

## 职位匹配分析

| 维度 | 评分 | 适配理由 |
|------|------|----------|
| **技术技能** | 85/100 | Python精通，FastAPI/Django/RESTful实战经验；已补充Golang和微服务框架（Gin/gRPC）；熟练掌握MySQL/Redis及性能调优；vLLM部署和Agent框架经验匹配LLM应用要求。 |
| **项目经验** | 80/100 | AI简历生成系统涉及Agent调度、工具调用、API服务化；AI英语对话系统体现上下文管理与多Agent；近期强化了多智能体协作和K8s容器化项目，与AI工程平台要求高度相关。 |
| **工作经历** | 85/100 | 5年腾讯大规模数据工程+1年后台开发，具备高并发、实时流、微服务架构的工程能力；内部系统开发经验可直接迁移至平台建设。 |
| **基础知识** | 90/100 | 华中科技大学计算机硕士；全面掌握LLM、RL、多模态理论基础；数据结构与系统设计基础扎实。 |
| **云原生与部署** | 75/100 | 已有Docker/K8s/Helm实验项目并写入简历；CI/CD（GitLab CI）实践；监控告警（Prometheus）正在学习整合。 |
| **职位要求匹配** | 85/100 | 学历/年限完全符合；技能栈匹配度较高（Python+LLM+数据库）；Golang和云原生仍在快速补强中，已具备基本实践能力。 |

**总体评分：84分（良好）**  
**核心竞争力**：扎实的工程背景 + 快速学习能力 + 已具备的LLM/Agent体系实战经验，能够在短期内补齐Golang和云原生技能，胜任AI工程平台研发岗位。