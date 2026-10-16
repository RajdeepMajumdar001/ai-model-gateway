
class ModelManager:
    def generate(self,prompt: str):
        return f"AI response generated for: {prompt}"

model_manager = ModelManager()
def get_model():
    return model_manager    