from sanic import Sanic
from settings import Config
from sanic.response import text


def create_app(config_object=Config, name='sanic'):
    app = Sanic(name)
    app.update_config(config_object)

    @app.get("/")
    async def hello_world(request):
        return text("Hello, world.")

    return app


app = create_app()
