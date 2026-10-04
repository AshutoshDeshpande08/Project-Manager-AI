from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ProjectBase(BaseModel):
    name: str
    description: str

    project_type: str | None = None
    domain: str | None = None
    environment: str | None = None
    skill_level: str | None = None

    budget_min: float | None = None
    budget_max: float | None = None
    currency: str = "INR"

    power_source: str | None = None
    target_runtime_hours: float | None = None

    size_constraints: dict = Field(default_factory=dict)
    performance_constraints: dict = Field(default_factory=dict)
    environmental_constraints: dict = Field(default_factory=dict)
    preferences: dict = Field(default_factory=dict)

    functional_requirements: list = Field(default_factory=list)
    technical_requirements: list = Field(default_factory=list)
    constraints: list = Field(default_factory=list)


class ProjectCreate(ProjectBase):
    pass


class ProjectResponse(ProjectBase):
    id: int
    feasibility_score: float | None = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)