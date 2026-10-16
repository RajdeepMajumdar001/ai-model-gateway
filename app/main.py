from contextlib import asynccontextmanager
from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from app.routes.testing import router as testing_router

from app.routes.inference import router as inference_router
from app.routes.models import router as models_router

from app.routes.health import router as health_router

from app.middleware.http import RequestIDMiddleware
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("AI model gateway starting ...")
    yield
    print("AI model gateway shutting down...")


app = FastAPI(
    title="AI Model Gateway",
    description="API gateway for AI model inference",
    version="1.0.0",
    lifespan = lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.exception_handler(Exception)
async def global_exception_handler(request:Request , exc: Exception):
    return JSONResponse(
        status_code = 500,
        content = {"detail":"Internal Server Error"}
    )

app.add_middleware(RequestIDMiddleware)
# Register the inference router with our main application
app.include_router(inference_router)
app.include_router(testing_router)
app.include_router(models_router)
app.include_router(health_router)


# Simple test endpoint
@app.get("/")
def root():
    return {"message": "AI Model Gateway is running"}