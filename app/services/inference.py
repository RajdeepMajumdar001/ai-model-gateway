class InferenceService:
    def __init__(self,model):
        self.model = model

    def generate(self,prompt:str):
        return self.model.generate(prompt)    