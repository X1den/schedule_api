
from pathlib import Path
import argparse

DEFAULT_TEMPLATE = """services:
  db:
    image: postgres:17
    environment:
      POSTGRES_DB: {db_name}
      POSTGRES_USER: {db_user}
      POSTGRES_PASSWORD: {db_password}
    ports:
      - "{host_port}:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
"""


def generate_compose(
    project_dir: Path,
    db_name: str,
    db_user: str,
    db_password: str,
    host_port: int,
) -> Path:
    project_dir = project_dir.resolve()
    target = project_dir / "compose.yaml"

    if not project_dir.is_dir():
        raise NotADirectoryError(
            f"Каталог проекта не существует: {project_dir}"
        )

    if target.exists():
        raise FileExistsError(
            f"Файл уже существует: {target}"
        )

    content = DEFAULT_TEMPLATE.format(
        db_name=db_name,
        db_user=db_user,
        db_password=db_password,
        host_port=host_port,
    )

    target.write_text(content, encoding="utf-8")
    return target


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Генератор compose.yaml с PostgreSQL"
    )
    parser.add_argument("project_dir", type=Path)
    parser.add_argument("--db-name", default="app_db")
    parser.add_argument("--db-user", default="app_user")
    parser.add_argument("--db-password", required=True)
    parser.add_argument("--port", type=int, default=5432)

    args = parser.parse_args()

    path = generate_compose(
        project_dir=args.project_dir,
        db_name=args.db_name,
        db_user=args.db_user,
        db_password=args.db_password,
        host_port=args.port,
    )

    print(f"Создан файл: {path}")


if __name__ == "__main__":
    main()
