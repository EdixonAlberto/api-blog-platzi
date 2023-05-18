import asyncio
from src.modules.server import Server


class Main():
  def __init__(self) -> None:
    server = Server()
    asyncio.run(server.start())
