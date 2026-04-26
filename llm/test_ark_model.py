import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from llm_api import LLMAPI

# 从环境变量获取API密钥
api_key = os.getenv('ARK_API_KEY')

if not api_key:
    print("请先设置环境变量 ARK_API_KEY")
    print("设置方法：export ARK_API_KEY=your_api_key_here")
    sys.exit(1)

# 初始化LLM API客户端，使用火山方舟模型
llm = LLMAPI(api_key, model_type="ark")

# 测试文本生成
test_messages = [
    {"role": "user", "content": "你好，你是谁？"}
]

print("测试火山方舟模型...")
try:
    # 调用API
    response = llm.chat_completion(test_messages)
    
    # 提取生成的文本
    completion_text = llm.get_completion_text(response)
    print(f"生成的文本: {completion_text}")
    
    print("\n测试成功！")
except Exception as e:
    print(f"测试失败: {str(e)}")

# 测试多模态输入（如果需要）
print("\n测试多模态输入...")
multimodal_messages = [
    {
        "role": "user", 
        "content": [
            {
                "type": "input_image",
                "image_url": "https://ark-project.tos-cn-beijing.volces.com/doc_image/ark_demo_img_1.png"
            },
            {
                "type": "input_text",
                "text": "你看见了什么？"
            }
        ]
    }
]

try:
    # 调用API
    response = llm.chat_completion(multimodal_messages)
    
    # 提取生成的文本
    completion_text = llm.get_completion_text(response)
    print(f"生成的文本: {completion_text}")
    
    print("\n多模态测试成功！")
except Exception as e:
    print(f"多模态测试失败: {str(e)}")
