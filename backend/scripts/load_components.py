import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
BACKEND_DIR = PROJECT_ROOT / "backend"

sys.path.insert(0, str(BACKEND_DIR))

from app.database.connection import SessionLocal
from app.services.component_loader import load_components_from_file


COMPONENTS_DIR = PROJECT_ROOT / "data" / "components"


def main() -> None:
    db = SessionLocal()

    total_inserted = 0
    files_processed = 0

    try:
        dataset_files = sorted(
            COMPONENTS_DIR.glob("*/*.json")
        )

        for dataset_file in dataset_files:
            if dataset_file.name == "test_components.json":
                continue

            inserted = load_components_from_file(
                str(dataset_file),
                db,
            )

            total_inserted += inserted
            files_processed += 1

            print(
                f"{dataset_file.parent.name:20} "
                f"{dataset_file.name:35} "
                f"inserted: {inserted}"
            )

        print()
        print("=" * 65)
        print(f"Dataset files processed : {files_processed}")
        print(f"Total components added  : {total_inserted}")
        print("=" * 65)

    finally:
        db.close()


if __name__ == "__main__":
    main()