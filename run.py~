# encoding: utf-8
import os
import datetime
import tornado.web as web
from tornado import ioloop
#from settings.routes import urls
from simple_settings import settings
from tornado.httpserver import HTTPServer
from tornado.web import Application, RequestHandler
from tornado.options import define, options, parse_command_line
from tornado_db import DbOperations

define("port", default=settings.PORT, help="run on the given port", type=int)

class MainHandler(RequestHandler):
    def get(self):
        cst = Customers()

        cst.telphone = 29898629
        cst.name = "Rafael"
        cst.address = "Av Maestro vila lobos"
        cst.neighborhood = "Tucuruvi"
        cst.number = 375
        cst.complement = 121
        cst.comments = "Mussarela sem azeite"

        cst.create_customer()

class Customers:
    def __init__(self, name = '', telphone = '', address = '', neighborhood = '', number = 0, complement = 0, comments = ''):
        self.name = name
        self.telphone = telphone
        self.address = address
        self.neighborhood = neighborhood
        self.number = number
        self.complement = complement
        self.comments = comments

    def create_customer(self):
        if(self.name != '' and self.telphone != '' and self.address != '' and self.neighborhood != '' and self.number > 0):

            createdOn = datetime.datetime.now()
            columns = "Telphone, Name, Address, Neighborhood, Number, Complement, Comments, CreatedOn"
            values = "'"+str(self.telphone)+"'" + "," + "'"+self.name+"'" + "," + "'"+self.address+"'" + "," + "'"+self.neighborhood+"'" + "," + str(self.number) + "," + str(self.complement) + "," + "'"+self.comments+"'" + "," + "'"+str(createdOn)+"'"

            query = "insert into pizz_Customers (%s) values (%s)" % (columns, values)
            db = DbOperations()
            db.insert_data(query)


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
