import pandas as pd
import os
import json
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import project_root

class DataProcessor:
    def __init__(self):
        self.project_dir = os.path.join(project_root, "jd_data")
        self.csv_files = [
            "大模型算法职位450个.csv"
        ]
        os.makedirs(self.project_dir, exist_ok=True)
    
    def load_csv(self, file_name):
        """加载CSV文件"""
        file_path = os.path.join(self.project_dir, file_name)
        try:
            # 跳过第一行（文件名），从第二行开始作为列名
            df = pd.read_csv(file_path, skiprows=1)
            print(f"成功加载 {file_name}，共 {len(df)} 条记录")
            print(f"列名: {list(df.columns)}")
            return df
        except Exception as e:
            print(f"加载 {file_name} 失败: {e}")
            return None
    
    def process_xiaohongshu(self, df):
        """处理小红书招聘职位数据"""
        jobs = []
        for _, row in df.iterrows():
            # 跳过空行
            if pd.isna(row.get('web_scraper_order')):
                continue
            
            job = {
                "job_id": str(row.get("web_scraper_order", "")),
                "job_title": str(row.get("item_page_title", row.get("title", ""))),
                "salary": str(row.get("data", "")),
                "experience": str(row.get("data_3", "")),
                "education": str(row.get("data_4", "")),
                "job_description": str(row.get("job_responsibilities", "")),
                "company_name": str(row.get("Company_Name", "")),
                "location": str(row.get("work_address", "")),
                "source": "小红书"
            }
            # 过滤空职位
            if job["job_title"] and job["company_name"]:
                jobs.append(job)
        return jobs
    
    def process_model_jobs(self, df, source):
        """处理大模型算法职位数据"""
        jobs = []
        for _, row in df.iterrows():
            # 跳过空行
            if pd.isna(row.get('web_scraper_order')):
                continue
            
            job = {
                "job_id": str(row.get("web_scraper_order", "")),
                "job_title": str(row.get("item_page_title", row.get("title", ""))),
                "salary": str(row.get("salary", "")),
                "experience": str(row.get("data", "")),
                "education": str(row.get("data_1", "")),
                "job_description": str(row.get("Job_Description", "")),
                "company_name": str(row.get("name_1", row.get("name2", ""))),
                "location": str(row.get("company_address", "")),
                "source": source
            }
            # 过滤空职位
            if job["job_title"] and job["company_name"]:
                jobs.append(job)
        return jobs
    
    def process_all_data(self):
        output_file = os.path.join(self.project_dir, "processed_jobs.json")
        if os.path.exists(output_file):
            print(f"文件 {output_file} 已存在，跳过处理")
            with open(output_file, 'r', encoding='utf-8') as f:
                jobs = json.load(f)
            return jobs

        """处理所有CSV数据"""
        all_jobs = []
        
        # 处理小红书数据
        # xhs_df = self.load_csv(self.csv_files[0])
        # if xhs_df is not None:
        #     xhs_jobs = self.process_xiaohongshu(xhs_df)
        #     all_jobs.extend(xhs_jobs)
        
        # 处理大模型算法职位477个
        model1_df = self.load_csv(self.csv_files[1])
        if model1_df is not None:
            model1_jobs = self.process_model_jobs(model1_df, "大模型算法职位477个")
            all_jobs.extend(model1_jobs)
        
        # 处理大模型算法职位450个
        model2_df = self.load_csv(self.csv_files[2])
        if model2_df is not None:
            model2_jobs = self.process_model_jobs(model2_df, "大模型算法职位450个")
            all_jobs.extend(model2_jobs)
        
        # 去重
        unique_jobs = self.remove_duplicates(all_jobs)
        
        # 保存处理后的数据
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(unique_jobs, f, ensure_ascii=False, indent=2)
        
        print(f"数据处理完成，共 {len(unique_jobs)} 个职位")
        return unique_jobs
    
    def remove_duplicates(self, jobs):
        """去重职位数据"""
        seen = set()
        unique_jobs = []
        for job in jobs:
            key = (job.get("job_title", ""), job.get("company_name", ""))
            if key not in seen and key != ("", ""):
                seen.add(key)
                unique_jobs.append(job)
        return unique_jobs

if __name__ == "__main__":
    processor = DataProcessor()
    processor.process_all_data()