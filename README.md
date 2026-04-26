# cv_match_jd
AI简历生成系统（2026.03 - 2026.04）

- **目标**：从Boss直聘抓取1000+大模型职位，构建职位匹配打分系统，为候选人自动生成定制简历。

- **方法**：使用agent写爬虫脚本爬boss简历，尝试一周后都失败了，后面换谷歌爬虫插件成功实现数据采集；使用pandas做数据清洗过滤；设计简历匹配评估和生成简历的prompt；部署Qwen3-8B的大模型提供api服务，对比调用自己部署的ai服务和Deepseek-v4等商业模型，发现deepseek在花费和质量上都有优势，因此使用deepseek进行匹配评估以及根据匹配结果重写简历内容。

- **技术栈**：Python、Pandas、Openai、Vllm、Transformer

- **亮点**：涉及数据挖掘、prompt工程、模型部署。
