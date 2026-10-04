from fastapi import FastAPI

from app.models.component import Component
from app.models.compatibility_rule import CompatibilityRule
from app.models.project import Project
from app.models.recommendation import Recommendation
from app.models.requirement import Requirement

from app.api.components import router as components_router
from app.api.projects import router as projects_router
from app.api.recommendations import router as recommendations_router


app = FastAPI(
    title="Engineering Project Design Platform",
    description="AI-assisted engineering project planning and component recommendation system",
    version="0.1.0",
)


app.include_router(projects_router)
app.include_router(components_router)
app.include_router(recommendations_router)


@app.get("/")
def root():
    return {
        "name": "Engineering Project Design Platform",
        "status": "online",
        "version": "0.1.0",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }