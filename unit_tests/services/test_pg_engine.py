from typing import Any

import pytest

from services.pg_engine import PGEngine


class TestPGEngine:
    @pytest.mark.parametrize(
        ["input", "output"],
        [
            [
                {
                    "host": "localhost",
                    "port": 5432,
                    "database": "google_search_service",
                },
                "postgresql://localhost:5432/google_search_service",
            ],
            [
                {
                    "host": "localhost",
                    "port": 5432,
                    "database": "google_search_service",
                    "user": "",
                    "password": "",
                },
                "postgresql://localhost:5432/google_search_service",
            ],
            [
                {
                    "host": "localhost",
                    "port": 5432,
                    "database": "google_search_service",
                    "user": "meow",
                    "password": "meow",
                },
                "postgresql://meow:meow@localhost:5432/google_search_service",
            ],
        ],
    )
    def test_connection_string(self, input: dict[str, Any], output: str) -> None:
        assert PGEngine.connection_string(input) == output
