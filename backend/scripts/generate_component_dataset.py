import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
TAXONOMY_FILE = PROJECT_ROOT / "data" / "components" / "taxonomy.json"


def load_taxonomy() -> dict:
    if not TAXONOMY_FILE.exists():
        raise FileNotFoundError(f"Taxonomy file not found: {TAXONOMY_FILE}")

    with TAXONOMY_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise ValueError("Taxonomy must contain a JSON object.")

    return data


def main() -> None:
    taxonomy = load_taxonomy()

    total_target = 0

    print("\nEngineering Component Knowledge Base")
    print("=" * 45)

    for category, details in taxonomy.items():
        target = details.get("target_records", 0)
        priority = details.get("priority", "medium")
        subcategories = details.get("subcategories", [])

        total_target += target

        print(
            f"{category:20} | "
            f"{priority:10} | "
            f"{target:4} records | "
            f"{len(subcategories):2} subcategories"
        )

    print("=" * 45)
    print(f"Total target records: {total_target}")
    print("\nTaxonomy loaded successfully.")


if __name__ == "__main__":
    main()