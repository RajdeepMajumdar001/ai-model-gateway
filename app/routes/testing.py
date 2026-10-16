from fastapi import APIRouter

router = APIRouter(
    prefix="/test",
    tags = ["Testing"]
)
@router.get(
        "/error",
        summary="Test global error handling",
        description="Intentionally raises an internal server error to verify the gateway's global exception handler."
)
def test_error():

    raise RuntimeError("Test internal server error")