from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import JSON

from app.database.base import Base


class CompatibilityRule(Base):
    __tablename__ = "compatibility_rules"

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

    rule_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    category: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    condition: Mapped[dict] = mapped_column(
        JSON,
        nullable=False,
    )

    action: Mapped[dict] = mapped_column(
        JSON,
        nullable=False,
    )

    severity: Mapped[str] = mapped_column(
        String(50),
        default="warning",
    )

    score_impact: Mapped[float] = mapped_column(
        default=0.0,
    )

    is_hard_constraint: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    explanation_template: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )