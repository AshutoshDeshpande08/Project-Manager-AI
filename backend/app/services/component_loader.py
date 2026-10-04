import json
from pathlib import Path

from sqlalchemy.orm import Session

from app.models.component import Component
from app.models.compatibility_rule import CompatibilityRule
from app.models.project import Project
from app.models.recommendation import Recommendation
from app.models.requirement import Requirement


def load_components_from_file(file_path: str, db: Session) -> int:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Component dataset not found: {file_path}")

    with path.open("r", encoding="utf-8") as file:
        components = json.load(file)

    if not isinstance(components, list):
        raise ValueError("Component dataset must contain a JSON list.")

    inserted = 0

    for component_data in components:
        part_number = component_data.get("part_number")

        if part_number:
            existing = (
                db.query(Component)
                .filter(Component.part_number == part_number)
                .first()
            )

            if existing:
                continue

        component = Component(**component_data)
        db.add(component)
        inserted += 1

    db.commit()

    return inserted