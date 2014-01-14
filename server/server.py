import tornado

from urls import urls

application = tornado.web.Application(urls)

if __name__ == "__main__":
    #application.listen(80, address='0.0.0.0')
    application.listen(8000, address='0.0.0.0')
    tornado.ioloop.IOLoop.instance().start()
