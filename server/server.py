import tornado
from api.config import config_logger
import logging
from urls import urls

logger = config_logger(__name__)

application = tornado.web.Application(urls)


def run_server():
    application.listen(80, address='0.0.0.0')
    logger.info('Starting server on 8000...')
    tornado.ioloop.IOLoop.instance().start()

def run_local():
    application.listen(8000, address='0.0.0.0')
    logger.info('Starting server on 8000...')
    tornado.ioloop.IOLoop.instance().start()
