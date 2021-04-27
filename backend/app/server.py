from sanic import Sanic
from sanic.log import logger
from sanic.websocket import WebSocketProtocol

from app.views import gls_fake
from settings import Config


def run(config_object=Config):
    app = Sanic(__name__, strict_slashes=True)
    app.update_config(config_object)
    app.add_websocket_route(gls_fake, '/order_pallet/')

    try:
        app.go_fast(
            host=app.config['HOST'],
            port=app.config['PORT'],
            protocol=WebSocketProtocol,
            debug=app.config['DEBUG'],
            auto_reload=False
        )
    except Exception as ex:
        logger.exception("stop_app ex=%s", ex)
        raise

    return app


app = run()
