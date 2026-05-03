class PromptEnhancer:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "user_prompt": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "template": ("STRING", {
                    "multiline": True,
                    "default": "masterpiece, best quality, {prompt}"
                }),
            },
            "optional": {
                "model_select": ([
                    "none",
                    "gemma3:2b",
                    "gemma3:7b",
                    "gemma3:12b",
                    "gemma3:27b"
                ],)
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("enhanced_prompt",)
    FUNCTION = "enhance"

    CATEGORY = "Prompt"

    def enhance(self, user_prompt, template, model_select="none"):
        # 1. 基础替换
        if "{prompt}" in template:
            enhanced = template.replace("{prompt}", user_prompt)
        else:
            enhanced = template + ", " + user_prompt

        # 2. 模型风格增强
        model_styles = {
            "gemma3:2b": "concise, simple description",
            "gemma3:7b": "detailed, natural language, vivid",
            "gemma3:12b": "highly detailed, cinematic, expressive",
            "gemma3:27b": "ultra detailed, professional photography, complex lighting"
        }

        if model_select in model_styles:
            enhanced += ", " + model_styles[model_select]

        return (enhanced,)


NODE_CLASS_MAPPINGS = {
    "PromptEnhancer": PromptEnhancer
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptEnhancer": "Prompt Enhancer (Gemma3)"
}