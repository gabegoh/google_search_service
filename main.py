from aiohttp import web


async def index(request):
    return web.Response(text="Hello Aiohttp!")


app: web.Application = web.Application()
routes: web.RouteTableDef = web.RouteTableDef()


def setup_routes(app: web.Application) -> None:
    """
    Setup the routes, the API endpoints the users can access
    """
    app.router.add_get("/", index)
    app.add_routes(routes)


setup_routes(app)


if __name__ == "__main__":
    web.run_app(app)