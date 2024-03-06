from quart import Quart
from server.handler import Handler

class APIEntrypoint:
    def __init__(self):
        quart = Quart(__name__)
        handler = Handler()
        quart.add_url_rule("/random", view_func=handler.get_random, methods=["GET"])

        self.app = quart

    def launch(self):
        self.app.run(host="0.0.0.0")
