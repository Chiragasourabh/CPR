import tornado.httpserver
import tornado.options
import tornado.escape
import tornado.ioloop
import tornado.web
import json
import os
from tornado.options import options,define
from handlers import *

define("PORT", default=8080, help="run on the given port", type=int)

class HealthHandler(tornado.web.RequestHandler):
    async def get(self):
        # self.content_type = 'application/json'
        # self.set_header("Content-Type", "application/json") 
        self.write(json.dumps({'status': 'up'}))
        self.set_header("Content-Type", "application/json")

def main():
    tornado.options.parse_command_line()
    HANDLERS = [
        (r"/health", HealthHandler),
        (r"/cpr", CPRHandler),

        ]

    application = tornado.web.Application(HANDLERS)
    # application.listen(options.PORT)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.PORT)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()