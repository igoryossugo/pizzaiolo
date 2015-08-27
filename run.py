# encoding: utf-8
import os
import tornado.web as web
from tornado import ioloop
#from settings.routes import urls
from simple_settings import settings
from tornado.httpserver import HTTPServer
from tornado.web import Application, RequestHandler
from tornado.options import define, options, parse_command_line

define("port", default=settings.PORT, help="run on the given port", type=int)

class MainHandler(RequestHandler):
    def get(self):
        data = {'status': 'ok', 'text': 'Hello World!'}
        self.write(data)

def main():
    app = Application(
        [(r'/', MainHandler)],
        debug=settings.DEBUG
    )
    server = HTTPServer(app)
    server.listen(options.port)
    print ('Listening on http://localhost:{0}/'.format(settings.PORT))
    print ('Quit the server with CONTROL-C')
    ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()