import tornado.ioloop
import tornado.web
import sys
import sqlite3
from datetime import date
import time
import json

from requests import post, get

import config

def google_date(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

def timestamp(year, month, day):
    d = date(year, month, day)
    return time.mktime(d.timetuple())

class GraphHandler(tornado.web.RequestHandler):
    def get(self):
        user = self.get_argument('user', '')
        self.write(json.dumps("Graph"))

class GitHubHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(json.dumps("Github"))

class RawHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(json.dumps("Raw"))

application = tornado.web.Application([
    (r"/graph", GraphHandler),
    (r"/github", GitHubHandler),
    (r"/raw", RawHandler),
    (r"/(.*)", tornado.web.StaticFileHandler, {'path' : '../'}),
])

if __name__ == "__main__":
    application.listen(80, address='0.0.0.0')
    tornado.ioloop.IOLoop.instance().start()
