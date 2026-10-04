from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.component import Component
from app.schemas.component import ComponentCreate, ComponentResponse
from app.services.component_service import search_components


router = APIRouter(
    prefix="/components",
    tags=["Components"],
)


@router.post(
    "/",
    response_model=ComponentResponse,
)
def create_component(
    component_data: ComponentCreate,
    db: Session = Depends(get_db),
):
    component = Component(
        **component_data.model_dump()
    )

    db.add(component)
    db.commit()
    db.refresh(component)

    return component


@router.get(
    "/",
    response_model=list[ComponentResponse],
)
def get_components(
    query: str | None = Query(default=None),
    category: str | None = Query(default=None),
    subcategory: str | None = Query(default=None),
    limit: int = Query(default=20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return search_components(
        db=db,
        query=query,
        category=category,
        subcategory=subcategory,
        limit=limit,
    )


@router.get(
    "/{component_id}",
    response_model=ComponentResponse,
)
def get_component(
    component_id: int,
    db: Session = Depends(get_db),
):
    component = db.query(Component).filter(
        Component.id == component_id
    ).first()

    if component is None:
        raise HTTPException(
            status_code=404,
            detail="Component not found",
        )

    return component