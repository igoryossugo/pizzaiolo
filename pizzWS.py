import tornado.ioloop
import tornado.web
from pymongo import Connection

class MainHandler(tornado.web.RequestHandler):
    def get(self):

	    con = Connection()
	    db = con.PizzLab1

	    customer = db.pizz_Customers

	    cstCollection = customer.find()

	    if cstCollection.count() == 0:
		    customer.insert({'PhoneNumber' : '011972114486', 
		    			   'Name' : 'Rafael Muller Shidomi',
		    			   'Address' : 'Av. Maestro Vila Lobos',
		    			   'Neighborhood' : 'Tucuruvi',
		    			   'AddressNumber' : '375',
		    			   'AddressComp' : '121',
		    			   'CustomerNote': 'Obs'})

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()