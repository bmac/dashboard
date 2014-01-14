import tornado
import tornado.web
import json

from api.user import validate_api_key


class DBHandler(tornado.web.RequestHandler):
    def prepare(self):
        api_key = self.get_argument('user', '')
        if not api_key:
            # Throw error.
            pass
        user = validate_api_key(api_key)
        if not user:
            # Throw error.
            pass


class GraphHandler(DBHandler):
    def get(self):
        user = self.get_argument('user', '')
        self.write(json.dumps("Graph"))


class GitHubHandler(DBHandler):
    def get(self):
        self.write(json.dumps("Github"))


class RawHandler(DBHandler):
    def get(self):
        self.write(json.dumps("Raw"))
