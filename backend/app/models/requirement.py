from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import JSON

from app.database.base import Base


class Requirement(Base):
    __tablename__ = "requirements"

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

    name: Mapped[str] = mapped_column(
        String(250),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    requirement_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True,
    )

    category: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    priority: Mapped[str] = mapped_column(
        String(50),
        default="medium",
    )

    is_hard_requirement: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    target_value: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    constraints: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    functions: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True,
    )

    extracted_from_text: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    confidence: Mapped[float | None] = mapped_column(
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    project = relationship(
        "Project",
        back_populates="requirements",
    )