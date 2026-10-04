from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.engine.requirements import extract_requirements
from app.models.project import Project
from app.models.requirement import Requirement
from app.schemas.project import ProjectCreate, ProjectResponse
from app.schemas.requirement import RequirementResponse


router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)


@router.post(
    "/",
    response_model=ProjectResponse,
)
def create_project(
    project_data: ProjectCreate,
    db: Session = Depends(get_db),
):
    project = Project(
        **project_data.model_dump()
    )

    db.add(project)
    db.commit()
    db.refresh(project)

    return project


@router.get(
    "/",
    response_model=list[ProjectResponse],
)
def get_projects(
    db: Session = Depends(get_db),
):
    return db.query(Project).order_by(Project.id.desc()).all()


@router.get(
    "/{project_id}",
    response_model=ProjectResponse,
)
def get_project(
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

    return project


@router.post(
    "/{project_id}/extract-requirements",
)
def generate_requirements(
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

    extracted = extract_requirements(project)

    db.query(Requirement).filter(
        Requirement.project_id == project_id
    ).delete()

    requirements = []

    for requirement_data in (
        extracted["functional_requirements"]
        + extracted["technical_requirements"]
        + extracted["constraints"]
    ):
        requirement = Requirement(
            project_id=project_id,
            name=requirement_data["name"],
            description=requirement_data["description"],
            requirement_type=requirement_data["requirement_type"],
            category=requirement_data["category"],
            priority=requirement_data["priority"],
            is_hard_requirement=requirement_data["is_hard_requirement"],
            target_value=requirement_data.get("target_value", {}),
            constraints=requirement_data.get("constraints", {}),
            functions=requirement_data.get("functions", []),
            extracted_from_text=project.description,
            confidence=requirement_data.get("confidence"),
        )

        db.add(requirement)
        requirements.append(requirement)

    db.commit()

    for requirement in requirements:
        db.refresh(requirement)

    return {
        "project_id": project_id,
        "total_requirements": len(requirements),
        "requirements": [
            RequirementResponse.model_validate(requirement)
            for requirement in requirements
        ],
    }