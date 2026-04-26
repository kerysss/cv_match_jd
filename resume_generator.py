import json
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import project_root
from llm.llm_api import LLMAPI

class ResumeGenerator:
    def __init__(self):
        self.project_root = project_root
        self.filtered_jobs_file = os.path.join(self.project_root, "result", "filtered_jobs.json")
        self.processed_jobs_file = os.path.join(self.project_root, "jd_data", "processed_jobs.json")
        self.resumes_dir = os.path.join(self.project_root, "custom_resumes")
        self.personal_resume_file = os.path.join(self.project_root, "cv_data/origin_cv.md")
        os.makedirs(self.resumes_dir, exist_ok=True)
        
        # 初始化LLM API客户端
        deepseek_api_key = ""
        ark_api_key = ""
        qwen3_api_key = "empty"  # qwen3模型在本地部署，不需要API密钥
        # 使用deepseek模型
        self.api_key = deepseek_api_key
        self.llm = LLMAPI(self.api_key, model_type="deepseek")
    
        
        # 加载完整职位数据到内存，避免重复读取文件
        self.processed_jobs_dict = self._load_processed_jobs_dict()
    
    def load_filtered_jobs(self):
        """加载过滤后的职位数据"""
        with open(self.filtered_jobs_file, 'r', encoding='utf-8') as f:
            jobs = json.load(f)
        print(f"加载了 {len(jobs)} 个过滤后的职位")
        return jobs
    
    def _load_processed_jobs_dict(self):
        """加载完整职位数据并构建字典，以job_id为键"""
        with open(self.processed_jobs_file, 'r', encoding='utf-8') as f:
            jobs = json.load(f)
        jobs_dict = {job['job_id']: job for job in jobs}
        print(f"加载了 {len(jobs_dict)} 个完整职位数据")
        return jobs_dict
    
    def get_full_job_info(self, job):
        """根据job_id获取完整的职位信息"""
        job_id = job.get('job_id')
        if job_id and job_id in self.processed_jobs_dict:
            full_job = self.processed_jobs_dict[job_id].copy()
            # 保留filtered_jobs中的evaluation信息
            if 'evaluation' in job:
                full_job['evaluation'] = job['evaluation']
            return full_job
        return job
    
    def load_personal_resume(self):
        """加载个人简历"""
        with open(self.personal_resume_file, 'r', encoding='utf-8') as f:
            return f.read()
    
    def load_resume_template(self):
        """加载简历提示词模板"""
        template_path = os.path.join(self.project_root, "prompt", "resume_template.md")
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def generate_prompt(self, job, personal_resume):
        """生成简历提示词"""
        template = self.load_resume_template()
        
        # 获取评估结果并格式化为字符串
        evaluation = job.get('evaluation', {})
        evaluation_text = ""
        if evaluation:
            total_score = evaluation.get('总体评分', {})
            scores = evaluation.get('各维度评分', [])
            analysis = evaluation.get('综合分析', '')
            suggestion = evaluation.get('建议', '')
            
            evaluation_text = f"总体评分：{total_score.get('总分', 0)}分 ({total_score.get('等级', '无')})\n\n"
            evaluation_text += "各维度评分：\n"
            for score in scores:
                evaluation_text += f"- {score.get('维度名称', '')}: {score.get('分数', 0)}分\n"
                if score.get('匹配点'):
                    evaluation_text += f"  匹配点: {score.get('匹配点', '')}\n"
                if score.get('不匹配点'):
                    evaluation_text += f"  不匹配点: {score.get('不匹配点', '')}\n"
            
            evaluation_text += f"\n综合分析：{analysis}\n"
            evaluation_text += f"建议：{suggestion}\n"
        else:
            evaluation_text = "暂无评估结果"
        
        return template.format(
            job_title=job.get("job_title", ""),
            company_name=job.get("company_name", ""),
            salary=job.get("salary", ""),
            experience=job.get("experience", ""),
            education=job.get("education", ""),
            location=job.get("location", ""),
            job_description=job.get("job_description", ""),
            personal_resume=personal_resume,
            evaluation=evaluation_text
        )
    
    def generate_custom_resume(self, job):
        """为职位生成定制化简历"""
        # 获取完整的职位信息
        full_job = self.get_full_job_info(job)
        
        job_title = full_job.get('job_title', '').replace('/', '_').replace(' ', '_')
        company_name = full_job.get('company_name', '').replace('/', '_').replace(' ', '_')
        resume_filename = f"{job_title}_{company_name}_resume.md"
        resume_path = os.path.join(self.resumes_dir, resume_filename)
        
        # 加载个人简历
        personal_resume = self.load_personal_resume()
        
        # 生成提示词
        prompt = self.generate_prompt(full_job, personal_resume)
        
        # 调用LLM API生成简历
        messages = [
            {"role": "user", "content": prompt}
        ]
        
        try:
            response = self.llm.chat_completion(messages, temperature=0.7, max_tokens=2000)
            resume_content = self.llm.get_completion_text(response)
            
            # 保存定制化简历
            with open(resume_path, 'w', encoding='utf-8') as f:
                f.write(resume_content)
            
            print(f"已生成定制化简历: {resume_filename}")
            return resume_path
            
        except Exception as e:
            print(f"生成简历时出错: {str(e)}")
            # 如果LLM调用失败，生成一个简单的简历
            resume_content = f"# LLM调用失败的定制化简历\n\n"
            resume_content += f"## 申请职位\n"
            resume_content += f"- 职位标题: {full_job.get('job_title', '')}\n"
            resume_content += f"- 公司名称: {full_job.get('company_name', '')}\n"
            resume_content += f"- 薪资范围: {full_job.get('salary', '')}\n\n"
            resume_content += f"## 职位匹配分析\n"
            resume_content += f"- 匹配度评分: {full_job['evaluation']['总体评分']['总分']}分 ({full_job['evaluation']['总体评分']['等级']})\n"
            resume_content += f"- 综合分析: {full_job['evaluation']['综合分析']}\n"
            
            with open(resume_path, 'w', encoding='utf-8') as f:
                f.write(resume_content)
            
            return resume_path
    
    def generate_resumes(self):
        """为所有过滤后的职位生成定制化简历"""
        jobs = self.load_filtered_jobs()
        generated_resumes = []
        
        for i, job in enumerate(jobs):
            print(f"生成第 {i+1}/{len(jobs)} 个定制化简历: {job.get('job_title', '')}")
            resume_path = self.generate_custom_resume(job)
            generated_resumes.append(resume_path)
        
        print(f"定制化简历生成完成，共生成 {len(generated_resumes)} 个简历")
        return generated_resumes

if __name__ == "__main__":
    generator = ResumeGenerator()
    generator.generate_resumes()