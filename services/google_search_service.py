import urllib.parse
import requests
from retry import retry

from models.google_search_response import GoogleSearchResponse
from services.google_search_dao import GoogleSearchDAO


def url_encodes_search_term(search_term: str) -> str:
    """
    Makes a search term (contain space, etc) into a url compatible search term

    E.G https://www.google.com/search?q=coffee+coffee

    The search term "coffee coffee" will be url-encoded to "coffee+coffee""
    """
    encoded_search_term: str = urllib.parse.quote_plus(search_term)
    return encoded_search_term


class GoogleSearchService:
    """
    Responsible for making an API call to google search engine

    Receives a query input on behalf of a user, and makes the API call to google search

    Receive the result and save it to PostgreSQL (SQL database server)
    """

    def __init__(self) -> None:
        self.__google_search_dao: GoogleSearchDAO = GoogleSearchDAO()

    @retry(tries=5, delay=0.01, backoff=2, jitter=(-0.001, 0.001))
    def _query_google_search(self, search_term: str) -> GoogleSearchResponse:
        """
        If this fails, it tries up to 5 times
        - 1st retry with 0.01s delay
        - 2nd retry with 0.02s delay
        - 3rd retry with 0.04s delay
        - 4th retry with 0.08s delay
        """
        formatted_search_url: str = (
            f"https://www.google.com/search?q={url_encodes_search_term(search_term)}"
        )
        response: requests.Response = requests.get(formatted_search_url)
        final_response: GoogleSearchResponse
        if response.status_code == 200:
            body: str = response.text
            final_response = GoogleSearchResponse.create(
                search_term=search_term, status_code=response.status_code, response=body
            )
        else:
            final_response = GoogleSearchResponse.create(
                search_term=search_term, status_code=response.status_code, response=None
            )
        return final_response

    def query_google_search(self, search_term: str) -> GoogleSearchResponse:
        """
        Response for two steps:
        - Make the API call, get the response
        - (TODO) Persist the response in PostgreSQL
        """
        response: GoogleSearchResponse
        try:
            response = self._query_google_search(search_term=search_term)
            print("finished response")
        except Exception:
            """
            If it still fails, default to status_code=500, and save it to DB anyway
            """
            response = GoogleSearchResponse.create(
                search_term=search_term, status_code=500
            )
        finally:
            self.__google_search_dao.insert_search_results(results=response)

        return response


if __name__ == "__main__":
    service: GoogleSearchService = GoogleSearchService()
    result = service.query_google_search("coffee grinders")
