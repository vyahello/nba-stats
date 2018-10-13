from stats.bot.message import Answer, BotAnswer, BotMessage
from stats.support.server import Server, SERVER, METHODS, POST, WELCOME_MESSAGE
from stats.support.server.requests import Request, ServerRequest

_server: Server = SERVER


@_server.route('/', methods=METHODS)
def index() -> str:
    request: Request = ServerRequest()
    answer: Answer = BotAnswer(request)

    if request.method() == POST:
        BotMessage(answer.chat_id(), answer.message()).send()

    return WELCOME_MESSAGE
