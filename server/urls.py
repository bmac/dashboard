from handlers import GraphHandler, GitHubHandler, RawHandler, UserHandler
import tornado

urls = [
    (r"/([^/]+)/graph", GraphHandler),
    (r"/github", GitHubHandler),
    (r"/raw", RawHandler),
    (r"/([^/]+)/", UserHandler),
    (r"/(.*)", tornado.web.StaticFileHandler, {'path': '../client/'}),
]
