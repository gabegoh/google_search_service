import urllib
from typing import Any
import toml
from sqlalchemy import create_engine, Engine


class PGEngine:
    """
    Class responsible for establishing connection to Postgres
    """

    def __init__(self) -> None:
        with open("local_config/config.toml", "r") as f:
            self.__config: dict[str, Any] = toml.load(f)
        connection_str: str = self.connection_string(self.__config["database"])
        self.__engine: Engine = create_engine(connection_str)

    def begin(self):
        """
        Establish a single connection to the PSQL server
        """
        return self.__engine.begin()

    @staticmethod
    def connection_string(db_config: dict[str, Any]) -> str:
        host: str = db_config["host"]
        port: str = db_config["port"]
        database: str = db_config["database"]
        user: str = db_config.get("user", "")
        password: str = db_config.get("password", "")
        return (
            f"postgresql://{host}:{port}/{database}"
            if not user and not password
            else f"postgresql://{urllib.parse.quote(user)}:{urllib.parse.quote(password)}@{host}:{port}/{database}"
        )
