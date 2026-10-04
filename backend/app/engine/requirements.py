from typing import Any


def extract_requirements(project: Any) -> dict:
    functional_requirements = []
    technical_requirements = []
    constraints = []

    for item in project.functional_requirements or []:
        functional_requirements.append(
            {
                "name": item,
                "description": item,
                "requirement_type": "functional",
                "category": "function",
                "priority": "high",
                "is_hard_requirement": False,
                "functions": [item],
                "confidence": 1.0,
            }
        )

    for item in project.technical_requirements or []:
        technical_requirements.append(
            {
                "name": item,
                "description": item,
                "requirement_type": "technical",
                "category": "technical",
                "priority": "high",
                "is_hard_requirement": False,
                "functions": [item],
                "confidence": 1.0,
            }
        )

    for item in project.constraints or []:
        constraints.append(
            {
                "name": item,
                "description": item,
                "requirement_type": "constraint",
                "category": "constraint",
                "priority": "critical",
                "is_hard_requirement": True,
                "functions": [],
                "confidence": 1.0,
            }
        )

    if project.budget_max is not None:
        constraints.append(
            {
                "name": "Maximum Budget",
                "description": f"Project budget must not exceed {project.budget_max} {project.currency}.",
                "requirement_type": "constraint",
                "category": "budget",
                "priority": "critical",
                "is_hard_requirement": True,
                "target_value": {
                    "maximum": project.budget_max,
                    "currency": project.currency,
                },
                "functions": [],
                "confidence": 1.0,
            }
        )

    if project.target_runtime_hours is not None:
        constraints.append(
            {
                "name": "Minimum Runtime",
                "description": (
                    f"System should operate for at least "
                    f"{project.target_runtime_hours} hours."
                ),
                "requirement_type": "constraint",
                "category": "power",
                "priority": "critical",
                "is_hard_requirement": True,
                "target_value": {
                    "minimum_hours": project.target_runtime_hours,
                },
                "functions": [],
                "confidence": 1.0,
            }
        )

    if project.power_source:
        constraints.append(
            {
                "name": "Power Source",
                "description": f"System must use {project.power_source} as its power source.",
                "requirement_type": "constraint",
                "category": "power",
                "priority": "high",
                "is_hard_requirement": True,
                "target_value": {
                    "source": project.power_source,
                },
                "functions": [],
                "confidence": 1.0,
            }
        )

    if project.environment:
        constraints.append(
            {
                "name": "Operating Environment",
                "description": f"System must operate in a {project.environment} environment.",
                "requirement_type": "constraint",
                "category": "environment",
                "priority": "high",
                "is_hard_requirement": True,
                "target_value": {
                    "environment": project.environment,
                },
                "functions": [],
                "confidence": 1.0,
            }
        )

    return {
        "functional_requirements": functional_requirements,
        "technical_requirements": technical_requirements,
        "constraints": constraints,
        "total_requirements": (
            len(functional_requirements)
            + len(technical_requirements)
            + len(constraints)
        ),
    }