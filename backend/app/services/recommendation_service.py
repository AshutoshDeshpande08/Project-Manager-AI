from sqlalchemy.orm import Session

from app.models.component import Component
from app.models.project import Project
from app.models.requirement import Requirement
from app.services.component_service import search_components


def retrieve_candidates(
    db: Session,
    project: Project,
    requirement: Requirement,
    limit: int = 10,
) -> list[Component]:
    query = requirement.name

    candidates = search_components(
        db=db,
        query=query,
        limit=limit,
    )

    if candidates:
        return candidates

    if requirement.functions:
        for function in requirement.functions:
            candidates = search_components(
                db=db,
                query=function,
                limit=limit,
            )

            if candidates:
                return candidates

    return []