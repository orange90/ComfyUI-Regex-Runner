import re

class RegexNode:
    """用于执行正则表达式操作的节点"""
    
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_text": ("STRING", {"default": "", "multiline": True}),
                "pattern": ("STRING", {"default": ""}),
                "replace_with": ("STRING", {"default": ""}),
            },
            "optional": {
                "mode": (["search", "replace", "findall"], {"default": "search"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "execute_regex"
    CATEGORY = "text"

    def execute_regex(self, input_text, pattern, replace_with="", mode="search"):
        try:
            if mode == "search":
                match = re.search(pattern, input_text)
                return (match.group(0) if match else "",)
            
            elif mode == "replace":
                result = re.sub(pattern, replace_with, input_text)
                return (result,)
            
            elif mode == "findall":
                matches = re.findall(pattern, input_text)
                return ("\n".join(matches) if matches else "",)
            
        except re.error as e:
            print(f"正则表达式错误: {str(e)}")
            return ("",)
        except Exception as e:
            print(f"执行错误: {str(e)}")
            return ("",)

# 注册节点
NODE_CLASS_MAPPINGS = {
    "RegexNode": RegexNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RegexNode": "Regex Operations"
} 