from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags =["Health"]
)
@router.get(
        "",
        summary="Check API health",
        description="Returns the currrnt health status of the AI model gateway"
)
def health_check():
    return{"status":"healthy"}