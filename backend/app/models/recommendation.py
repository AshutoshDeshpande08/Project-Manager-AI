from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import JSON

from app.database.base import Base


class Recommendation(Base):
    __tablename__ = "recommendations"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    component_id: Mapped[int] = mapped_column(
        ForeignKey("components.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    role: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    compatibility_score: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    electrical_score: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    functional_score: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    interface_score: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    power_score: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    physical_score: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    environmental_score: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    performance_score: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    cost_score: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    availability_score: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    complexity_score: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    estimated_cost: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        default=1,
    )

    reasons: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True,
    )

    warnings: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True,
    )

    alternatives: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    project = relationship(
        "Project",
        back_populates="recommendations",
    )

    component = relationship(
        "Component",
        back_populates="recommendations",
    )