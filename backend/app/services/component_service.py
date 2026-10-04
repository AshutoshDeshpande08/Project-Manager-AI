from sqlalchemy.orm import Session

from app.models.component import Component


def search_components(
    db: Session,
    query: str | None = None,
    category: str | None = None,
    subcategory: str | None = None,
    limit: int = 20,
) -> list[Component]:

    components_query = db.query(Component)

    if category:
        components_query = components_query.filter(
            Component.category == category
        )

    if subcategory:
        components_query = components_query.filter(
            Component.subcategory == subcategory
        )

    components = components_query.all()

    if not query:
        return components[:limit]

    query_lower = query.lower().strip()
    query_words = query_lower.split()

    def field_matches(value: str) -> int:
        value_lower = value.lower()

        if query_lower == value_lower:
            return 10

        if query_lower in value_lower:
            return 6

        word_matches = sum(
            1
            for word in query_words
            if word in value_lower
        )

        return word_matches * 2

    def relevance_score(component: Component) -> int:
        score = 0

        # Core identity
        score += field_matches(component.name or "") * 3
        score += field_matches(component.description or "") * 2
        score += field_matches(component.category or "") * 2
        score += field_matches(component.subcategory or "")

        # Engineering knowledge
        for function in component.functions or []:
            score += field_matches(function) * 5

        for application in component.applications or []:
            score += field_matches(application) * 3

        for interface in component.interfaces or []:
            score += field_matches(interface) * 4

        # Search structured compatibility metadata
        compatibility = component.compatibility or {}

        for key, value in compatibility.items():
            score += field_matches(str(key)) * 2
            score += field_matches(str(value)) * 2

        return score

    scored_components = [
        (component, relevance_score(component))
        for component in components
    ]

    scored_components = [
        item
        for item in scored_components
        if item[1] > 0
    ]

    scored_components.sort(
        key=lambda item: item[1],
        reverse=True,
    )

    return [
        component
        for component, score in scored_components[:limit]
    ]