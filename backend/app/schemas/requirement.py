from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class RequirementBase(BaseModel):
    project_id: int

    name: str
    description: str

    requirement_type: str
    category: str

    priority: str = "medium"

    is_hard_requirement: bool = False

    target_value: dict = Field(default_factory=dict)
    constraints: dict = Field(default_factory=dict)

    functions: list = Field(default_factory=list)

    extracted_from_text: str | None = None
    confidence: float | None = None


class RequirementCreate(RequirementBase):
    pass


class RequirementResponse(RequirementBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)