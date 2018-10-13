from typing import Tuple
from stats.support.server.core import Server, WebServer

SERVER: Server = WebServer()
WELCOME_MESSAGE: str = '<h1>NBA statistics telegram bot</h1>'
METHODS: Tuple[str, ...] = ('POST', 'GET')
POST: str = 'POST'

from . import routes
