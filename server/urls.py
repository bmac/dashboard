from handlers import GitHubHandler, UserHandler, DashHandler, DataHandler
import tornado

urls = [
    (r"/js/(.*)",tornado.web.StaticFileHandler, {"path": "../client/js/"},),
    (r"/css/(.*)",tornado.web.StaticFileHandler, {"path": "../client/css/"},),
    (r"/([^/]+)[\/]?", DashHandler),
   (r"/([^/]+)/data[\/]?", DataHandler),
    (r"/([^/]+)/github[\/]?", GitHubHandler),
    (r"/([^/]+)/([^/]+)[\/]?", UserHandler),
    (r"/(.*)", tornado.web.StaticFileHandler, {'path': '../client/'}),
]
