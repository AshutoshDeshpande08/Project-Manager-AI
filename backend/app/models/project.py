from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import JSON

from app.database.base import Base


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(250),
        nullable=False,
        index=True,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    project_type: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
        index=True,
    )

    domain: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
        index=True,
    )

    environment: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    skill_level: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    budget_min: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    budget_max: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    currency: Mapped[str] = mapped_column(
        String(10),
        default="INR",
    )

    power_source: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    target_runtime_hours: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    size_constraints: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    performance_constraints: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    environmental_constraints: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    preferences: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    functional_requirements: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True,
    )

    technical_requirements: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True,
    )

    constraints: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True,
    )

    feasibility_score: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )

    requirements = relationship(
        "Requirement",
        back_populates="project",
        cascade="all, delete-orphan",
    )

    recommendations = relationship(
        "Recommendation",
        back_populates="project",
        cascade="all, delete-orphan",
    )