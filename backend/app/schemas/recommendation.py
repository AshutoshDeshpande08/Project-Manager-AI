from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class RecommendationBase(BaseModel):
    project_id: int
    component_id: int

    role: str

    compatibility_score: float

    electrical_score: float = 0.0
    functional_score: float = 0.0
    interface_score: float = 0.0
    power_score: float = 0.0
    physical_score: float = 0.0
    environmental_score: float = 0.0
    performance_score: float = 0.0
    cost_score: float = 0.0
    availability_score: float = 0.0
    complexity_score: float = 0.0

    estimated_cost: float | None = None

    quantity: int = 1

    reasons: list = Field(default_factory=list)
    warnings: list = Field(default_factory=list)
    alternatives: list = Field(default_factory=list)


class RecommendationCreate(RecommendationBase):
    pass


class RecommendationResponse(RecommendationBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)