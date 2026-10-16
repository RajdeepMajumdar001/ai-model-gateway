from pydantic import BaseModel,Field

class GenerateRequest(BaseModel):
    prompt: str = Field(
        min_length=1,
        examples=["explain transformers in simple terms"]
        )
    model: str = Field(
        min_length=1,
        examples=["llama-3.1"]
        )
    temperature: float = Field(
        ge=0,
        le=2,
        examples=[0.7]
        )

class GenerateResponse(BaseModel):
    request_id: str
    model: str
    model_version: str
    response: str
    latency_ms: float

    model_config = {
        "json_schema_extra": {
            "example": {
                "request_id": "a2837b53-cc6c-4da6-bb87-f8d8498d0107",
                "model": "llama-3.1",
                "model_version": "v2",
                "response": "Transformers are neural network architectures...",
                "latency_ms": 2.99
            }
        }
    }
