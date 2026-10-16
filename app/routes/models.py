from fastapi import APIRouter

router = APIRouter(
    prefix="/models",
    tags=["Models"]
)
@router.get("",
           summary="List available AI models",
            description="Returns the AI models currently registered and available for inference." )
def get_models():
    return {
        "models":[
            {
                "name":"llama-3.1",
                "version":"v2"
            }
        ]
    }