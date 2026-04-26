import os
import sys

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_processor import DataProcessor
from model_evaluator import ModelEvaluator
from filter_checker import FilterChecker
from resume_generator import ResumeGenerator
from config import project_root

class CVMatchSystem:
    def __init__(self):
        self.project_root = project_root
    
    def run(self):
        """运行完整的简历-职位匹配系统"""
        print("=== 简历-职位匹配系统 ===\n")
        
        # 1. 数据处理
        print("1. 数据处理")
        processor = DataProcessor()
        jobs = processor.process_all_data()
        print("1. 数据处理完成")
        
        # 2. 职位评估
        print("2. 职位评估")
        evaluator = ModelEvaluator()
        results = evaluator.evaluate_jobs(sample_size=1000)  # 评估所有职位
        print("2. 职位评估完成")
        
        # 3. 过滤和检查
        print("3. 过滤和检查")
        checker = FilterChecker()
        checker.run()
        print("3. 过滤和检查完成")
        
        # 4. 生成定制化简历
        print("4. 生成定制化简历")
        generator = ResumeGenerator()
        resumes = generator.generate_resumes()
        print("4. 生成定制化简历完成")
        
        print("=== 系统运行完成 ===")
        print(f"- 处理职位数: {len(jobs)}")
        print(f"- 评估职位数: {len(results)}")
        print(f"- 过滤后职位数: {len(resumes)}")
        print(f"- 生成简历数: {len(resumes)}")

if __name__ == "__main__":
    system = CVMatchSystem()
    system.run()