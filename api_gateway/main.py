from fastapi import FastAPI
import uvicorn
from config.settings import settings
from api_gateway.routes.auth import auth_router
from config.logger import setup_logging
import logging
from contextlib import asynccontextmanager

setup_logging()

logger=logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application is starting")
    yield
    logger.info("Application is shutting down")

app=FastAPI(
    title="AI-Learning and Notes taking",
    version="1.0",
    lifespan=lifespan,
    description="Backend to track calories of meals using AI and record progress/goals.",
)

app.include_router(auth_router)

@app.get("/")
async def root_route():
    logger.info("Route route was accessed")
    return {"message":"Service is running"}

if __name__ == "__main__":
    uvicorn.run(app,host=settings.APP_HOST,port=settings.APP_PORT,reload=settings.RELOAD)
