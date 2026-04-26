import json
import os
import sys
import random
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import project_root
from llm.llm_api import LLMAPI

class ModelEvaluator:
    def __init__(self):
        self.project_root = project_root
        self.jobs_file = os.path.join(self.project_root, "jd_data", "processed_jobs.json")
        self.prompt_template_file = os.path.join(self.project_root, "prompt", "prompt_template.md")
        self.evaluation_results_file = os.path.join(self.project_root, "result", "evaluation_results.json")
        self.personal_resume_file = os.path.join(self.project_root, "cv_data/origin_cv.md")
        
        # 初始化LLM API客户端
        deepseek_api_key = ""
        ark_api_key = ""
        qwen3_api_key = "empty"  # qwen3模型在本地部署，不需要API密钥
        # 使用deepseek模型
        self.api_key = deepseek_api_key
        self.llm = LLMAPI(self.api_key, model_type="deepseek")
    
    def load_jobs(self):
        """加载处理后的职位数据"""
        with open(self.jobs_file, 'r', encoding='utf-8') as f:
            jobs = json.load(f)
        print(f"加载了 {len(jobs)} 个职位")
        return jobs
    
    def load_prompt_template(self):
        """加载提示词模板"""
        with open(self.prompt_template_file, 'r', encoding='utf-8') as f:
            template = f.read()
        return template
    
    def load_personal_resume(self):
        """加载个人简历"""
        with open(self.personal_resume_file, 'r', encoding='utf-8') as f:
            return f.read()
    
    def generate_prompt(self, template, job):
        """根据职位信息生成提示词"""
        prompt = template.format(
            job_title=job.get("job_title", ""),
            company_name=job.get("company_name", ""),
            salary=job.get("salary", ""),
            experience=job.get("experience", ""),
            education=job.get("education", ""),
            location=job.get("location", ""),
            job_description=job.get("job_description", "")
        )
        return prompt
    
    def _create_empty_report(self, analysis, suggestion):
        """创建一个置0的评估结果"""
        total_score = 0
        
        scores = {
            "技术技能匹配度": 0,
            "项目经验匹配度": 0,
            "工作经历匹配度": 0,
            "基础知识匹配度": 0,
            "教育背景和转型经历": 0,
            "职位要求匹配度": 0
        }
        
        level = "差"
        
        report = {
            "总体评分": {
                "总分": total_score,
                "等级": level
            },
            "各维度评分": scores,
            "综合分析": analysis,
            "建议": suggestion
        }
        
        return report
    
    def model_call(self, prompt):
        """调用LLM API进行职位匹配度评估"""
        # 调用LLM API进行评估
        messages = [
            {"role": "user", "content": prompt}
        ]
        
        try:
            response = self.llm.chat_completion(messages, temperature=0.5, max_tokens=3000)
            evaluation_text = self.llm.get_completion_text(response)
            
            # 打印LLM返回的原始文本，以便调试
            print("LLM返回的原始文本:")
            print(evaluation_text)
            print("\n" + "-"*50 + "\n")
            
            # 尝试清理JSON字符串
            # 移除可能的多余字符
            evaluation_text = evaluation_text.strip()
            # 移除可能的Markdown代码块标记
            if evaluation_text.startswith('```json'):
                evaluation_text = evaluation_text[7:]
            if evaluation_text.endswith('```'):
                evaluation_text = evaluation_text[:-3]
            
            report = json.loads(evaluation_text)
            
            print(".....")
            # 验证评分格式
            if "总体评分" not in report or "各维度评分" not in report:
                raise ValueError("LLM返回的评估结果格式不正确")
            
            print(f"LLM评估完成，总分: {report['总体评分']['总分']}分")
            return report   
        except json.JSONDecodeError as e:
            print(f"LLM评估时JSON解析出错: {str(e)}")
            print(f"原始文本长度: {len(evaluation_text)}")
            print(f"原始文本前500字符: {evaluation_text[:500]}...")
            # 如果JSON解析失败，返回一个置0的评估结果
            return self._create_empty_report(
                "LLM返回的JSON格式不正确，返回一个置0的评估结果。",
                "请检查LLM返回的格式是否正确。"
            )
        except Exception as e:
            print(f"LLM评估时出错: {str(e)}")
            # 如果LLM调用失败，返回一个置0的评估结果
            return self._create_empty_report(
                "LLM调用失败，返回一个置0的评估结果。",
                "待排查。"
            )
    
    def evaluate_jobs(self, sample_size=10):
        """评估职位匹配度"""
        jobs = self.load_jobs()
        template = self.load_prompt_template()
        
        # 随机采样职位进行评估
        sampled_jobs = random.sample(jobs, min(sample_size, len(jobs)))
        print(f"随机采样 {len(sampled_jobs)} 个职位进行评估")
        
        results = []
        for i, job in enumerate(sampled_jobs):
            print(f"评估第 {i+1}/{len(sampled_jobs)} 个职位: {job.get('job_title', '')}")
            
            # 生成提示词
            prompt = self.generate_prompt(template, job)
            
            # 调用大模型（模拟）
            evaluation = self.model_call(prompt)
            
            # 保存评估结果
            result = {
                "job_id": job.get("job_id", ""),
                "job_title": job.get("job_title", ""),
                "company_name": job.get("company_name", ""),
                "salary": job.get("salary", ""),
                "evaluation": evaluation
            }
            results.append(result)
        
        # 保存评估结果
        with open(self.evaluation_results_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        print(f"评估完成，共评估 {len(results)} 个职位")
        return results

if __name__ == "__main__":
    evaluator = ModelEvaluator()
    evaluator.evaluate_jobs(sample_size=1)