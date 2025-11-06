from fastapi import FastAPI
from src.api.routes import router as api_router

app = FastAPI(
    title="GenTales00 API",
    description="API for GenTales00 project",
    version="1.0.0"
)

# Include API routes with /api prefix
app.include_router(api_router, prefix="/api")

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the GenTales00 API!",
        "version": "1.0.0",
        "docs": "/docs"
    }