# __author__ = Issa Masumbuko

"""Repository-level pytest bootstrap for database-backed tests."""

from __future__ import annotations

import os
from collections.abc import Iterator

import pytest
from coordinatetbi.config import get_settings
from coordinatetbi.db import get_engine, reset_db_and_tables

DEFAULT_TEST_DB_URL = "postgresql+psycopg://postgres:postgres@postgres:5432/coordinatetbi_test"
TEST_DB_URL = os.environ.get("TEST_DATABASE_URL", DEFAULT_TEST_DB_URL)

os.environ["ENVIRONMENT"] = "test"
os.environ["TEST_DATABASE_URL"] = TEST_DB_URL
os.environ["DATABASE_URL"] = TEST_DB_URL


@pytest.fixture(scope="session", autouse=True)
def reset_postgres_test_database() -> Iterator[None]:
    """Reset the shared PostgreSQL test database before the suite runs."""
    get_settings.cache_clear()
    get_engine.cache_clear()
    reset_db_and_tables()
    yield
    get_engine.cache_clear()
    get_settings.cache_clear()
