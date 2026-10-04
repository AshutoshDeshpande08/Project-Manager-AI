from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ComponentBase(BaseModel):
    name: str
    part_number: str | None = None
    manufacturer: str | None = None

    category: str
    subcategory: str | None = None

    description: str | None = None

    functions: list[str] = Field(default_factory=list)
    applications: list[str] = Field(default_factory=list)
    interfaces: list[str] = Field(default_factory=list)

    electrical_specs: dict = Field(default_factory=dict)
    physical_specs: dict = Field(default_factory=dict)
    performance_specs: dict = Field(default_factory=dict)
    environmental_specs: dict = Field(default_factory=dict)

    compatibility: dict = Field(default_factory=dict)
    constraints: dict = Field(default_factory=dict)

    estimated_cost: float | None = None
    currency: str = "INR"

    availability: dict = Field(default_factory=dict)

    alternatives: list = Field(default_factory=list)

    datasheet_url: str | None = None
    documentation_url: str | None = None


class ComponentCreate(ComponentBase):
    pass


class ComponentResponse(ComponentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)