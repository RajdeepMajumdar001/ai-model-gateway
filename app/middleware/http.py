import logging
import uuid
import time
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger("AI-model-gateway")

logger.setLevel(logging.INFO)

class RequestIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request , call_next):
        
        start_time = time.perf_counter()

        request_id = str(uuid.uuid4())

        request.state.request_id = request_id

        response = await call_next(request)

        end_time = time.perf_counter()

        latency_ms = (end_time  - start_time)*1000

        request.state.latency_ms = latency_ms

        response.headers["X-Response-Time-ms"] = str(round(latency_ms,2))

        response.headers["X-Content-Type-Options"] = "nosniff"

        response.headers["X-Frame-Options"] = "DENY"

        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"

        response.headers["X-Request-ID"]  = request_id

        logger.info(
            f">{request.method}{request.url.path}"
            f"<{response.status_code}     | {latency_ms:.2f} ms"       
                    )
        return response