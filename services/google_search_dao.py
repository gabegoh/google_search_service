from retry import retry
from sqlalchemy import TextClause, text, Row

from models.google_search_response import GoogleSearchResponse
from services.pg_engine import PGEngine


class GoogleSearchDAO:
    def __init__(self) -> None:
        self.__pg_engine: PGEngine = PGEngine()

    @retry(tries=5, delay=0.01, backoff=2, jitter=(-0.001, 0.001))
    def fetch_search_results(self, search_term: str) -> list[GoogleSearchResponse]:
        """
        Fetches all search results whose search_term = input
        """
        search_sql: TextClause = text(
            "SELECT "
            "   search_id, "
            "   search_term, "
            "   response, "
            "   status_coee, "
            "   is_deleted, "
            "   created_at "
            "FROM google_searches "
            "WHERE search_term = :input_search_term",
        )
        with self.__pg_engine.begin() as conn:
            """
            We used named params feature in sqlalchemy,
            to clean the input, before querying SQL with it
            This prevents SQL Injection Attacks
            """
            results: list[Row] = conn.execute(
                search_sql, {"input_search_term": search_term}
            )
            final_results: list[GoogleSearchResponse] = [
                GoogleSearchResponse.model_validate(
                    {
                        "search_id": row[0],
                        "search_term": row[1],
                        "response": row[2],
                        "status_code": row[3],
                        "is_deleted": row[4],
                        "created_at": row[5],
                    }
                )
                for row in results
            ]
            return final_results

    @retry(tries=5, delay=0.01, backoff=2, jitter=(-0.001, 0.001))
    def insert_search_results(self, results: GoogleSearchResponse) -> None:
        """
        Inserts results into database
        """
        insert_sql: TextClause = text(
            "INSERT INTO google_searches("
            "search_id, "
            "search_term, "
            "status_code, "
            "response, "
            "is_deleted, "
            "created_at"
            ") VALUES ("
            "   :search_id, "
            "   :search_term, "
            "   :status_code, "
            "   :response, "
            "   :is_deleted, "
            "   :created_at"
            ")",
        )
        with self.__pg_engine.begin() as conn:
            """
            We used named params feature in sqlalchemy,
            to clean the input, before querying SQL with it
            This prevents SQL Injection Attacks
            """
            conn.execute(
                insert_sql,
                {
                    "search_id": results.search_id,
                    "search_term": results.search_term,
                    "status_code": results.status_code,
                    "response": results.response,
                    "is_deleted": results.is_deleted,
                    "created_at": results.created_at,
                },
            )
