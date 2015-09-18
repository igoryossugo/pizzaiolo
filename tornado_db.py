import tornado.ioloop
import tornado.web
import torndb

class DbOperations:

    def insert_data(self, query):
        db = torndb.Connection(
            host="localhost", database="PizzLab",
            user="root", password="shidomi")
        db.insert(query)
        db.close()
