from handlers import GraphHandler, GitHubHandler, RawHandler
import tornado

urls = [
    (r"/graph", GraphHandler),
    (r"/github", GitHubHandler),
    (r"/raw", RawHandler),
    (r"/(.*)", tornado.web.StaticFileHandler, {'path': '../client/'}),
]
