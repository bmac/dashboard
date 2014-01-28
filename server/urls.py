from handlers import GitHubHandler, UserHandler, ProfileHandler
import tornado

urls = [
    (r"/([^/]+)[\/]?", ProfileHandler),
    (r"/([^/]+)/github[\/]?", GitHubHandler),
    (r"/([^/]+)/([^/]+)[\/]?", UserHandler),
    (r"/(.*)", tornado.web.StaticFileHandler, {'path': '../client/'}),
]
