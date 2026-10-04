from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import JSON

from app.database.base import Base


class Component(Base):
    __tablename__ = "components"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
        index=True,
    )

    part_number: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
        index=True,
    )

    manufacturer: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    category: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    subcategory: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    functions: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True,
    )

    applications: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True,
    )

    interfaces: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True,
    )

    electrical_specs: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    physical_specs: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    performance_specs: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    environmental_specs: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    compatibility: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    constraints: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    estimated_cost: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    currency: Mapped[str] = mapped_column(
        String(10),
        default="INR",
    )

    availability: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    alternatives: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True,
    )

    datasheet_url: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    documentation_url: Mapped[str | None] = mapped_column(
        Text,
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

    recommendations = relationship(
        "Recommendation",
        back_populates="component",
        cascade="all, delete-orphan",
    )