"""Database connectivity tests."""

from sqlalchemy import text

from app.db.database import SessionLocal


def test_database_connection() -> None:
    """The application should connect to PostgreSQL."""
    with SessionLocal() as db:
        result = db.execute(text("SELECT 1"))

        assert result.scalar_one() == 1


def test_database_connection_check_table_exists() -> None:
    """The initial Alembic-managed table should exist."""
    with SessionLocal() as db:
        result = db.execute(
            text(
                """
                SELECT to_regclass(
                    'public.database_connection_check'
                )
                """
            )
        )

        assert result.scalar_one() == "database_connection_check"


def test_database_connection_check_row_can_be_inserted() -> None:
    """The application should insert and read a test row."""
    with SessionLocal() as db:
        db.execute(
            text(
                """
                INSERT INTO database_connection_check (name)
                VALUES (:name)
                """
            ),
            {"name": "phase-2-test"},
        )
        db.commit()

        result = db.execute(
            text(
                """
                SELECT name
                FROM database_connection_check
                WHERE name = :name
                ORDER BY id DESC
                LIMIT 1
                """
            ),
            {"name": "phase-2-test"},
        )

        assert result.scalar_one() == "phase-2-test"