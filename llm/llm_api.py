import logging
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from openai import OpenAI
from model_config import MODEL_CONFIGS

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class LLMAPI:
    def __init__(self, api_key, model_type="deepseek"):
        """
        初始化LLM API客户端
        
        Args:
            api_key (str): API密钥
            model_type (str): 模型类型，默认为deepseek
        """
        if model_type not in MODEL_CONFIGS:
            raise ValueError(f"Unsupported model type: {model_type}")
        
        self.api_key = api_key
        self.model_type = model_type
        self.config = MODEL_CONFIGS[model_type]
        self.base_url = self.config["base_url"]
        self.default_model = self.config["model"]
        self.default_params = self.config["default_params"]
        
        # 初始化OpenAI客户端
        self.client = OpenAI(
            api_key=api_key,
            base_url=self.base_url
        )
    
    def chat_completion(self, messages, model=None, **kwargs):
        """
        调用LLM聊天完成API
        
        Args:
            messages (list): 消息列表，格式为[{"role": "user", "content": "..."}]
            model (str): 使用的模型，默认为配置中的模型
            **kwargs: 其他参数，如temperature, max_tokens, top_p等
        
        Returns:
            dict: API返回的响应结果
            
        Raises:
            Exception: 当API请求失败时抛出异常
        """
        try:
            # 使用默认模型或指定模型
            target_model = model or self.default_model
            
            logger.info(f"Sending request to {self.model_type} API with model: {target_model}")
            
            # 针对不同模型类型使用不同的调用方式
            if self.model_type == "ark":
                # 火山方舟API调用方式
                # 构建输入格式
                # 火山方舟API使用不同的输入格式
                input_text = ""
                for msg in messages:
                    if msg["role"] == "user":
                        content = msg["content"]
                        if isinstance(content, str):
                            input_text = content
                        elif isinstance(content, list):
                            # 处理多模态输入
                            for item in content:
                                if item.get("type") == "input_text":
                                    input_text = item.get("text", "")
                
                # 构建请求参数
                # 火山方舟API不支持max_tokens参数，需要使用不同的参数
                params = {
                    "model": target_model,
                    "input": input_text,
                }
                
                # 添加温度参数
                if "temperature" in self.default_params:
                    params["temperature"] = self.default_params["temperature"]
                if "temperature" in kwargs:
                    params["temperature"] = kwargs["temperature"]
                
                # 火山方舟API使用max_output_tokens而不是max_tokens
                if "max_tokens" in self.default_params:
                    params["max_output_tokens"] = self.default_params["max_tokens"]
                if "max_tokens" in kwargs:
                    params["max_output_tokens"] = kwargs["max_tokens"]
                
                # 添加top_p参数
                if "top_p" in self.default_params:
                    params["top_p"] = self.default_params["top_p"]
                if "top_p" in kwargs:
                    params["top_p"] = kwargs["top_p"]
                
                response = self.client.responses.create(**params)
                # 火山方舟API返回的格式不同，需要转换
                result = {
                    "id": response.id,
                    "object": "chat.completion",
                    "created": response.created,
                    "model": response.model,
                    "choices": [{
                        "index": 0,
                        "message": {
                            "role": "assistant",
                            "content": response.output
                        },
                        "finish_reason": "stop"
                    }],
                    "usage": {
                        "prompt_tokens": response.usage.input_tokens,
                        "completion_tokens": response.usage.output_tokens,
                        "total_tokens": response.usage.total_tokens
                    }
                }
            else:
                # 标准OpenAI API调用方式
                # 构建请求参数
                params = {
                    "model": target_model,
                    "messages": messages,
                    **self.default_params,
                    **kwargs
                }
                
                response = self.client.chat.completions.create(**params)
                
                # 将响应转换为字典格式
                result = response.model_dump()
            
            logger.info(f"Received response from {self.model_type} API: {result}")
            
            return result
            
        except Exception as e:
            logger.error(f"Error when calling {self.model_type} API: {str(e)}")
            raise Exception(f"{self.model_type} API request failed: {str(e)}")
    
    def get_completion_text(self, response):
        """
        从API响应中提取生成的文本
        
        Args:
            response (dict): API返回的响应结果
            
        Returns:
            str: 生成的文本内容
        """
        try:
            return response['choices'][0]['message']['content']
        except (KeyError, IndexError) as e:
            logger.error(f"Failed to extract completion text: {str(e)}")
            raise Exception(f"Failed to extract completion text: {str(e)}")

# 示例使用
if __name__ == "__main__":
    # 请替换为您的API密钥
    deepseek_api_key = ""
    ark_api_key = ""
    # 使用DeepSeek模型
    llm = LLMAPI(deepseek_api_key, model_type="deepseek")
    
    # 示例消息
    messages = [
        {"role": "user", "content": "Hello, how are you?"}
    ]
    
    try:
        # 调用API
        response = llm.chat_completion(messages)
        
        # 提取生成的文本
        completion_text = llm.get_completion_text(response)
        print(f"Generated text: {completion_text}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
