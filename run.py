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
    def get(self, method_id):
        db = torndb.Connection(
            host="localhost", database="PizzLab",
            user="root", password="shidomi")

        self.InsertData(db)
        self.UpdateData(db)
        self.DeleteData(db)
        self.ShowData(db)

        db.close()

    def InsertData(self, db):
        query = "insert into pizz_Customers (ID, NAME) values (1, 'Rafael')"
        db.insert(query)

    def UpdateData(self, db):
        query = "update pizz_Customers set ID = 2 where ID = 1"
        db.update(query)

    def DeleteData(self, db):
        query = "delete from pizz_Customers where ID = 2"
        db.update(query)

    def ShowData(self, db):
        query = "select * from pizz_Customers"
        rows = db.query(query)
        for row in rows:
            print(str(row["ID"]) + " | " + str(row["NAME"]))


def main():
    app = Application(
        [(r'/', MainHandler)],
	[(r"/method/([0-9]+)", MainHandler)],
        debug=settings.DEBUG
    )
    server = HTTPServer(app)
    server.listen(options.port)
    print ('Listening on http://localhost:{0}/'.format(settings.PORT))
    print ('Quit the server with CONTROL-C')
    ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
