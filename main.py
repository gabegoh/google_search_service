from typing import Any

from aiohttp import web

from models.google_search_response import GoogleSearchResponse
from services.google_search_service import GoogleSearchService

service: GoogleSearchService = GoogleSearchService()


async def index(request: web.Request) -> web.Response:
    return web.Response(text="Hello Aiohttp!")


async def perform_search(request: web.Request) -> web.Response:
    input_data: dict[str, Any] = await request.json()
    search_term: str = input_data.get("search_term", "")
    if not search_term:
        return web.json_response({"error": "search_term is required"}, status=400)
    result: GoogleSearchResponse = service.query_google_search(search_term)
    return web.json_response(result.model_dump())


app: web.Application = web.Application()
routes: web.RouteTableDef = web.RouteTableDef()


def setup_routes(app: web.Application) -> None:
    """
    Setup the routes, the API endpoints the users can access
    """
    app.router.add_get("/", index)
    app.router.add_post("/perform_search", perform_search)
    app.add_routes(routes)


setup_routes(app)


if __name__ == "__main__":
    web.run_app(app)
