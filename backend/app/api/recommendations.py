from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.project import Project
from app.models.requirement import Requirement
from app.services.recommendation_service import retrieve_candidates


router = APIRouter(
    prefix="/projects",
    tags=["Recommendations"],
)


@router.get(
    "/{project_id}/candidates",
)
def get_project_candidates(
    project_id: int,
    db: Session = Depends(get_db),
):
    project = db.query(Project).filter(
        Project.id == project_id
    ).first()

    if project is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )

    requirements = (
        db.query(Requirement)
        .filter(
            Requirement.project_id == project_id
        )
        .order_by(Requirement.id)
        .all()
    )

    results = []

    for requirement in requirements:
        candidates = retrieve_candidates(
            db=db,
            project=project,
            requirement=requirement,
            limit=10,
        )

        results.append(
            {
                "requirement_id": requirement.id,
                "requirement": requirement.name,
                "requirement_type": requirement.requirement_type,
                "category": requirement.category,
                "candidates": [
                    {
                        "id": component.id,
                        "name": component.name,
                        "category": component.category,
                        "subcategory": component.subcategory,
                        "manufacturer": component.manufacturer,
                        "estimated_cost": component.estimated_cost,
                        "currency": component.currency,
                    }
                    for component in candidates
                ],
            }
        )

    return {
        "project_id": project_id,
        "requirements": results,
    }