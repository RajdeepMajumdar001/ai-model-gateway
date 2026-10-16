from fastapi import APIRouter,Depends,Request 
from app.dependencies.model import get_model
from app.schemas.inference import GenerateRequest, GenerateResponse
from app.services.inference import InferenceService

router = APIRouter(
    prefix="/inference",
    tags=["Inference"]
)
@router.post(
    "/generate",
    response_model=GenerateResponse,
    summary="Generate an AI response",
    description="Runs inference using the selected AI model and returns the generated response with request metadata."
)
def generate(
    request:Request,
    body: GenerateRequest,
    model=Depends(get_model)
):
    service = InferenceService(model)
    result = service.generate(body.prompt)

    return GenerateResponse(
        request_id=request.state.request_id,
        model=body.model,
        model_version="v2",
        response=result,
        latency_ms=0.0

    )