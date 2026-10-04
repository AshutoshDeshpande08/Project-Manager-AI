from app.database.base import Base
from app.database.connection import engine

from app.models.component import Component
from app.models.compatibility_rule import CompatibilityRule
from app.models.project import Project
from app.models.recommendation import Recommendation
from app.models.requirement import Requirement


def init_database() -> None:
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_database()
    print("Database initialized successfully.")