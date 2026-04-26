import json
import os
import random
from config import project_root

class FilterChecker:
    def __init__(self):
        self.project_root = project_root
        self.evaluation_results_file = os.path.join(self.project_root, "result", "evaluation_results.json")
        self.filtered_jobs_file = os.path.join(self.project_root, "result", "filtered_jobs.json")
        self.check_report_file = os.path.join(self.project_root, "result", "check_report.md")
    
    def load_evaluation_results(self):
        """加载评估结果"""
        with open(self.evaluation_results_file, 'r', encoding='utf-8') as f:
            results = json.load(f)
        print(f"加载了 {len(results)} 个评估结果")
        return results
    
    def filter_jobs(self, results):
        """过滤职位（80分以上）"""
        filtered_jobs = []
        for result in results:
            total_score = result['evaluation']['总体评分']['总分']
            if total_score >= 80:
                filtered_jobs.append(result)
        
        # 保存过滤后的职位
        with open(self.filtered_jobs_file, 'w', encoding='utf-8') as f:
            json.dump(filtered_jobs, f, ensure_ascii=False, indent=2)
        
        print(f"过滤完成，共 {len(filtered_jobs)} 个职位达到推荐标准（80分以上）")
        return filtered_jobs
    
    def sample_check(self, results, filtered_jobs, sample_size=5):
        """抽样检查"""
        if len(results) <= sample_size:
            sample_jobs = results
        else:
            sample_jobs = random.sample(results, sample_size)
        
        # 生成检查报告
        report = "# 职位匹配度检查报告\n\n"
        report += f"## 总体情况\n"
        report += f"- 评估职位总数: {len(self.load_evaluation_results())}\n"
        report += f"- 过滤后职位数: {len(filtered_jobs)}\n"
        report += f"- 抽样检查职位数: {len(sample_jobs)}\n\n"
        
        report += "## 抽样检查详情\n"
        for i, job in enumerate(sample_jobs):
            report += f"### 职位 {i+1}\n"
            report += f"- 职位标题: {job.get('job_title', '')}\n"
            report += f"- 公司名称: {job.get('company_name', '')}\n"
            report += f"- 薪资范围: {job.get('salary', '')}\n"
            report += f"- 评分: {job['evaluation']['总体评分']['总分']}分 ({job['evaluation']['总体评分']['等级']})\n"
            report += f"- 综合分析: {job['evaluation']['综合分析']}\n"
            report += f"- 建议: {job['evaluation']['建议']}\n\n"
        
        # 保存检查报告
        with open(self.check_report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"抽样检查完成，生成了检查报告")
        return sample_jobs
    
    def run(self):
        """运行过滤和检查流程"""
        results = self.load_evaluation_results()
        filtered_jobs = self.filter_jobs(results)
        self.sample_check(results, filtered_jobs)

if __name__ == "__main__":
    checker = FilterChecker()
    checker.run()