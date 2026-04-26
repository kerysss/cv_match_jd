# 模型配置文件

# DeepSeek模型配置 
DEEPSEEK_CONFIG = {
    "base_url": "https://api.deepseek.com/v1",
    "model": "deepseek-reasoner",
    "default_params": {
        "temperature": 1.0,
        "max_tokens": 1024,
        "top_p": 1.0
    }
}

# Qwen/Qwen3.5-9B-Instruct
QWEN3_CONFIG = {
    "base_url": "http://192.168.1.100:8000/v1",
    "model": "Qwen/Qwen3.5-9B-Instruct",
    "default_params": {
        "temperature": 1.0,
        "max_tokens": 1024,
        "top_p": 1.0
    }
}

# 其他模型配置可以在这里添加
# 例如：
# OPENAI_CONFIG = {
#     "base_url": "https://api.openai.com/v1/chat/completions",
#     "model": "gpt-3.5-turbo",
#     "default_params": {
#         "temperature": 0.7,
#         "max_tokens": 1024,
#         "top_p": 1.0
#     }
# }

# 火山方舟模型配置
ARK_CONFIG = {
    "base_url": "https://ark.cn-beijing.volces.com/api/v3",
    "model": "doubao-seed-2-0-lite-260215",
    "default_params": {
        "temperature": 0.7,
        "max_tokens": 1024,
        "top_p": 1.0
    }
}

# 模型配置映射
MODEL_CONFIGS = {
    "deepseek": DEEPSEEK_CONFIG,
    "ark": ARK_CONFIG,
    "qwen3": QWEN3_CONFIG,
    # 可以添加其他模型配置
    # "openai": OPENAI_CONFIG,
}
