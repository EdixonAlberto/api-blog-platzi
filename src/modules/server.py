
import uvicorn
from fastapi import FastAPI
from src.modules.config import Config
from src.middlewares import auth_midd
from src.routes import main_route, posts_route


class Server(Config):
  def __init__(self) -> None:
    super().__init__()
    self.app = FastAPI()
    self.middlewares()
    self.routes()

  def middlewares(self):
    self.app.middleware("http")(auth_midd.handler)

  def routes(self):
    self.app.include_router(main_route.router)
    self.app.include_router(posts_route.router)

  async def start(self):
    port_env = self.env('PORT')
    port: int = int(port_env) if port_env else 3000

    mode_dev = self.env('MODE_DEV')
    reload: bool = mode_dev == 'development'
    host: str = 'localhost' if mode_dev == 'development' else '0.0.0.0'

    config = uvicorn.Config('src.modules.server:app', host=host, port=port, log_level="info", reload=reload)
    server = uvicorn.Server(config)
    await server.serve()


app = Server().app
